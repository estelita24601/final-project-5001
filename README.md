# Python To-Do List Website

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
