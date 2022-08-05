
import sys
import random
from PySide2.QtCore import Qt, QSize
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QWidget, QMessageBox, QLabel, QLineEdit, QHBoxLayout




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        text = QLabel("Hello")
        font = text.font()
        font.setPointSize(30)
        text.setFont(font)

        self.setCentralWidget(text)

        self.cb = self.ComboBox()
        self.b_t_n_s = self.Buttons()

    class ComboBox(QWidget):
        def __init__(self):
            super().__init__()

            drop_down = QComboBox()
            drop_down.show()
            # drop_down.addItems(["One", "Two", "Three"])
            drop_down.addItems(
                [str(random.randint(0, 10000)), str(random.randint(0, 10000)), str(random.randint(0, 10000))])

            # The default signal from currentIndexChanged sends the index
            drop_down.currentIndexChanged.connect(self.index_changed)

            # The same signal can send a text string
            drop_down.currentTextChanged.connect(self.text_changed)

            # self.setCentralWidget(drop_down)

        def index_changed(self, i):  # i is an int
            print(i)


        def text_changed(self, s):  # s is a str
            print(s)


    class Buttons(QWidget):
        def __init__(self):
            super().__init__()
            # TODO for some reason the program wont allow both the QComboBox and the buttons to be on the window. while the button box is there the progam prioritizes that and doesnt show the dropdown
            l = QHBoxLayout()
            done_btn = QPushButton("DONE")
            done_btn.setStyleSheet("background-color: green")
            done_btn.clicked.connect(self.done_was_clicked)
            l.addWidget(done_btn)

            cancel_btn = QPushButton("CANCEL")
            cancel_btn.setStyleSheet("background-color: green")
            cancel_btn.clicked.connect(self.cancel_was_clicked)
            # cancel_btn.clicked.connect(self.toggle_window2)
            l.addWidget(cancel_btn)

            w = QWidget()
            w.setLayout(l)
            # self.setCentralWidget(w)

        def toggle_window1(self, checked):
            if self.window1.isVisible():
                self.window1.hide()

            else:
                self.window1.show()

        def done_was_clicked(self):
            # done_btn.clicked.connect(self.toggle_window1)
            print("The user clicked the 'DONE' button!")
            # TODO make it move to the next window where the number that was selected by the user is printed
            # TODO (In the next window): "you selected { }" give an 'okay' btn and end the program

        def cancel_was_clicked(self):
            print("The user clicked the 'CANCEL' button!")
            # TODO if user selects the 'cancel' btn, then the program asks "are you sure you want to close out?" with a yes or no btn choice.
            # TODO if 'no' then the window warning closes and they can use the program.
            # TODO if 'yes' the program closes



app = QApplication(sys.argv)

window = MainWindow()
window.show()


combo = window.cb()
btns = window.b_t_n_s()


combo.display()
btns.display()

# start the event loop
app.exec_()

# your application wont reach her until you exit and the event loop has stopped


