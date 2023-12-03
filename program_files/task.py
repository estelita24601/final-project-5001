from datetime import date


class Task:
    def __init__(self, name, is_complete=False, due_date: str = None) -> None:
        """
        Args: name (str): short description of the task
        is_complete (bool, optional): Whether the task is complete or not. Defaults to False.
        date (str, optional): string in valid ISO format, defaults to None

        """
        self.name: str = name
        self.is_complete = is_complete

        if due_date is None or due_date == "None":
            self.date = None
        else:
            self.date = date.fromisoformat(due_date)

        self.unique_id = id(self)

    def __str__(self):
        return f"{self.unique_id:10} | {self.name:10} | {self.date:10} | {self.is_complete}"

    def get_id(self):
        return self.unique_id

    def get_name(self):
        """returns the name of the task

        Returns:
            self.name (str)
        """
        return self.name

    def get_completion_status(self) -> bool:
        """returns True if the task is complete and False if it is incomplete

        Returns:
            self.is_complete(bool)
        """
        return self.is_complete

    def get_date(self):
        """if the task has a due date returns a date object for the due date
        otherwise returns None
        """
        return self.date

    def change_name(self, new_name: str) -> None:
        """changes the name of the task

        Args:
            new_name (str): the new name for the task

        """
        if not isinstance(new_name, str):
            raise TypeError(self, "new name for the task must be a string")
        self.name = new_name

    # FIXME: update docstring and corresponding test
    def change_date(self, due_date: str):
        """change the date task is due

        Args:
            #FIXME
        """
        self.date = date.fromisoformat(due_date)

    def remove_date(self) -> None:
        self.date = None

    def change_completion_status(self, new_status: bool) -> None:
        """updates whether the task is complete or not

        Args:
            new_status (bool): True for completed tasks and False for incomplete tasks
        """
        if not isinstance(new_status, bool):
            raise TypeError(
                self, "completion status must be boolean True or False")
        else:
            self.is_complete = new_status

    def mark_complete(self):
        self.is_complete = True

    def mark_incomplete(self):
        self.is_complete = False

    def to_csv(self) -> str:
        return ",".join((self.unique_id, self.name, self.is_complete, self.date))


class TaskList:
    def __init__(self, file_name: str):
        task_list = []

        with open(file_name, "r") as task_file:
            for line in task_file:
                current_task = self.task_from_csv(line)
                task_list.append(current_task)

        self.task_dictionary = self.create_obj_dict(task_list)

    def task_from_csv(self, csv_line: str) -> Task:
        # csv_line = "name of task, False, None"
        csv_list = csv_line.split(",")
        name = csv_list[0].strip()
        is_complete = bool(csv_list[1])
        due_date = csv_list[2].strip()
        if due_date == "None":
            due_date = None
        return Task(name, is_complete, due_date)

    def update_csv(self, file_name: str):
        with open(file_name, "w") as csv_file:
            for line in self.create_csv_list():
                csv_file.write(line)
                csv_file.write("\n")

    def create_csv_list(self) -> list:
        return [task.to_csv() for task in self.task_dictionary.values()]

    def create_obj_dict(self, task_list) -> dict:
        task_dict = {}

        for task in task_list:
            task_dict[task.get_id()] = task

        return task_dict

    def remove_task(self, task_id):
        self.task_dictionary.pop(task_id)

    def add_task(self, task_obj):
        self.task_dictionary[task_obj.get_id()] = task_obj

    def get_task(self, task_id):
        return self.task_dictionary[task_id]
