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

    def complete(self, earned_grade: float):
        self.grade_earned = earned_grade
        self.is_completed = True

    def is_overdue(self):
        if self.is_completed is True:
            return False
        return date.today() > self.due_date

class Course:
