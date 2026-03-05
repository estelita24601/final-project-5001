from task import Task


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
