# Final Project Goals

## Basic Goals (must do)

* [x] Display a list of tasks on the website
* [x] check boxes that mark tasks as complete when you click once. will undo if clicked again
* [x] field for the user to input new tasks to the list
* [x] option to delete individual tasks
* [x] ability to edit/update task and all of its parameters

## Further Goals (ideally would do)

* [ ] button to mass delete all completed tasks

* [ ] add optional labels/tags for tasks

* [x] add optional due date parameter for tasks
  
  **Sorting Tasks**
  
  * [ ] arrange task list so completed items are on the bottom
  * [ ] alphabetically by task name
  * [ ] by due date
  * [ ] by tag
  
  **Advanced Sorting**
  
  * [ ] whenever sorting by date or tag also sort alphabetically
  * [ ] whenever sorting by date also group by tag in alphabetical order
  * [ ] whenever sorting by tag also sort by order of date in alphabetical order

* [x] save status of website to file that can be reloaded later (current list of tasks, status of said tasks etc)

* [ ] login or custom url for different users and their associated file

## Stretch Goals

* [ ] weekly view and daily view

* [ ] Option to only show tasks with a certain tag (either with filter button or separate tab or something else)

* [ ] field for additional task details

* [ ] select multiple tasks to give them all the same tag or remove same tag

* [ ] select multiple tasks to give them all the same due date

* [ ] replace save file with a data base (<https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/>)

* [ ] Option to only show tasks with a certain tag (either with filter button or separate tab or something else)

* [ ] Option to only show tasks with multiple specific tags (ex only show tasks labelled financial and urgent)

* [ ] field for additional task details

* [ ] different color themes / color coding?

## Long Term / More Difficult

* [ ] undo button (up to 5 changes to start?)
* [ ] subtasks / nested tasks
* [ ] Option to only show tasks with multiple specific tags (ex only show tasks labeled financial and urgent)
* [ ] duplicate task button (like google calendar creates duplicate but lets you edit before saving)
* [ ] Custom tags for tasks
* [ ] mobile friendly website version

# Methods to use on a list of Tasks

* **alphabetic_sort**(list of Task objects) -> list of Task objects

* **date_sort**(list of Task objects) -> list of Task objects
  
  * first compare year
  * then compare month within the same year
  * then compare day within the same month

* **tag_sort**(list of Task objects) -> list of Task objects
  
  * maybe use global variable that is a list of the tags in alphabetic order?
  * advanced version of this function will call **date_sort()** on each separate tag, and then call **alphabetic _sort()** on each separate date

* **completion_sort**(list of Task objects) -> ??????
  
  * either put the completed items at the end OR return two lists, one for complete items and another for incomplete
  * will depend on how other files handle Tasks

* **sub_list_merger**(list of lists or a tuple of lists) -> one list of Task objects
  
  * Ex. one sublist for tasks in November, and another sublist for tasks in December. Return one combined list made of the two lists in correct order (november list first then december list)
  * make it general enough so it works on more than just months/days

* sub_list_creator() ???
  
  * helper function that splits a list into sublists, one sublist for each value of the given attribute. ex one list for all items with date = [11, 3, 2023], and another for all items with date = [11, 5, 2023]
  * but somehow general enough to be able to use in multiple sorting functions

# Brainstorming

advanced sorting:

* first sort by main feature
* as doing this put tasks with the same value for the main feature in their own mini lists
* then run the other sort functions on those mini-lists
* then put it all back together somehow
* helper function(s) to make mini lists and to merge them back into one list

Overall sorting:

* create new list with items in new order to replace old list or is that too expensive?
