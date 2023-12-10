# Final Project Report

* Student Name: Estelita Chen
* Github Username: estelita24601
* Semester: Fall 2023
* Course: CS 5001

## Description

This is a To-Do List website created using Flask and Python. You can create new tasks and edit or delete existing ones. This project was inspired by the spreadsheet I use to keep track of my schoolwork.

## Key Features

In addition to creating, editing and deleting tasks, the website also saves whatever changes you make so they are still there if you leave and come back later. 

## Guide

<u>To create a new task:</u>

* enter name of the task in the textbox

* if there is a due date input that in the date field either by typing or using the pop up calendar

* press the "create new task" button

<u>To delete a task:</u>

* click the "delete" button on the same row as the task you want to delete

<u>To mark a task as complete or incomplete:</u>

* click the checkbox to the left of the task (a blue checkmark indicates the task is complete, an empty white checkbox indicates the task is not complete)

<u>To edit a task:</u>

* click the "edit" button to the right of the task you want to edit

* you will be brought to a new page where you can enter a name and optional date in the same manner you would when creating a new task

* click the "save changes" button to be brought finish editing the task and be brought back to the main view with all tasks
  
  ## Installation Instructions

* download flask: ```pip install flask```

* To launch the website navigate to the ```program_files``` directory on commandline and type the following: `python -m flask --app website.py run`

* Click on the link (Ctrl+Click) to open the website on your browser.

* Type Ctrl+C to shut down the server

## Code Review

##### website.py

```python
@app.route("/", methods=["POST", "GET"])
def home():
```

This function is for the homepage of the website. The decorator specifies the url and what http requests will be handled by it. 

The post request is used to get information from the website whenever a form is submitted. 

* if a post request has been detected the home() function will take that information and put it into dictionary form inside of the variable `form_data`
  
  * if the user clicked delete `form_data = {id_number: "delete"}``
  
  * if the user clicked edit `form_data = {id_number: "edit"}`
  
  * if the user clicked a checkbox `form_data = {id_number: "True"}` or `{id_number: "checkbox"}`
    
    * the checkbox input in html will send back "True" when it's checked but when unchecked it sends nothing so I created a hidden element that will send back "checkbox" so I can know when tasks are unchecked as well
  
  * if the user clicked create new task `form_data = {"new_name": "what the user typed", "new_date": "YYYY-MM-DD"}`

* because flask will resend a duplicate post request when the page is refreshed, the program will compare the request to `request_history.json` to prevent the bugs that would occur otherwise. 

* after confirming this post request isn't the result of a page refresh the program will update ```request_history.json``` and then use  ```process_post_request()``` to execute whatever is needed to complete the user's request.

* `process_post_request()` can handle deleting tasks, changing checkboxes and creating new tasks with helper functions and built in class methods from the backend. For editing tasks `process_post_request` will return "edit" and the `home()` function will then redirect to a different webpage if detected.

```python
if user_action == "edit":
                return redirect(url_for("task_editor", post_dict=form_data))

@app.route("/edit/<post_dict>", methods=["POST", "GET"])
def task_editor(post_dict):
```

* The webpage for editing is created by `task_editor()` which has a custom url that allows me to pass on information from `home()`

* `url_for()` creates a url that follows the necessary format for `task_editor` and inserts the variable `form_data` into the url as a string. `task_editor` then takes that string and puts it into the variable `post_dict`
  
  * it would have perhaps been better to use JSON format 

* `post_dict` is processed to get the task the user wants to edit display it in textbox and date input elements. 

* `task_editor()` then waits to receive another post request from the "save changes" button to save the changes to the CSV and redirect back to the homepage

* after any post requests have been dealt with `home()` and `task_editor()` get the html template they're associated with and return the template to the front end in a get request. `.render(variable_name = my_info)` is used on the template to pass along what information the webpage needs to display.

##### HTML Templates + Jinja2

home_page.html

* template for the home page of the website where the user will spend most of their time. Lists out all the tasks and has a GUI to interact with tasks in the list
  
  

```jinja2
{% for task_id in task_data %}
        <!-- use the dictionary entry to get info on each task object-->
        {% set task_obj = task_data[task_id] %}
        {% set name_value = task_obj.get_name() %}
        {% set check_status = task_obj.get_completion_status() %}
        {% set date = task_obj.get_display_date() %}
```

* When this template was rendered the variable `task_data` received a dictionary of task objects. Using jinja I can loop through every task in the dictionary and extract the information I want to display



```html
<form action="" method="post" name="new task">
    <input type="text" name="new_name" value="enter name of task here" />
    <input type="date" name="new_date" />
    <input type="submit" value="create new task" />
</form>
```

- This creates the text input field, the date input field and the "create new task button" and puts them together in the same form so when the submit button is pressed the rest of the information is also sent

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

edit_task.html

* When a user wants to edit a task they get redirected to a page that renders this html file.

* Has a text input field, date input field and a button that will save the information and return the user to the home page.

##### task.py

* 



### Major Challenges

Key aspects could include pieces that you struggled on and/or pieces that you are proud of and want to show off.

* The first major hurdle was figuring out what a post request was and how to handle them. At first I could only send a post request if the user hit a submit button after every change, and it would send information about every single input element on the page which was harder to process. When I started to better understand how `<input>` and `<form>` worked I was able to set up my html page to send smaller and easier to understand post requests whenever the user interacted with the website. 

* The hardest bug to fix was the website crashing or malfunctioning whenever the user refreshed the page. I realized the website was sending the previous post request a second time whenever refreshing, and it seemed the conventional fix was to use javascript to override flask's default behavior. Then I realized instead of preventing duplicate requests from being made I could have my program just ignore those duplicate requests. I used a json file to save the most recent post request so it could be compared to the next post request sent. 



### Example Runs

Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

## Testing

How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_

* In the repository there's a folder named `testing` that contains my tests.

* I extended `unittest` and wrote tests for all the methods in `Task`

* I also wrote a test class for `TaskCollection` however some methods couldn't be checked by `.assert` as easily so I had those methods update a csv file so I could manually see if the output matched what I expected.

* Testing flask was harder but I ended up using a lot of print statements that would show up on the command line and were very helpful for debugging.

* To test my html input elements and post requests I created a temporary webpage that all forms would redirect to that displayed the post request. This also helped me figure out the best format for the data I sent in my post requests. However once I started putting in more buttons I switched over to using more print statements.
  
  ![](https://cdn.discordapp.com/attachments/778320935488716851/1180713497219305472/image.png)
  
  

## Missing Features / What's Next

Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

## Final Reflection

Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.
