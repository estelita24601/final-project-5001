from datetime import date


class Task:
    """Class representing a task on a checklist"""

    def __init__(self, name, is_complete=False, due_date: str = None) -> None:
        """
        Args: name (str): short description of the task
        is_complete (bool, optional): Whether the task is complete or not. Defaults to False.
        date (str, optional): string in valid ISO format ("YYYY-MM-DD"), defaults to None
        """
        self.name: str = name
        self.is_complete = is_complete

        if due_date in (None, "None", ""):
            self.date = None
        else:
            self.date = date.fromisoformat(due_date)

        self.unique_id = id(self)

    def get_id(self) -> int:
        """
        Returns:
            self.unique_id (int): integer unique to this instance of Task
        """
        return self.unique_id

    def get_name(self) -> str:
        """
        Returns:
            self.name (str): name of the task
        """
        return self.name

    def get_completion_status(self) -> bool:
        """
        Returns:
            self.is_complete (bool): True for complete tasks, False for incomplete tasks
        """
        return self.is_complete

    def get_date(self):
        """
        Returns:
            self.date: either a date object form datetime module or None
        """
        return self.date

    def get_display_date(self) -> str:
        """
        Returns:
            str: a string representation of self.date formatted to be displayed on the website
        """
        if self.date is not None:
            return self.date.strftime("%m/%d/%y")
        else:
            return ""

    def change_name(self, new_name: str) -> None:
        """changes the name of the task

        Args:
            new_name (str): the new name for the task

        """
        if not isinstance(new_name, str):
            raise TypeError(self, "new name for the task must be a string")
        self.name = new_name

    def change_date(self, due_date: str) -> None:
        """
        Args:
            due_date (str): new date for Task object in ISO format ("YYY-MM-DD")
        """
        if due_date in ("None",None,""):
            self.remove_date()
        else:
            self.date = date.fromisoformat(due_date)


    def remove_date(self) -> None:
        """reset self.date to be None"""
        self.date = None

    def change_completion(self) -> None:
        """Change self.is_complete to opposite bool value. Mimics marking a checkbox"""
        self.is_complete = not self.is_complete

    def to_csv(self) -> str:
        """Creates a string in csv format that represents this instance of Task.
        Helper for update_csv() from TaskCollection class

        Example:
            "unique_id_number, task_name, is_complete, due_date"
            "24601, Task #1, False, 2024-01-01"
        """
        unique_id = str(self.unique_id)
        is_complete = str(self.is_complete)

        try:  # try to turn self.date into a string
            due_date = self.date.isoformat()
        except (
            AttributeError
        ):  # if that doesn't work then create default string of 'None'
            due_date = "None"

        return ",".join((unique_id, self.name, is_complete, due_date))

    # for testing purposes only
    def change_id(self, new_id: int) -> None:
        """Changes value of self.unique_id so you can know what output to expect from get_id().
        Only used for testing purposes
        """
        self.unique_id = new_id


class TaskCollection:
    """Class representing multiple Tasks that are on the same checklist"""

    def __init__(self, save_file_name: str) -> None:
        task_list = []
        # read from file to create Tasks objects that are inside of this instance of TaskCollection
        try:
            with open(save_file_name, "r") as task_file:
                for line in task_file:
                    current_task = self.task_from_csv(line)
                    task_list.append(current_task)
        except FileNotFoundError:
            new_file = open(save_file_name, "x")
            new_file.close()

        self.task_dictionary = self.create_obj_dict(task_list)
        # update the save file so the unique id numbers of the objects are updated
        self.update_csv(save_file_name)

    def task_from_csv(self, csv_line: str) -> Task:
        """given one line from a csv file, create a Task object with the proper attributes

        Args:
            csv_line (str): string in csv format

        Returns:
            Task: instance of the Task class
        """
        csv_list = csv_line.split(",")
        name = csv_list[1].strip()

        is_complete = csv_list[2]
        # converting the str into a bool
        if is_complete == "False":
            is_complete = False
        else:
            is_complete = True

        due_date = csv_list[3].strip()
        if due_date == "None":
            due_date = None

        return Task(name, is_complete, due_date)

    def update_csv(self, file_name: str) -> None:
        """given the name of a csv file, overwrite it with the current Tasks inside of this instance of TaskCollection"""

        with open(file_name, "w") as csv_file:
            # write csv line for each Task object
            for line in self.create_csv_list():
                csv_file.write(line)
                csv_file.write("\n")

    # helper for update_csv()
    def create_csv_list(self) -> list:
        """create a list of strings for a csv file from all the Tasks inside of this TaskCollection

        Returns:
            list[str]: list of strings where every string will be one line of a csv file
        """
        # for every task in the dictionary, turn it into a string for a csv file
        return [task.to_csv() for task in self.task_dictionary.values()]

    # helper for __init__()
    def create_obj_dict(self, task_list: list[Task]) -> dict:
        """turn a list of Task objects into a dictionary to facilitate retrieval.

        Args:
            task_list (list[Task]): a list of task objects

        Returns:
            task_dict: task id number (int) for the keys and instance of Task class for values
        """
        task_dict = {}

        for task in task_list:
            task_dict[task.get_id()] = task

        return task_dict

    def get_task_dictionary(self) -> dict:
        """
        Returns:
            self.task_dictionary: task id number (int) for the keys and instance of Task class for values
        """
        return self.task_dictionary

    def delete_task(self, task_id: int) -> None:
        """removes Task that is associated with task_id (int)"""
        self.task_dictionary.pop(task_id)

    def add_task(self, task_obj: Task) -> None:
        """updates this instance of TaskCollection to have new Task object inside of it

        Args:
            task_obj (Task): the task you want to add
        """
        self.task_dictionary[task_obj.get_id()] = task_obj

    def get_task(self, task_id: int) -> Task:
        """finds and returns the Task object associated with task_id (int)"""
        return self.task_dictionary[task_id]
