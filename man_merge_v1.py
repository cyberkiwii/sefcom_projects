import sys
import random
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize, QEvent
from PySide2.QtGui import QPalette, QColor

def generate_random_dict():
    types = [
        "int", "char", "long", "int*", "char*", "long*", "bool"
    ]
    _type = random.choice(types)
    _name = f"v{random.randint(1,90)}"
    return {
        "type": _type,
        "name": _name
    }


class MergeWin(QDialog):
    def __init__(self, dict1, dict2):
        super().__init__()

        self.setWindowTitle("Manual Merge")

        self.d1 = dict1
        self.d2 = dict2

        QBtn1 = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn1)
        self.buttonBox.accepted.connect(self.okay_button)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QGridLayout()
        self.setLayout(self.layout)


        self.text1 = QLabel(f"{self.d1['type']} ")
        self.text2 = QLabel(f"{self.d2['name']};")
        space = QLabel(" ")

        self.text1.installEventFilter(self)
        self.text2.installEventFilter(self)

        # self.layout.addWidget(space)
        self.layout.addWidget(self.text1, 1, 1)
        self.layout.addWidget(self.text2, 1, 2)
        # self.layout.addWidget(space)

        self.layout.addWidget(self.buttonBox, 3, 2)




    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self.text1:
            menu = QMenu()
            menu.addAction(self.d1['type'])
            menu.addAction(self.d2['type'])

            action = menu.exec_(event.globalPos())

            if action:
                item = action.text()
                self.text1.setText(f"{item} ")
                self.set_type = item




        if event.type() == QEvent.ContextMenu and source is self.text2:
            menu = QMenu()
            menu.addAction(self.d1['name'])
            menu.addAction(self.d2['name'])

            action = menu.exec_(event.globalPos())

            if action:
                item = action.text()
                self.text2.setText(item)
                self.set_name = item


        return super().eventFilter(source, event)


    def okay_button(self):
        print(self.set_type + " " + self.set_name)






class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")

        startButton = QPushButton("Press here to start")
        startButton.clicked.connect(self.start_code)
        self.setCentralWidget(startButton)


    def start_code(self):
        print("User clicked the Start Button")

        win1 = MergeWin(generate_random_dict(), generate_random_dict())
        win1.exec_()


app = QApplication(sys.argv)

main = MainWindow()

main.show()
app.exec_()

