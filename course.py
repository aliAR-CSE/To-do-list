from assessment import Assessment
from datetime import date

class Course:


    def __init__(self, name: str):

        self.name = name    # intilizes a course name
        self.assessments = []   # creates an empty list of assessments

    """Changes the name of a course"""
    def update(self, name = None):

        if name is not None:
            self.name = name

    """Creates and adds a new lab/test to an exisiting list of assessments"""
    def add_assessment(self, name: str, kind: str, due_date: date, weight: float):
        new_assessment = Assessment(name, kind, due_date, weight)
        self.assessments.append(new_assessment)

    """Searches and removes a lab/test from the course"""
    def remove_assessment(self, name: str) -> bool:

        found = False

        for assessment in self.assessments:
            if assessment.name == name:
                self.assessments.remove(assessment)
                found = True
                break
        return found
    
    """Calculates the grade earned for the course
    Returns 0 if no assessments are completed"""
    def course_grade(self) -> float:

        points_earned = 0
        weight_completed = 0

        for assessment in self.assessments:

            if assessment.grade_earned is not None:
                points_earned += assessment.grade_earned * (assessment.weight / 100)
                weight_completed += assessment.weight

        if weight_completed == 0:
            return 0
        
        return points_earned / weight_completed
    
    """Counts the amount of completed and uncompleted assessments
    and returns the completion of the course as a %"""
    def completion(self) -> float:

        numb_completed = 0
        numb_uncompleted = 0
        for assessment in self.assessments:

            if assessment.is_completed:
                numb_completed += 1
            else:
                numb_uncompleted += 1
        if numb_completed + numb_uncompleted == 0:
            return 0
        return  100 * numb_completed / (numb_completed + numb_uncompleted)