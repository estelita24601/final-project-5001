# Issues/Questions Need to Deal With

* is Figma to figure out GUI necessary or not? maybe just draw on paper

* is it worth it to also make a console interface before making the website?
    * Is there a way to create a library of global variables for all 4 files? could use this to standardize communication with File 2
      - ex if the user clicks a button then the website sends the same command to the backend as the console interface would send if the user typed the correct thing, then won't need to change backend when switching from text interface to GUI
  
# class Task

#### Attributes:

* **name**
  * string "Problem Set 8 - question 1a"

* **completion_status**
  * Boolean True or False

* **date (optional)**
  * list of attributes [self.month, self.day, self.year]
  * *month(required for date)*
    * int 4
  * *day (required for date)*
    * int 25
  * *year (required for date)*
    * int 2023

* **tag (optional)**
  * string "School"

#### Methods:
* **get_attribute**
  * for name, date, tag and completion_status

* **change_attribute**
  * for name, date, tag and completion_status
  * <u>will only accept valid format, otherwise raise error</u>

* **calculate_days**
  * return int for # days until deadline
  * can return negative numbers

# Methods to use on a list of Tasks

- **alphabetic_sort**(list of Task objects) -> list of Task objects

- **date_sort**(list of Task objects) -> list of Task objects
  - first compare year
  - then compare month within the same year
  - then compare day within the same month

- **tag_sort**(list of Task objects) -> list of Task objects
  - maybe use global variable that is a list of the tags in alphabetic order?
  - advanced version of this function will call **date_sort()** on each separate tag, and then call **alphabetic _sort()** on each separate date

- **completion_sort**(list of Task objects) -> ??????
  - either put the completed items at the end OR return two lists, one for complete items and another for incomplete
  - will depend on how other files handle Tasks

- **sub_list_merger**(list of lists or a tuple of lists) -> one list of Task objects
  - Ex. one sublist for tasks in November, and another sublist for tasks in December. Return one combined list made of the two lists in correct order (november list first then december list)
  - make it general enough so it works on more than just months/days

- sub_list_creator() ???
  - helper function that splits a list into sublists, one sublist for each value of the given attribute. ex one list for all items with date = [11, 3, 2023], and another for all items with date = [11, 5, 2023]
  - but somehow general enough to be able to use in multiple sorting functions


# Brainstorming

possible idea: Make sure File 1-3 work first before doing File 4?
* **FILE 1:** my custom class(es) + methods that will process and output data

* **FILE 2:** intermediary between File 1 and File 3 and 4. Takes user interaction information from 3/4 and uses that to decide what functions to call from File 1. Then takes output from File 1 and gives it to 3/4 so they can display it to user.

* **FILE 3:** text interface. Print to console and user types to interact

* **FILE 4:** website with GUI

Dealing with User Errors
  * invalid date format
  * empty task name, or maybe task name with no letters
  * non-existent tag/label
  * maybe handle by displaying warning on GUI and not allowing them to hit submit/save until input is valid?

advanced sorting:
* first sort by main feature
* as doing this put tasks with the same value for the main feature in their own mini lists
* then run the other sort functions on those mini-lists
* then put it all back together somehow
* helper function(s) to make mini lists and to merge them back into one list

Overall sorting:
* create new list with items in new order to replace old list or is that too expensive?
