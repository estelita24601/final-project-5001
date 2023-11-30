from datetime import date


class Task:
    def __init__(self, name, is_complete=False, due_date: tuple[int, int, int] = (0, 0, 0)) -> None:
        """
        Args:
            name (str): short description of the task
            is_complete (bool, optional): Whether the task is complete or not. Defaults to False.
            date (tuple, optional): integers for year, month and date in the correct format for a date object from the datetime module. No leading zeroes and numbers in range of the gregorian calendar.

        """
        self.name: str = name
        self.is_complete = is_complete

        # if we don't have the default tuple then try to make a date object
        if due_date != (0, 0, 0):
            year = int(due_date[0])
            month = int(due_date[1])
            day = int(due_date[2])
            self.date = date(year, month, day)
        else:
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
    # possible errors: not an integer, leading 0, numbers out of range, didn't provide all three
    def change_date(self, year, month, day):
        """change the date task is due

        Args:
            year (int): year as an integer with 4 digits
            month (int): month as an integer with no leading 0
            day (int): day as an integer with no leading 0
        """
        try:
            self.date = date(year, month, day)
        except TypeError as e:
            print("unable to change date due to", e)
        except ValueError as e:
            print("unable to change date due to", e)

    #FIXME: add docstring and create test
    def remove_date(self) -> None:
        self.date = None

    def change_completion_status(self, new_status: bool) -> None:
        """updates whether the task is complete or not

        Args:
            new_status (bool): True for completed tasks and False for incompleted tasks
        """
        if not isinstance(new_status, bool):
            raise TypeError(
                self, "completion status must be boolean True or False")
        else:
            self.is_complete = new_status

#FIXME: add docstring and create test
def create_task_list(file_name: str) -> list[Task]:
    task_list = []

    with open(file_name, "r") as task_file:
        for line in task_file:
            current_task = task_from_csv(line)
            task_list.append(current_task)
    
    return task_list

#FIXME: add docstring and create test
def task_from_csv(csv_line:str):
    # csv_line = "name of task, False, None"
    csv_line = csv_line.split(",")
    name = csv_line[0]
    is_complete = csv_line[1]
    date = date_conversion(csv_line[2])
    return Task(name, is_complete, date)

#FIXME: add docstring and create test
def date_conversion(date_string):
    if date_string == "None":
        return (0, 0, 0)
    #FIXME: date_string will be in "YYYY-MM-DD" format either change task.date attribute or manipulate string into tuple of ints