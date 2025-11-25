import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, abort)
from datetime import datetime, timedelta
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


def current_greeting():
    """Return a time-of-day greeting."""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good Morning"
    if 12 <= hour < 18:
        return "Good Afternoon"
    return "Good Evening"


def is_admin(user_doc: dict | None) -> bool:
    """Return True if the user has an admin role."""
    return bool(user_doc and user_doc.get("role") == "admin")


def is_superadmin(user_doc: dict | None) -> bool:
    """Return True if the user has the superadmin role."""
    return bool(user_doc and user_doc.get("role") == "superadmin")


def is_frozen(user_doc: dict | None) -> bool:
    """Return True if the user account is frozen."""
    return bool(user_doc and user_doc.get("is_frozen"))


def generate_reset_token():
    """Generate a simple time-based token."""
    return generate_password_hash(str(datetime.utcnow()))


def get_current_user():
    """Return the current user document from session or None."""
    username = session.get("user")
    if not username:
        return None
    return mongo.db.users.find_one({"username": username})


@app.context_processor
def inject_user_context():
    """Provide current_user and is_admin flag to all templates without direct DB calls in Jinja."""
    user_doc = get_current_user()
    return {
        "current_user": user_doc,
        "is_admin_user": is_admin(user_doc),
        "is_superadmin_user": is_superadmin(user_doc),
        "is_frozen_user": is_frozen(user_doc),
    }


@app.route("/")
@app.route("/get_welcome")
def get_welcome():
    """Landing page for the app."""
    return render_template("welcome.html")


@app.route("/my_tasks")
def my_tasks():
    """
    Show only the tasks created by the logged-in user. Supports optional category filtering via ?category=<name>.
    """
    user = session.get("user")
    if not user:
        flash("Please log in to view your tasks.")
        return redirect(url_for("login"))

    selected_category = request.args.get("category", "").strip()

    query = {"created_by": user}
    if selected_category:
        query["category_name"] = selected_category

    tasks = list(
        mongo.db.tasks.find(query).sort("due_date", 1)
    )
    categories = list(mongo.db.categories.find().sort("category_name", 1))

    # Annotate tasks with RAG status based on due_date proximity.
    today = datetime.today().date()
    for task in tasks:
        rag_class = ""
        due_raw = task.get("due_date")
        try:
            due_dt = datetime.strptime(due_raw, "%Y-%m-%d").date() if due_raw else None
        except Exception:
            due_dt = None

        if due_dt:
            days_until_due = (due_dt - today).days
            if days_until_due <= 0:
                rag_class = "rag-red"
            elif days_until_due <= 2:
                rag_class = "rag-amber"
            else:
                rag_class = "rag-green"
        task["rag_class"] = rag_class

    return render_template(
        "my_tasks.html",
        tasks=tasks,
        categories=categories,
        selected_category=selected_category,
        greeting=current_greeting(),
    )


@app.route("/profile/<username>")
def profile(username):
    """
    Legacy profile route: redirect to my_tasks for consistency.
    """
    user = session.get("user")
    if not user:
        flash("Please log in to view your profile.")
        return redirect(url_for("login"))

    return redirect(url_for("my_tasks"))


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
            "password": generate_password_hash(request.form.get("password")),
            "role": "user",
            "is_frozen": False,
            "failed_logins": 0,
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("my_tasks"))
    return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if is_frozen(existing_user):
                flash("Account is frozen. Please contact a superadmin.")
                return redirect(url_for("login"))

            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"],
                request.form.get("password"),
            ):
                username = request.form.get("username").lower()
                session["user"] = username
                mongo.db.users.update_one(
                    {"_id": existing_user["_id"]},
                    {"$set": {"failed_logins": 0}}
                )
                flash(f"Welcome, {username}!")
                return redirect(url_for("my_tasks"))
            else:
                # invalid password match
                failed = existing_user.get("failed_logins", 0) + 1
                updates = {"failed_logins": failed}
                freeze = False
                if failed >= 3:
                    updates["is_frozen"] = True
                    freeze = True
                mongo.db.users.update_one(
                    {"_id": existing_user["_id"]},
                    {"$set": updates}
                )
                if freeze:
                    flash("Account frozen after too many failed attempts. Contact a superadmin.")
                else:
                    flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")



# @app.route("/profile/<username>")
# def profile(username):
#     """
#     Show the logged-in user's tasks. Redirects to login if there is no session.
#     """
#     user = session.get("user")
#     if not user:
#         flash("Please log in to view your profile.")
#         return redirect(url_for("login"))

#     if user != username.lower():
#         flash("You can only view your own profile.")
#         return redirect(url_for("profile", username=user))

#     tasks = list(
#         mongo.db.tasks.find({"created_by": user}).sort("due_date", 1)
#     )
#     return render_template("tasks.html", tasks=tasks)


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
        return redirect(url_for("my_tasks"))

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
        return redirect(url_for("my_tasks"))

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_task.html", task=task, categories=categories)

@app.route("/delete_task/<task_id>", methods=["POST"])
def delete_task(task_id):
    user_doc = get_current_user()
    if not user_doc:
        flash("Please log in to delete tasks.")
        return redirect(url_for("login"))

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    if not task:
        abort(404)

    # Only owner or superadmin can delete
    if not is_superadmin(user_doc) and task.get("created_by") != user_doc["username"]:
        abort(403)

    mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    # Redirect based on role
    if is_superadmin(user_doc):
        return redirect(url_for("admin_tasks"))
    return redirect(url_for("my_tasks"))


@app.route("/admin/users")
def admin_users():
    """
    Superadmin-only: list users and allow role toggling.
    """
    user_doc = get_current_user()
    if not is_superadmin(user_doc):
        abort(403)

    users = list(mongo.db.users.find().sort("username", 1))
    return render_template("admin_users.html", users=users)


@app.route("/admin/users/<user_id>/toggle_role", methods=["POST"])
def toggle_role(user_id):
    """
    Superadmin-only: toggle a user's role between admin and user.
    Superadmin cannot demote themselves or other superadmins.
    """
    user_doc = get_current_user()
    if not is_superadmin(user_doc):
        abort(403)

    target = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if not target:
        abort(404)

    # Prevent demoting self
    if target["username"] == user_doc["username"]:
        flash("You cannot change your own role.")
        return redirect(url_for("admin_users"))

    # Prevent altering other superadmins
    if is_superadmin(target):
        flash("You cannot change another superadmin's role.")
        return redirect(url_for("admin_users"))

    # Toggle admin/user
    new_role = "admin" if target.get("role") != "admin" else "user"
    mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"role": new_role}})
    flash(f"Updated {target['username']} to role: {new_role}")
    return redirect(url_for("admin_users"))


@app.route("/admin/users/<user_id>/delete", methods=["POST"])
def delete_user(user_id):
    """
    Superadmin-only: delete a user account and their tasks.
    Cannot delete self or any superadmin.
    """
    user_doc = get_current_user()
    if not is_superadmin(user_doc):
        abort(403)

    target = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if not target:
        abort(404)

    if target["username"] == user_doc["username"]:
        flash("You cannot delete your own account.")
        return redirect(url_for("admin_users"))

    if is_superadmin(target):
        flash("You cannot delete a superadmin account.")
        return redirect(url_for("admin_users"))

    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    mongo.db.tasks.delete_many({"created_by": target["username"]})
    flash(f"Deleted user {target['username']} and their tasks.")
    return redirect(url_for("admin_users"))


@app.route("/admin/users/<user_id>/toggle_freeze", methods=["POST"])
def toggle_freeze(user_id):
    """
    Superadmin-only: freeze/unfreeze a user's account.
    """
    user_doc = get_current_user()
    if not is_superadmin(user_doc):
        abort(403)

    target = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if not target:
        abort(404)

    if target["username"] == user_doc["username"]:
        flash("You cannot freeze or unfreeze your own account.")
        return redirect(url_for("admin_users"))

    if is_superadmin(target):
        flash("You cannot freeze a superadmin account.")
        return redirect(url_for("admin_users"))

    new_state = not target.get("is_frozen", False)
    mongo.db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"is_frozen": new_state, "failed_logins": 0}}
    )
    flash(f"{'Frozen' if new_state else 'Unfrozen'} user {target['username']}.")
    return redirect(url_for("admin_users"))


@app.route("/reset_request", methods=["GET", "POST"])
def reset_request():
    """
    Allow a user to request a password reset token.
    In a real deployment, this would email the token link.
    Here we display the link after generating it.
    """
    reset_link = None
    if request.method == "POST":
        username = request.form.get("username", "").lower().strip()
        user = mongo.db.users.find_one({"username": username})
        if user:
            token = generate_reset_token()
            expires = datetime.utcnow() + timedelta(hours=1)
            mongo.db.users.update_one(
                {"_id": user["_id"]},
                {"$set": {"reset_token": token, "reset_expires": expires}}
            )
            reset_link = url_for("reset_password", token=token, _external=True)
            flash("Reset link generated (valid for 1 hour).")
        else:
            flash("If the account exists, a reset link has been generated.")
        return render_template("reset_request.html", reset_link=reset_link)

    return render_template("reset_request.html", reset_link=reset_link)


@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    """
    Reset password using a token.
    """
    user = mongo.db.users.find_one({"reset_token": token})
    if not user:
        flash("Invalid or expired reset token.")
        return redirect(url_for("login"))

    expires = user.get("reset_expires")
    if not expires or expires < datetime.utcnow():
        flash("Reset token has expired.")
        return redirect(url_for("login"))

    if request.method == "POST":
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        if not password or password != confirm:
            flash("Passwords do not match.")
            return redirect(url_for("reset_password", token=token))

        mongo.db.users.update_one(
            {"_id": user["_id"]},
            {"$set": {
                "password": generate_password_hash(password),
                "failed_logins": 0,
                "is_frozen": False
            },
                "$unset": {"reset_token": "", "reset_expires": ""}
            }
        )
        flash("Password updated. Please log in.")
        return redirect(url_for("login"))

    return render_template("reset_password.html", token=token)


@app.route("/admin/tasks")
def admin_tasks():
    """
    Superadmin-only: view all tasks across users.
    """
    user_doc = get_current_user()
    if not is_superadmin(user_doc):
        abort(403)

    selected_user = request.args.get("owner", "").strip()
    query = {}
    if selected_user:
        query["created_by"] = selected_user

    tasks = list(mongo.db.tasks.find(query).sort("due_date", 1))
    users = list(mongo.db.users.find().sort("username", 1))
    return render_template(
        "admin_tasks.html",
        tasks=tasks,
        users=users,
        selected_user=selected_user,
    )


@app.route("/admin/tasks/<task_id>/delete", methods=["POST"])
def admin_delete_task(task_id):
    """
    Superadmin-only: delete any task.
    """
    user_doc = get_current_user()
    if not is_superadmin(user_doc):
        abort(403)

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    if not task:
        abort(404)

    mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
    flash("Task deleted.")
    return redirect(url_for("admin_tasks"))


@app.route("/admin/categories", methods=["GET", "POST"])
def admin_categories():
    """
    Superadmin-only: manage categories.
    """
    user_doc = get_current_user()
    if not is_superadmin(user_doc):
        abort(403)

    if request.method == "POST":
        name = request.form.get("category_name", "").strip()
        if not name:
            flash("Category name is required.")
        else:
            existing = mongo.db.categories.find_one({"category_name": name})
            if existing:
                flash("Category already exists.")
            else:
                mongo.db.categories.insert_one({"category_name": name})
                flash("Category added.")
        return redirect(url_for("admin_categories"))

    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("admin_categories.html", categories=categories)


@app.route("/admin/categories/<category_id>/delete", methods=["POST"])
def delete_category(category_id):
    """
    Superadmin-only: delete a category if no tasks reference it.
    """
    user_doc = get_current_user()
    if not is_superadmin(user_doc):
        abort(403)

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    if not category:
        abort(404)

    in_use = mongo.db.tasks.count_documents({"category_name": category["category_name"]})
    if in_use:
        flash("Cannot delete a category that is in use by tasks.")
        return redirect(url_for("admin_categories"))

    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category deleted.")
    return redirect(url_for("admin_categories"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
