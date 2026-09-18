from assessment import Assessment
from datetime import date

class Course:


    def __init__(self, name: str):

        self.name = name    # intilizes a course name
        self.assessments = []   # creates an empty list of assessments

    def update(self, name = None):
        """Changes the name of a course"""
        if name is not None:
            self.name = name

    def add_assessment(self, name: str, kind: str, due_date: date, weight: float):
        """Creates and adds a new lab/test to 
        an exisiting list of assessments"""
        new_assessment = Assessment(name, kind, due_date, weight)
        self.assessments.append(new_assessment)

    def remove_assessment(self, name: str) -> bool:
        """Searches and removes a lab/test from the course"""
        found = False

        for assessment in self.assessments:
            if assessment.name == name:
                self.assessments.remove(assessment)
                found = True
                break
        return found
    
    def get_grade(self) -> float:
        """Calculates the grade earned for the course
        Returns 0 if no assessments are completed"""
        points_earned = 0
        weight_completed = 0

        for assessment in self.assessments:

            if assessment.grade_earned is not None:
                points_earned += assessment.grade_earned * (assessment.weight / 100)
                weight_completed += assessment.weight

        if weight_completed == 0:
            return 0
        
        return points_earned / weight_completed
    
    def get_completion_rate(self) -> float:
        """Counts the amount of completed and uncompleted assessments
        and returns the completion of the course as a %"""
        completed_count = 0
        uncompleted_count = 0
        for assessment in self.assessments:

            if assessment.is_completed:
                completed_count += 1
            else:
                uncompleted_count += 1
        if completed_count + uncompleted_count == 0:
            return 0
        return  100 * completed_count / (completed_count + uncompleted_count)
    
    def to_dict(self) -> dict:
        """Converts a Course object to a dictionary 
        an all of the corresponding assessments to dictionaries"""
        assessment_lst = []
        for assessment in self.assessments:
            assessment_lst.append(assessment.to_dict())

        return{"name" : self.name, "assessments" : assessment_lst}