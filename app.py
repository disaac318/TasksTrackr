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
@app.route("/get_tasks")
def get_tasks():
    tasks = list(
        mongo.db.tasks.find().sort("due_date", 1)   # chronological
    )

    return render_template("tasks.html", tasks=tasks)


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        task = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(task)
        flash("Task Successfully Added")
        return redirect(url_for("get_tasks"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_task.html", categories=categories)

@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
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
