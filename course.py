from assessment import Assessment
from datetime import date

class Course:


    def __init__(self, name: str):
        self.name = name    # intilizes a course name
        self.assessments = []   # creates an empty list of assessments

    # Changes the name of a course
    def update(self, name = None):
        if name is not None:
            self.name = name

    # Creates and adds a new lab/test to an exisiting list of assessments
    def add_assessment(self, name: str, kind: str, due_date: date, weight: float):
        new_assessment = Assessment(name, kind, due_date, weight)
        self.assessments.append(new_assessment)

    # Searches and removes a lab/test from the course
    def remove_assessment(self, name: str):
        found = False
        for assessment in self.assessments:
            if assessment.name == name:
                found = True
                self.assessments.remove(assessment)
                print(f"{name} was removed\n")
                break
        if not found:
            print(f"{name} was not found\n")
    
    # Calculates the grade earned for the course
    # Returns 0 if no assessments are completed
    def course_grade(self):
        points_earned = 0
        weight_completed = 0
        for assessment in self.assessments:

            if assessment.grade_earned is not None:
                points_earned += assessment.grade_earned * (assessment.weight / 100)
                weight_completed += assessment.weight

        if weight_completed == 0:
            return 0
        
        return points_earned / weight_completed