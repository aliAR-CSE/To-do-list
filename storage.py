import json
from course import Course
file_name = "data.JSON"
""""Converts the list of courses in a dictionary and imported into a JSON file"""
def save_courses(file_name: str, courses: list[Course]):
    data = []
    for course in courses:
        data.append(course.to_dict())
    with open(file_name, "w", encoding = 'utf-8') as file:
        json.dump(data, file, ensure_ascii = False, indent = 4)