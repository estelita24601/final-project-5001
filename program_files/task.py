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

        if due_date in (None, "None", ""):
            self.date = None
        else:
            self.date = date.fromisoformat(due_date)

        self.unique_id = id(self)

    def get_id(self):
        return self.unique_id

    def get_name(self):
        """returns the name of the task

        Returns:
            self.name (str)
        """
        return self.name

    def get_completion_status(self) -> bool:
        """returns True if the task is complete and False if it is incomplete"""
        return self.is_complete

    def get_date(self):
        """if the task has a due date returns a date object for the due date
        otherwise returns None
        """
        return self.date

    def get_display_date(self) -> str:
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

    def change_date(self, due_date: str):
        """UPDATE ME!!!!!! change the date task is due
        wants the input in YYY-MM-DD form"""
        self.date = date.fromisoformat(due_date)

    def remove_date(self) -> None:
        self.date = None

    def change_completion(self) -> None:
        self.is_complete = not self.is_complete

    def to_csv(self) -> str:
        unique_id = str(self.unique_id)
        is_complete = str(self.is_complete)
        try:
            due_date = self.date.isoformat()
        except AttributeError:
            due_date = "None"
        return ",".join((unique_id, self.name, is_complete, due_date))

    def change_id(self, new_id: int) -> None:
        # for testing purposes only
        self.unique_id = new_id


class TaskCollection:
    def __init__(self, file_name: str):
        task_list = []
        try:
            with open(file_name, "r") as task_file:
                for line in task_file:
                    current_task = self.task_from_csv(line)
                    task_list.append(current_task)
        except FileNotFoundError:
            new_file = open(file_name, "x")
            new_file.close()

        self.task_dictionary = self.create_obj_dict(task_list)
        self.update_csv(file_name)  # put unique id for each object into csv

    def task_from_csv(self, csv_line: str) -> Task:
        # csv_line = "name of task, False, None"
        csv_list = csv_line.split(",")
        name = csv_list[1].strip()

        is_complete = csv_list[2]
        if is_complete == "False":
            is_complete = False
        else:
            is_complete = True

        due_date = csv_list[3].strip()
        if due_date == "None":
            due_date = None

        return Task(name, is_complete, due_date)

    def update_csv(self, file_name: str):
        print("-------UPDATING CSV FILE")  # TESTING
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

    def get_task_dictionary(self) -> dict:
        return self.task_dictionary

    def delete_task(self, task_id) -> None:
        self.task_dictionary.pop(task_id)

    def add_task(self, task_obj) -> None:
        self.task_dictionary[task_obj.get_id()] = task_obj

    def get_task(self, task_id) -> Task:
        return self.task_dictionary[task_id]
