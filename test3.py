import sys
from PySide2.QtCore import*
from PySide2.QtWidgets import*

app = QApplication(sys.argv)

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


text = QLabel("Hello")
font = text.font()
font.setPointSize(30)
text.setFont(font)


numList = ['one', 'two', 'three']
numChoice = QComboBox()
numChoice.addItems(numList)

l = QHBoxLayout()
done_btn = QPushButton("OKAY")
done_btn.setStyleSheet("background-color: green")
done_btn.clicked.connect(done_was_clicked)
l.addWidget(done_btn)

cancel_btn = QPushButton("CANCEL")
cancel_btn.setStyleSheet("background-color: green")
cancel_btn.clicked.connect(cancel_was_clicked)
# cancel_btn.clicked.connect(self.toggle_window2)
l.addWidget(cancel_btn)

w = QWidget()
w.setLayout(l)
# self.setCentralWidget(w)



text.show()
numChoice.show()
done_btn.show()
cancel_btn.show()
app.exec_()