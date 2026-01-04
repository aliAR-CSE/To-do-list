import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QHBoxLayout, 
                             QGridLayout, QDesktopWidget, QTreeWidgetItem,
                             QTreeWidget)
from storage import save_courses, load_courses, FILE_NAME

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acedemic Planner")
        self.courses = load_courses(FILE_NAME)
        self.resize(900, 600)
        self.center()
        self.initUI()

    def initUI(self):
        """Sets up the lay out of the MainWindow by initilizing
        a central widget were other widgets can be added """
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.center()
        self.tree = QTreeWidget()

        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        self.tree.setColumnCount(5)
        layout.addWidget(self.tree)
        self.tree.setHeaderLabels(['Name', 'Type', 'Weight', 'Grade', 'Completion'])
        self.refresh_tree()

    def center(self):
        """Automatically centers the MainWindow 
        to the center of the screen"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def refresh_tree(self):
        """Clears all object in the tree then fills the
        tree based on the data loaded form the JSON file"""
        self.tree.clear()
        # set the courses in the tree
        for course in self.courses:
            new_course = QTreeWidgetItem(self.tree)
            new_course.setText(0, course.name)
            # set the assessments
            for assessment in course.assessments:
                new_assessment = QTreeWidgetItem(new_course)
                new_assessment.setText(0, assessment.name)
                new_assessment.setText(1, assessment.kind)
                new_assessment.setText(2, str(assessment.weight))
                if assessment.grade_earned is None:
                    new_assessment.setText(3, '-')
                else:
                    new_assessment.setText(3, str(assessment.grade_earned))
                if assessment.is_completed:
                    new_assessment.setText(4, '\u2714')
                else:
                    new_assessment.setText(4, 'X')
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()