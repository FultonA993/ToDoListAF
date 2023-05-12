# To-Do List Application
#5/11/2023
#By: Adam Fulton

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QListWidget, QMessageBox
from PyQt5.QtGui import QFont

class ToDoListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List Application")
        self.setGeometry(200, 200, 400, 300)

        #Set Window Size
        self.setMinimumSize(400, 300) 
        self.setMaximumSize(400, 300) 

        # Create widgets
        self.label = QLabel("Task:")
        
        # Change font size
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)

        self.entry = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.list_widget = QListWidget()
        self.remove_button = QPushButton("Remove Task")
        self.remove_button.clicked.connect(self.remove_task)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.add_button)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.remove_button)

        self.entry.setStyleSheet("background-color: white;")
        self.add_button.setStyleSheet("background-color: grey;")
        self.list_widget.setStyleSheet("background-color: white;")
        self.remove_button.setStyleSheet("background-color: grey;")

        # Create central widget and set layout
        central_widget = QWidget()
        central_widget.setLayout(layout)


        self.setCentralWidget(central_widget)

        # Initialize todo_list
        self.todo_list = []

    def add_task(self):
        task = self.entry.text()
        if task:
            self.todo_list.append(task)
            self.list_widget.addItem(task)
            self.entry.clear()
        else:
            QMessageBox.warning(self, "Warning", "Please enter a task.")

    def remove_task(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            task = selected_item.text()
            self.todo_list.remove(task)
            self.list_widget.takeItem(self.list_widget.row(selected_item))
        else:
            QMessageBox.warning(self, "Warning", "No task selected.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = ToDoListApp()
    todo_app.show()
    sys.exit(app.exec_())
