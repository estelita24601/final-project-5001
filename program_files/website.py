from flask import Flask, render_template, request, redirect, url_for
from jinja2 import Environment, FileSystemLoader
from task import TaskCollection

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    # set up so template can be used
    my_environment = Environment(loader=FileSystemLoader("templates/"))
    task_list_template = my_environment.get_template(
        "home.html")

    # read task names from file into a list
    collection_of_tasks = TaskCollection("test_input_data.csv")
    task_dictionary = collection_of_tasks.get_task_dictionary()

    # if user hit submit lets get that data and display it on another screen for testing purposes
    # later we will process the data and re-render the template instead
    if request.method == "POST":
        form_data = request.form
        # user_action = form_data.get('name')
        # if user_action in ("checkbox", "delete task"):
        #     pass
        #     #FIXME: stay on same page, update csv file, then re-render the page
        # elif user_action == "edit":
        #     pass
        #     #FIXME: redirect to a different page that has a diff template for user input

        return redirect(url_for("test_form", my_data=form_data))
        # FIXME: remove when done with testing

    # render the template with the task info from the file
    return task_list_template.render(task_data=task_dictionary)


@app.route("/testing<my_data>", methods=["POST", "GET"])
def test_form(my_data):
    return f"<p>{my_data}</p>"
