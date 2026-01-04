import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QHBoxLayout, 
                             QGridLayout, QDesktopWidget, QTreeWidgetItem,
                             QTreeWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acedemic Planner")
        self.resize(900, 600)
        self.center()
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.center()

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        drop_down = QTreeWidget()
        drop_down.setColumnCount(4)
        layout.addWidget(drop_down)
        drop_down.setHeaderLabels(['Name', 'Type', 'Weight', 'Grade'])
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()