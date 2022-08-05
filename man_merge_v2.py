import sys
import random
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize, QEvent
from PySide2.QtGui import QPalette, QColor

# todo make a long list of 50 options. have them all be displayed on the screen; be able to edit them with a clickable dropdown.

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

def gen_random_dic_pairs():
    return [
        (generate_random_dict(), generate_random_dict()) for _ in range(random.randint(2,25))
    ]

class MergeWin(QDialog):
    def __init__(self, dictionary):
        super().__init__()

        self.setWindowTitle("Manual Merge")

        self.dict = dictionary

        QBtn1 = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn1)
        self.buttonBox.accepted.connect(self.okay_button)


        self.layout = QGridLayout()
        self.setLayout(self.layout)



        x = len(self.dict)  #sets the number of lines added to the window

        self.types = {}
        self.names = {}
        self.final = {}

        self.org_pairs = []

        for i in range(x):
            type_ = QLabel(str(self.dict[i][0]["type"]))
            self.types[type_] = [self.dict[i][0]["type"], self.dict[i][1]["type"]]
            self.layout.addWidget(type_, i, 1)
            type_.installEventFilter(self)

            name_ = QLabel(str(self.dict[i][0]["name"]))
            self.names[name_] = [self.dict[i][0]["name"], self.dict[i][1]["name"]]
            self.layout.addWidget(name_, i, 2)
            name_.installEventFilter(self)

            self.final[(type_, name_)] = {"type": (self.dict[i][0]["type"]), "name": (self.dict[i][0]["name"])}
            first = type_
            second = name_

            self.org_pairs.append((first, second))


        self.layout.addWidget(self.buttonBox, x+2, 3)

    def tuple_pairs(self, source):
        tuples_ = self.org_pairs
        for tup in tuples_:
            print(source)
            print(tup[0])
            print(tup[1])
            if source == tup[0]:
                other = tup[1]
                break
            elif source == tup[1]:
                other = tup[0]
                break
        return other



    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source in self.types:
            menu = QMenu()
            for i in range(2):
                menu.addAction(self.types[source][i])

            action = menu.exec_(event.globalPos())

            if action:
                item = action.text()
                source.setText(f"{item} ")
                other = self.tuple_pairs(source)
                self.set_type = item
                self.final[(source, other)]["type"] = item

        if event.type() == QEvent.ContextMenu and source in self.names:
            menu = QMenu()
            for i in range(2):
                menu.addAction(self.names[source][i])

            action = menu.exec_(event.globalPos())

            if action:
                item = action.text()
                source.setText(f"{item}")
                other = self.tuple_pairs(source)
                self.set_type = item
                self.final[(other, source)]["name"] = item



        return super().eventFilter(source, event)


    def okay_button(self):
        vals = self.final.values()
        print(vals)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")

        startButton = QPushButton("Press here to start")
        startButton.clicked.connect(self.start_code)
        self.setCentralWidget(startButton)


    def start_code(self):
        print("User clicked the Start Button")

        win1 = MergeWin(gen_random_dic_pairs())
        win1.exec_()


app = QApplication(sys.argv)

main = MainWindow()

main.show()
app.exec_()

