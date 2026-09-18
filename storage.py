import json
from course import Course
from assessment import Assessment
from datetime import date
import os
DEFAULT_FILE_PATH = "data.JSON"


def save_courses(file_path: str, courses: list[Course]):
    """Converts a list of Course objects Into a list of 
    dictionaries, then saves it to a JSON file
    """
    data = []
    for course in courses:
        data.append(course.to_dict())
    with open(file_path, "w", encoding = 'utf-8') as file:
        json.dump(data, file, ensure_ascii = False, indent = 4)

def load_courses(file_path: str) -> list[Course]:
    """Converts JSON into a list of Course object"""
    course_list = []
    if not os.path.exists(file_path):
        with open(file_path,"x") as file:
            json.dump(course_list, file, ensure_ascii = False, indent = 4)
    else:      
        with open(file_path, 'r') as file:

            data_list = json.load(file) # parse JSON file and obtain lst[dict]

        for course in data_list:

            new_course = Course(course["name"])

            for assessment in course["assessments"]:
                new_assessment = Assessment(assessment["name"], assessment["kind"], date.fromisoformat(assessment["due_date"]), assessment["weight"])
                new_assessment.grade_earned = assessment["grade_earned"]
                new_assessment.is_completed = assessment["is_completed"]
                new_course.assessments.append(new_assessment)
            course_list.append(new_course)

    return course_list