from assessment import Assessment
from datetime import date

class Course:


    def __init__(self, name: str):
        self.name = name
        self.assessments = []

    def update(self, name = None):
        if name is not None:
            self.name = name

    def add_assessment(self, name: str, kind: str, due_date: date, weight: float):
        new_assessment = Assessment(name, kind, due_date, weight)
        self.assessments.append(new_assessment)