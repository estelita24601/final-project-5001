# Final Project Report

* Student Name: Estelita Chen
* Github Username: estelita24601
* Semester: Fall 2023
* Course: CS 5001

## Description

This is a To-Do List website created using Flask and Python. You can create new tasks and edit or delete existing ones. This project was inspired by the spreadsheet I use to keep track of my schoolwork.

## Key Features

In addition to creating, editing, and deleting tasks, the website also saves whatever changes you make so they are still there if you leave and come back later. 

## Guide

<u>To create a new task:</u>

* enter the name of the task in the textbox

* if there is a due date, use the date field either by typing or using the pop-up calendar

* press the "create new task" button

<u>To delete a task:</u>

* click the "delete" button on the same row as the task you want to delete

<u>To mark a task as complete or incomplete:</u>

* click the checkbox to the left of the task (a blue checkmark indicates the task is complete, and an empty white checkbox indicates the task is not complete)

<u>To edit a task:</u>

* click the "edit" button to the right of the task you want to edit

* you will be brought to a new page where you can enter a name and optional date in the same manner you would when creating a new task

* click the "save changes" button to finish editing the task and be brought back to the main view with all tasks

NOTE: please click at a normal speed, I haven't been able to fix a bug that occurs with rapid consecutive clicks on the same button/checkbox.

## Installation Instructions

* download flask: ```pip install flask```

* To launch the website navigate to the ```program_files``` directory on the command line and type the following: `python -m flask --app website.py run`

* Click on the link (Ctrl+Click) to open the website on your browser.

* Type Ctrl+C to shut down the server

## Code Review

#### <u>[website.py](https://github.com/estelita24601/final-project-5001/blob/bf1eb650e62033d3d107b5aa631688ef4390881d/program_files/website.py)</u>

```python
@app.route("/", methods=["POST", "GET"])
def home():
```

This function is for the homepage of the website. The decorator specifies the URL and what HTTP requests will be handled by it. 

The post request is used to get information from the website whenever a form is submitted. 

* if a post request has been detected the home() function will take that information and put it into dictionary form inside of the variable `form_data`

* Because Flask will resend a duplicate post request when the page is refreshed, the program will compare the request to `request_history.json` to prevent the bugs that would occur otherwise. 

* After confirming this post request isn't the result of a page refresh the program will update ```request_history.json``` and then use  ```process_post_request()``` to execute whatever is needed to complete the user's request.

* `process_post_request()` can handle deleting tasks, changing checkboxes, and creating new tasks with helper functions. However for editing tasks `process_post_request` will return `"edit"` and the `home()` function will then redirect to a different webpage.

```python
if user_action == "edit":
                return redirect(url_for("task_editor", post_dict=form_data))

@app.route("/edit/<post_dict>", methods=["POST", "GET"])
def task_editor(post_dict):
```

* The webpage for editing is created by `task_editor()` which has a custom URL that allows me to pass on information from `home()`

* `url_for()` creates a URL that follows the necessary format for `task_editor` and inserts the variable `form_data` into the URL as a string. `task_editor` then takes that string and puts it into the variable `post_dict`
  
  * it would have perhaps been better to use JSON format 

* `post_dict` is processed to get the task the user wants to edit and display it in the textbox and date input elements. 

* `task_editor()` then waits to receive another post request from the "save changes" button to save the changes to the CSV and redirect back to the homepage

* after any post requests have been dealt with `home()` and `task_editor()` get the HTML template they're associated with and return the template to the front end in a get request. `.render(variable_name = my_info)` is used on the template to pass along what information the webpage needs to display.

#### <u> HTML Templates + Jinja2</u>

<u>[home_page.html](https://github.com/estelita24601/final-project-5001/blob/bf1eb650e62033d3d107b5aa631688ef4390881d/program_files/templates/home_page.html)</u>

* template for the home page of the website where the user will spend most of their time. Lists out all the tasks and has a GUI to interact with tasks in the list

```jinja2
{% for task_id in task_data %}
        <!-- use the dictionary entry to get info on each task object-->
        {% set task_obj = task_data[task_id] %}
        {% set name_value = task_obj.get_name() %}
        {% set check_status = task_obj.get_completion_status() %}
        {% set date = task_obj.get_display_date() %}
```

* When this template was rendered the variable `task_data` received a dictionary of task objects. Using Jinja I can loop through every task in the dictionary and extract the information I want to display

```html
<form action="" method="post" name="new task">
    <input type="text" name="new_name" value="enter name of task here" />
    <input type="date" name="new_date" />
    <input type="submit" value="create new task" />
</form>
```

- This creates the text input field, the date input field, and the "create new task button" and puts them together in the same form so when the submit button is pressed the rest of the information is also sent

```html
<form action="" method="post" name="checkbox" onclick="submit();">
    {% if check_status == true %}
        <input type="checkbox" name="{{task_id}}" value="True" checked />
    {% else %}
        <input type="checkbox" name="{{task_id}}" value="True" />
     {% endif %}
    <input type="hidden" name="{{task_id}}" value="checkbox" />
</form>
```

* creates a checkbox for every task and loads it already checked off if needed. Has a hidden input type so the form still sends information when something is unchecked.

```html
<form action="" method="post" name="edit task">
    <input type="submit" name="{{task_id}}" value="edit" />
</form>

<form action="" method="post" name="delete task">
    <input type="submit" name="{{task_id}}" value="delete" />
</form>
```

* the edit and delete buttons are created in the same column of the table but separate forms so they only send information on themselves when clicked.

(for all the html input elements above `name=` and `value=` get returned to the flask application in the post request as a key value pair so they were chosen strategically so they could be more easily processed)

[edit_task.html](https://github.com/estelita24601/final-project-5001/blob/bf1eb650e62033d3d107b5aa631688ef4390881d/program_files/templates/edit_task.html)

* When a user wants to edit a task they get redirected to a page that renders this html file.

* Has a text input field, date input field, and a button that will save the information and return the user to the home page.

#### <u>[task.py](https://github.com/estelita24601/final-project-5001/blob/bf1eb650e62033d3d107b5aa631688ef4390881d/program_files/task.py)</u>

[`Task`](https://github.com/estelita24601/final-project-5001/blob/bf1eb650e62033d3d107b5aa631688ef4390881d/program_files/task.py#L4) class - make every individual task an object with a name, date, id number, and completion status. 

* date is an optional parameter that will create a datetime object if given a string in the correct ISO format (YYYY-MM-DD) otherwise it will have a value of `None`

* the id number is created with `self.unique_id = id(self)` and is used as the key for this object whenever it is put into a dictionary. 

* ```python
  def to_csv(self) -> str:
          unique_id = str(self.unique_id)
          is_complete = str(self.is_complete)
  
          try:
              due_date = self.date.isoformat()
          except AttributeError:
              due_date = "None"
  
          return ",".join((unique_id, self.name, is_complete, due_date))
  ```

* `to_csv()` is mostly used by the `TaskCollection` class to update csv files. It takes all the attributes of the object and turns them into strings which it then transforms into CSV format. The exception handling is for cases when the task doesn't have a date and `self.date` is not a date object

[`TaskCollection`](https://github.com/estelita24601/final-project-5001/blob/bf1eb650e62033d3d107b5aa631688ef4390881d/program_files/task.py#L115) class - a container for all of the task objects that will be displayed on the website. 

* `__init__` 
  
  * reads a CSV file using the helper function `task_from_csv()` to create a `Task` object with the correct attributes for each line in the file. 
  
  * These objects are all put into a dictionary using `create_obj_dict()`, with the keys being the unique id numbers of the task object, and the value being the task objects themselves. 
  
  * The CSV file is then updated to reflect the unique id numbers for each object

* `update_csv()` and `create_csv_list()`
  
  * `create_csv_list()` is a helper function for `update_csv()`. It uses list comprehension to convert every task object in the dictionary into a CSV formatted string with the task object's `to_csv()` method.

**General Comments on the Code**

* Since the id numbers for each task are based on location in memory there is only one instance of `TaskCollection` created so that each task is also only created once. This is done in the global scope of `website.py` to prevent new instances from being created whenever the page reloads or re-renders. This way each instance of `Task` has a unique id number that doesn't change during the runtime of the program, even if it is edited in any way.

* I think using JSON instead of .csv would have made the code more readable by cutting down on all the string formatting and parsing I had to do to convert to and from a dictionary.

* Currently I am re-writing the entire CSV file any time a change is made and then re-rendering the template. It would be more efficient instead to make edits to the CSV file. It would still require a loop to find the correct line to edit or delete, but would often finish early. Meanwhile adding a task wouldn't require a loop at all anymore and would be much faster.

### Major Challenges

* The first major hurdle was figuring out what a post request was and how to handle them. At first, I could only send a post request if the user hit a submit button after every change, and it would send information about every single input element on the page which was harder to process. When I started to better understand how `<input>` and `<form>` worked I was able to set up my HTML page to send smaller and easier to understand post requests whenever the user interacted with the website.

* The hardest bug to figure out was the website crashing or malfunctioning whenever the user refreshed the page. I realized the website was sending the previous post request a second time whenever refreshing, and it seemed the conventional fix was to use JavaScript to override Flask's default behavior. Then I realized instead of preventing duplicate requests from being made I could have my program just ignore those duplicate requests. I used a JSON file to save the most recent post request so it could be compared to the next post request sent.

* I still haven't been able to figure out the rapid clicking bug. My suspicion is that clicking too quickly interrupts the program writing to the CSV or JSON which then causes confusion. I only discovered it recently since the speed of clicking needed to cause a problem doesn't happen naturally.

### Example Run

* [5001 Final Project Demo - YouTube](https://www.youtube.com/watch?v=F8nvG_GGA0Q&ab_channel=Ita)

## Testing

How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

* In the repository there's a folder named [testing](https://github.com/estelita24601/final-project-5001/tree/bf1eb650e62033d3d107b5aa631688ef4390881d/testing) that contains my tests.

* I extended `unittest` and wrote tests for all the methods in `Task` (https://github.com/estelita24601/final-project-5001/blob/bf1eb650e62033d3d107b5aa631688ef4390881d/testing/test_task.py)

* I also wrote a test class for `TaskCollection` however some methods couldn't be checked by `.assert` as easily so I had those methods update a CSV file so I could manually see if the output matched what I expected.

* Testing flask was harder but I ended up using a lot of print statements that would show up on the command line and were very helpful for debugging.

* To test my html input elements and post requests I created a temporary webpage that all forms would redirect to that displayed the post request. This also helped me figure out the best format for the data I sent in my post requests. I would also keep my CSV file open to the side to make sure it was being edited correctly. As the website progressed I had to get rid of the temporary webpage and switch to more print statements.
  ![]![image](https://github.com/estelita24601/final-project-5001/assets/24834264/30237ee8-6772-4290-85ad-a843001603c7)

  ![](https://cdn.discordapp.com/attachments/778320935488716851/1180713497219305472/image.png)

* When testing interaction with the website I would cycle through the same few interactions. Checking and unchecking several of the already existing tasks. Creating one new task with a date and another with no date. Editing just the name of a task, just the date of task and then editing both. And finally, I would delete tasks.

## Missing Features / What's Next

* Currently editing a task redirects you to a different page where you can only see the task you're editing. With more time I would have liked to allow tasks to be edited on the homepage.
  
  * Perhaps by re-rendering the page with text and date input elements in place of the text elements previously displaying the task's name and date. And then replacing the edit/delete buttons with a save button.

* Now that I have the basic working I'd like to add multiple ways to sort the tasks on the list by name, date, and completion. I would also love to add the ability to nest tasks.
  
  * For sorting I could just keep the instance of `TaskCollection` the same and just re-sort the CSV file. Or it might be better to switch to an array since the dictionary might make nesting tasks cumbersome as well. I could extend `TaskCollection` to make a class for groups of nested tasks that indicates which task is the main header task and which ones are the subtasks.

## Final Reflection

* In this course I've started to learn how the memory stack works, which has given me a better understanding of mutability and scope than I had before. This also improved my understanding of objects in Python. Another key thing I've learned is how to write more comprehensive tests. I've gotten better at catching edge cases now, and learning how to use doctest and unittest has made it much easier/faster as well. Particularly through this project, I've gotten better at reading and understanding documentation. Teaching myself how to use Flask and HTML from scratch was difficult at first but it was a great learning experience and has made me feel less intimidated about using new languages or libraries in the future. Going forward in my learning I would like to do practice problems more frequently throughout the week and dig deeper into how programming languages work behind the scenes.
