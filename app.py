import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for,)
from markupsafe import Markup
from datetime import datetime
from flask_pymongo import PyMongo
from flask_wtf import CSRFProtect
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
csrf = CSRFProtect(app)


@app.template_filter("format_date")
def format_date(value, in_fmt="%Y-%m-%d", out_fmt="%d-%m-%Y"):
    """
    Convert a date string like 2025-11-20 into 20-11-2025 for display.
    If parsing fails, return the original value.
    """
    try:
        parsed = datetime.strptime(value, in_fmt)
        return parsed.strftime(out_fmt)
    except Exception:
        return value


@app.route("/")
@app.route("/get_welcome")
def get_welcome():
    """Landing page for the app."""
    return render_template("welcome.html")


@app.route("/get_tasks")
def get_tasks():
    tasks = list(
        mongo.db.tasks.find().sort("due_date", 1)   # chronological
    )

    return render_template("tasks.html", tasks=tasks)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"],
                request.form.get("password"),
            ):
                username = request.form.get("username").lower()
                session["user"] = username
                flash(f"Welcome, {username}!")
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>")
def profile(username):
    """
    Show the logged-in user's tasks. Redirects to login if there is no session.
    """
    user = session.get("user")
    if not user:
        flash("Please log in to view your profile.")
        return redirect(url_for("login"))

    if user != username.lower():
        flash("You can only view your own profile.")
        return redirect(url_for("profile", username=user))

    tasks = list(
        mongo.db.tasks.find({"created_by": user}).sort("due_date", 1)
    )
    return render_template("tasks.html", tasks=tasks)


@app.route("/logout")
def logout():
    """Clear the user session and return to the login page."""
    session.pop("user", None)
    flash("Thank you for using TaskTrackr™.    You have been logged out.")
    return redirect(url_for("get_welcome"))



@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    user = session.get("user")
    if not user:
        flash("Please log in to add a task.")
        return redirect(url_for("login"))

    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        task = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": user
        }
        mongo.db.tasks.insert_one(task)
        flash("Task Successfully Added")
        return redirect(url_for("get_tasks"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_task.html", categories=categories)

@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    user = session.get("user")
    if not user:
        flash("Please log in to edit tasks.")
        return redirect(url_for("login"))

    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": user
        }
        mongo.db.tasks.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": submit}
        )
        flash("Task Successfully Updated")
        return redirect(url_for("get_tasks"))

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_task.html", task=task, categories=categories)

@app.route("/delete_task/<task_id>", methods=["POST"])
def delete_task(task_id):
    mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_tasks"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
