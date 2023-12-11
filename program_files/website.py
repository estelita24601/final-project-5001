import json
from flask import Flask, request, redirect, url_for
from jinja2 import Environment, FileSystemLoader
from task import Task, TaskCollection

app = Flask(__name__)

REQUEST_HISTORY = "request_history.json"
SAVE_FILE = "save_file.csv"
# read task names from file into our TaskCollection object. make it only once for entire program to use
MASTER_TASK_LIST = TaskCollection(SAVE_FILE)

# set up so templates from folder can be used
MY_ENVIRONMENT = Environment(loader=FileSystemLoader("templates/"))
HOME_TEMPLATE = "home_page.html"
EDITOR_TEMPLATE = "edit_task.html"


@app.route("/", methods=["POST", "GET"])
def home():
    # if user has interacted with website
    if request.method == "POST":
        # get the info about user interaction in dictionary form
        form_data = request.form.to_dict()

        # load the previous request from JSON file
        with open(REQUEST_HISTORY, "r") as request_file:
            previous_request = json.load(request_file)

        # if this is a new request the update JSON file and process the request
        if form_data != previous_request:
            # update the previous request
            with open(REQUEST_HISTORY, "w") as request_file:
                json.dump(form_data, request_file)

            user_action = process_post_request(form_data, MASTER_TASK_LIST, SAVE_FILE)
            if user_action == "edit":
                return redirect(url_for("task_editor", post_dict=form_data))

    # render the template with the task info from the file
    task_list_template = MY_ENVIRONMENT.get_template(HOME_TEMPLATE)
    task_dictionary = MASTER_TASK_LIST.get_task_dictionary()
    return task_list_template.render(task_data=task_dictionary)


# helper for home()
def process_post_request(post_dict, collection_of_tasks: TaskCollection, csv_file: str):
    """_summary_

    Args:
        post_dict (_type_): _description_
        collection_of_tasks (TaskCollection): _description_
        csv_file (str): _description_

    Returns:
        _type_: _description_
    """

    for key, action in post_dict.items():
        # post_dict for new tasks has different format so check for that
        if key in ("new_name", "new_date"):
            create_task_from_request(post_dict)
            break
        else:
            id_number = int(key)
            if action == "edit":
                return action  # return to home() function to redirected to editor url
            if action == "delete":
                collection_of_tasks.delete_task(id_number)
            elif action in ("checkbox", "True"):
                # this means user clicked checkbox
                task_obj = collection_of_tasks.get_task(id_number)
                task_obj.change_completion()

    collection_of_tasks.update_csv(csv_file)


# helper for process_post_request()
def create_task_from_request(attribute_dict: dict):
    name = attribute_dict["new_name"]
    date = attribute_dict["new_date"]

    new_task = Task(name, due_date=date)
    MASTER_TASK_LIST.add_task(new_task)


@app.route("/edit/<post_dict>", methods=["POST", "GET"])
def task_editor(post_dict):
    # parsing a dictionary in string form to get task id
    task_id = int(post_dict.split("'")[1])
    task_to_edit = MASTER_TASK_LIST.get_task(task_id)

    # if user hit the submit button then update task and return home
    if request.method == "POST":
        form_data = request.form.to_dict()
        update_task(task_to_edit, form_data)
        return redirect("/")

    task_editor_template = MY_ENVIRONMENT.get_template(EDITOR_TEMPLATE)
    return task_editor_template.render(task=task_to_edit)


# helper for task_editor
def update_task(task_obj, changes: dict):
    new_name = changes["update_name"]
    new_date = changes["update_date"]

    # only update task object if name/date fields weren't empty
    if new_name:
        task_obj.change_name(new_name)
    if new_date:
        task_obj.change_date(new_date)

    MASTER_TASK_LIST.update_csv(SAVE_FILE)
