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
