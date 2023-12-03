from flask import Flask, render_template, request, redirect, url_for
from jinja2 import Environment, FileSystemLoader
from task import *

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    # set up so template can be used
    my_environment = Environment(loader=FileSystemLoader("templates/"))
    uss_voyager_template = my_environment.get_template(
        "voyager_task_format.html")

    # read task names from file into a list
    voyager_tasks = TaskList("voyager_tasks.csv")
    task_names = voyager_tasks.get_names()

    # if user hit submit lets get that data and display it on another screen for testing purposes
    # later we will process the data and re-render the template instead
    if request.method == "POST":
        form_data = request.form
        # FIXME: use this to update voyager_tasks.csv
        # FIXME: then update task_names so website renders

        return redirect(url_for("test_form", my_data=form_data))
        # FIXME: remove when done with testing

    # render the template with the list of tasks from the file
    return uss_voyager_template.render(task_list=task_names)


@app.route("/testing<my_data>", methods=["POST", "GET"])
def test_form(my_data):
    return f"<p>{my_data}</p>"
