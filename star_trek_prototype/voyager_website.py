from flask import Flask, render_template
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route("/")
def home():
    my_environment = Environment(loader = FileSystemLoader("templates/"))
    voyager_template = my_environment.get_template("voyager_task_format.html")

    voyager_list = []
    with open("fake_task_names.txt", "r") as captains_log:
        for task in captains_log:
            task = task.title()
            voyager_list.append(task)

    return voyager_template.render(task_list = voyager_list)