from datetime import date

class Assessment:
    def __init__(self, name: str, kind: str, due_date: date, weight: float):
        self.name = name
        self.kind = kind
        self.due_date = due_date
        self.weight = weight
        self.grade_earned = None
        self.is_completed = False

    def update(self, name = None, due_date = None, weight = None, grade = None):
        if name is not None:
            self.name = name
        if due_date is not None:
            self.due_date = due_date
        if weight is not None:
            self.weight = weight
        if grade is not None:
            self.grade_earned = grade

    def complete(self):
        self.is_completed = True

    def is_overdue(self):
        if self.is_completed is True:
            return False
        return date.today() > self.due_date # compares today's date as YYYY-MM-DD to a set due date
    
    def to_dict(self):
        new_dict = {"name" : self.name, 
                    "kind" : self.kind, 
                    "due_date" : str(self.due_date), 
                    "weight" : self.weight, 
                    "grade_earned" : self.grade_earned, 
                    "is_completed" : self.is_completed}
        return new_dict