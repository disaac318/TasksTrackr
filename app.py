import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
