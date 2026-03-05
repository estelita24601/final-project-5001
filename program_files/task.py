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