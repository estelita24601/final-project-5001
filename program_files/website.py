from flask import Flask, request, redirect, url_for
from jinja2 import Environment, FileSystemLoader
from task import TaskCollection

app = Flask(__name__)
# read task names from file into a list
master_task_collection = TaskCollection("test_input_data.csv")


@app.route("/home", methods=["POST", "GET"])
def home():
    # set up so template can be used
    my_environment = Environment(loader=FileSystemLoader("templates/"))
    task_list_template = my_environment.get_template(
        "home.html")

    # if user has interacted with website process data and do what's needed
    if request.method == "POST":
        form_data = request.form.to_dict()
        user_action = process_post_request(
            form_data, master_task_collection, "test_output_data.csv")

        # if user_action != "edit": return redirect(url_for("test_form", my_data=form_data))
        # # FIXME: remove when done with testing

    task_dictionary = master_task_collection.get_task_dictionary()

    # render the template with the task info from the file
    return task_list_template.render(task_data=task_dictionary)


@app.route("/testing<my_data>", methods=["POST", "GET"])
def test_form(my_data):
    return f"<p>{my_data}</p>"

# FIXME: the entire thing


@app.route("/edit<task_id>", methods=['POST', 'GET'])
def edit_task(task_id):
    my_environment = Environment(loader=FileSystemLoader("templates/"))
    task_editor_template = my_environment.get_template(
        "edit_task.html")

    task_to_edit = master_task_collection.get_task(task_id)

    return task_editor_template.render(task=task_to_edit)


def process_post_request(dict_data, task_collection_obj: TaskCollection, csv_file: str):

    for task_id, action in dict_data.items():
        print("-------ACTION VARIABLE =", action)  # FIXME
        id_number = int(task_id)
        task_obj = task_collection_obj.get_task(id_number)

        if action == 'delete':
            task_collection_obj.delete_task(id_number)
        elif action == 'edit':
            return redirect(url_for("edit_task", task_id=id_number))
        else:
            action = 'checkbox'
            task_obj.change_completion()

        task_collection_obj.update_csv(csv_file)

        return action
