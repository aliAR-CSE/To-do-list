
class Course:


    def __init__(self, name: str):
        self.name = name
        self.assessments = []

    def update(self, name = None):
        if name is not None:
            self.name = name
