from flask import Flask, request, redirect, url_for
from jinja2 import Environment, FileSystemLoader
from task import Task, TaskCollection

app = Flask(__name__)

# read task names from file into a list. make it only once for entire program to use
master_task_collection = TaskCollection(
    "test_input_data.csv")  # FIXME: change filename

# set up so templates from folder can be used
my_environment = Environment(loader=FileSystemLoader("templates/"))


@app.route("/", methods=["POST", "GET"])
def home():
    # if user has interacted with website
    if request.method == "POST":
        form_data = request.form.to_dict()
        # FIXME:testing
        print(
            f"received {form_data} of type {type(form_data)} from post request")

        user_action = process_post_request(form_data, master_task_collection,
                                           "test_input_data.csv")  # FIXME: change file used for final version

        if user_action == 'edit':
            return redirect(url_for("task_editor", post_dict=form_data))

    # render the template with the task info from the file
    task_list_template = my_environment.get_template(
        "home_table_version.html")  # FIXME: put template here
    task_dictionary = master_task_collection.get_task_dictionary()
    return task_list_template.render(task_data=task_dictionary)


# helper for home()
def process_post_request(post_dict, collection_of_tasks: TaskCollection, csv_file: str):
    for key, action in post_dict.items():
        if key in ('new_name', 'new_date'):
            # this means user wants to make a new task
            create_task_from_request(post_dict)
        else:
            id_number = int(key)
            if action == 'edit':
                return action
            elif action == 'delete':
                collection_of_tasks.delete_task(id_number)
            else:
                # this means user clicked checkbox
                task_obj = collection_of_tasks.get_task(id_number)
                task_obj.change_completion()

    collection_of_tasks.update_csv(csv_file)


# helper for process_post_request()
def create_task_from_request(attribute_dict: dict):
    name = attribute_dict['new_name']
    date = attribute_dict['new_date']

    new_task = Task(name, due_date=date)
    master_task_collection.add_task(new_task)


@app.route('/edit/<post_dict>', methods=['POST', 'GET'])
def task_editor(post_dict):
    # even though argument given as a dictionary somehow it is a string here
    # so going to turn the string into what I need
    task_id = int(post_dict.split("'")[1])
    task_to_edit = master_task_collection.get_task(task_id)

    # check if user has hit submit button
    if request.method == "POST":
        form_data = request.form.to_dict()
        update_task(task_to_edit, form_data)
        return redirect('/')

    task_editor_template = my_environment.get_template("edit_task.html")
    return task_editor_template.render(task=task_to_edit)


# helper for task_editor
def update_task(task_obj, changes: dict):
    new_name = changes['update_name']
    new_date = changes['update_date']

    task_obj.change_name(new_name)
    task_obj.change_date(new_date)

    # FIXME: change filename for final version
    master_task_collection.update_csv("test_input_data.csv")
