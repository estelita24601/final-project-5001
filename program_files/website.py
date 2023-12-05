from flask import Flask, request, redirect, url_for
from jinja2 import Environment, FileSystemLoader
from task import TaskCollection

app = Flask(__name__)
# read task names from file into a list. make it only once for entire program to use
master_task_collection = TaskCollection("test_input_data.csv")
# set up so template can be used
my_environment = Environment(loader=FileSystemLoader("templates/"))

@app.route("/", methods=["POST", "GET"])
def home():
    task_list_template = my_environment.get_template("home.html")

    # if user has interacted with website
    if request.method == "POST":
        form_data = request.form.to_dict()
        user_action = process_post_request(form_data, master_task_collection, "test_output_data.csv")
        
        if user_action == 'edit':
            return redirect(url_for("edit_task", post_dict=form_data))

    # render the template with the task info from the file
    task_dictionary = master_task_collection.get_task_dictionary()
    return task_list_template.render(task_data=task_dictionary)

# FIXME: the entire thing
@app.route('/edit/<post_dict>', methods=['POST', 'GET'])
def edit_task(post_dict):
    task_editor_template = my_environment.get_template(
        "edit_task.html")

    for key in post_dict.keys():
        task_id = int(key)
        task_to_edit = master_task_collection.get_task(task_id)
    
    return task_editor_template.render(task=task_to_edit)


def process_post_request(post_dict, collection_of_tasks: TaskCollection, csv_file: str):
    for task_id, action in post_dict.items():
        print("-------ACTION VARIABLE =", action)  # FIXME
        id_number = int(task_id)

        if action in ('edit', 'create'):
            return action
        elif action == 'delete':
            collection_of_tasks.delete_task(id_number)
        else:
            task_obj = collection_of_tasks.get_task(id_number)
            task_obj.change_completion()
            
    collection_of_tasks.update_csv(csv_file)


@app.route("/testing<my_data>", methods=["POST", "GET"])
def test_form(my_data):
    return f"<h1>Testing Page</h1><p>{my_data}</p>"