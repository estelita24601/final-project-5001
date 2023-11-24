from datetime import date


class Task:
    def __init__(self, name, is_complete=False, year=None, month=None, day=None) -> None:
        """
        Args:
            name (str): short description of the task
            is_complete (bool, optional): Whether the task is complete or not. Defaults to False.

            # if one or more of the following are not provided task will not have a date
            year (int, optional): 4-digit number for the year. Defaults to None.
            month (int, optional): 1 or 2-digit number for the month. Defaults to None.
            day (int, optional): 1 or 2-digit number for the day. Defaults to None.
        """
        self.name: str = name
        self.is_complete = is_complete

        if year and month and day:  # make sure we have everything needed to create a date object
            self.date = date(year, month, day)
        else:   # if all three values weren't provided our task doesn't have a date
            self.date = None

    def __str__(self):
        output = f"{self.name:10} | {self.date:10} | {self.is_complete}"

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

    # QUESTION: Is it okay to return none when there is no date?
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

    # QUESTION: should I let the date object handle errors for me?
    def change_date(self, year, month, day):
        """change the date task is due

        Args:
            year (int): year as an integer with 4 digits
            month (int): month as an integer with no leading 0
            day (int): day as an integer with no leading 0
        """
        try:
            self.date = date(year, month, day)
        except e as TypeError:
            print(e)

    def change_completion_status(self, new_status: bool) -> None:
        """updates whether the task is complete or not

        Args:
            new_status (bool): True for completed tasks and False for incompleted tasks
        """
        if not isinstance(new_status, bool):
            raise TypeError(self, "completion status must be boolean True or False")
        else:
            self.is_complete = new_status
