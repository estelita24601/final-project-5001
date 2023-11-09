from datetime import date

#FIXME: initialization of self.date needs more thought, what args do I want from user here?
# asking for a date object might be too cumbersome
class Task:
    def __init__(self, name, is_complete=False, date=None) -> None:
        self.name: str = name
        self.is_complete = is_complete
        self.date = date

# QUESTION: best practices for repr vs str??
    def __repr__(self):
        return f"Task('{self.name}', {self.is_complete}, {self.date})"

    def get_name(self):
        return self.name

    def change_name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError(self, "requires new name to be a string")
        self.name = new_name

    def get_completion_status(self) -> bool:
        return self.is_complete

    def change_completion_status(self) -> None:
        self.is_complete = not self.is_complete

    def get_date(self):
        return self.date
        # FIXME: maybe return false if there is no date? or just return none?

    def change_date(self, year, month, day):
        new_date = date(year, month, day)
    
        if new_date >= date.today():
            self.date = new_date
        else:
            raise ValueError("due date cannot be before today's date")