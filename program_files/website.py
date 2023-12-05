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

    # if user has interacted with website process data and do what's needed
    if request.method == "POST":
        form_data = request.form.to_dict()
        print(form_data)  # FIXME
        process_post_request(
            form_data, collection_of_tasks, "test_output_data.csv")

        return redirect(url_for("test_form", my_data=form_data))
        # FIXME: remove when done with testing

    task_dictionary = collection_of_tasks.get_task_dictionary()

    # render the template with the task info from the file
    return task_list_template.render(task_data=task_dictionary)


@app.route("/testing<my_data>", methods=["POST", "GET"])
def test_form(my_data):
    return f"<p>{my_data}</p>"


@app.route("/edit<task_obj>", methods=['POST', 'GET'])
def edit_task(task_obj):
    return f"<p>I'm going to edit: {task_obj}</p>"


def process_post_request(dict_data, task_collection_obj: TaskCollection, csv_file: str) -> str:
    print(dict_data)  # FIXME

    for id, action in dict_data.items():
        id_number = int(id)
        print(id_number) #FIXME
        print(action) #FIXME
        user_task = task_collection_obj.get_task(id_number)

        if action == 'delete':
            task_collection_obj.delete_task(id_number)
        elif action == 'edit':
            return redirect(url_for("edit_task", task_obj=user_task))
        else:
            action = 'checkbox'
            user_task.change_completion()

        task_collection_obj.update_csv(csv_file)

        return action
