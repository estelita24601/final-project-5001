from flask import Flask, render_template, request, redirect, url_for
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    # set up so template can be used
    my_environment = Environment(loader = FileSystemLoader("templates/"))
    uss_voyager_template = my_environment.get_template("voyager_task_format.html")

    # read task names from file into a list
    uss_voyager_list = []
    with open("fake_task_names.txt", "r") as captains_log:
        for task in captains_log:
            task = task.title()
            uss_voyager_list.append(task)

    if request.method == "POST":
        form_data = request.form
        return redirect(url_for("test_form", my_data=form_data))

    # render the template with the list of tasks from the file
    return uss_voyager_template.render(task_list = uss_voyager_list)


@app.route("/testing<my_data>", methods=["POST", "GET"])
def test_form(my_data):
    return f"<h1>{my_data}</h1>"