# 

# Final Project Planning Document

## Basic Goals (must do)

- [ ] Create a website using Flask

- [ ] Display list of tasks on the website

- [ ] create check boxes for each item

- [ ] when you click on a checkbox it strikes through the task and grays out

- [ ] field for user to input new tasks to the list

- [ ] option to delete individual tasks

- [ ] ability to edit/update task and all it's parameters

## Further Goals (ideally would do)

- [ ] button to mass delete all completed tasks

- [ ] option to add and edit tags to tasks in order to categorize them

- [ ] editable due date parameter for tasks

- [ ] color code based on days until due date
  
  **Sorting Tasks**
  
  - [ ] automatically arrange task list so completed items are on the bottom
  
  - [ ] alphabetically by task name
  
  - [ ] by due date
  
  - [ ] by tag
  
  **Advanced Sorting**
  
  - [ ] whenever sorting by date or tag also sort alphabetically
  
  - [ ] whenever sorting by date also group by tag in alphabetical order
  
  - [ ] whenever sorting by tag also sort by order of date in alphabetical order

- [ ] save status of website to file that can be reloaded later (current list of tasks, status of said tasks etc)

- [ ] login or custom url for different users and their associated file

## Stretch Goals (optional/for the future)

- [ ] undo button (up to 5 changes to start?)

- [ ] select multiple tasks to give them all the same tag or remove same tag

- [ ] select multiple tasks to give them all the same due date

- [ ] Option to only show tasks with a certain tag (either with filter button or separate tab or something else)

- [ ] Option to only show tasks with multiple specific tags (ex only show tasks labelled financial and urgent)

- [ ] field for additional task details

- [ ] subtasks / nested tasks

- [ ] duplicate task button (like google calendar creates duplicate but lets you edit before saving)

- [ ] different color themes

- [ ] Custom tags for tasks

- [ ] mobile friendly website version

## Ideas/Brainstorming

* class Task, each task is an instance of this class
  
  * methods to add name, date etc
  
  * tag parameter as a list? if no tags list is empty, otherwise allows multiple tags in the list
  
  * boolean True/False for if task is complete or if task is crossed out?

* put all task objects in a list and have functions to sort the list
  
  * alphabetic_sort()
  
  * date_sort()
  
  * tag_sort()
  
  * completion_sort()

* advanced sorting:
  
  * first sort by main feature
  * as doing this put tasks with the same value for the main feature in their own mini lists
  * then run the other sort functions on those mini lists
  * then put it all back together somehow

* Overall sorting:
  
  * create new list with items in new order to replace old list or is that too expensive?

* possible idea: Make sure File 1-3 work first before doing File 4
  
  * **FILE 1:** create back end first and just have it process/output tasks in their raw form
  
  * **FILE 2:** intermediary between File 1 and File 3 and 4. Takes user interaction information from 3/4 and uses that to decide what functions to call from File 1. Then takes output from File 1 and gives it to 3/4 so they can display it to user.
  
  * **FILE 3:** text interface. Print to console and user types to interact
  
  * **FILE 4:** file for the website

* User errors to account for:
  
  * empty task name
  
  * incorrect date format
  
  * warn them with GUI and don't let them click add/save until input is acceptable?
