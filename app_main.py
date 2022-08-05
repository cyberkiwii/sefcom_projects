
# only needed for access to command line arguments
import sys
import random
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox


print(random.randint(1,100))

# subclass QMainWindow to customize your application's main window
"""
class MainWin
# only needed for access to command line arguments
import sys
import random
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox


print(random.randint(1,100))

# subclass QMainWindow to customize your application's main window
"""
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Push This Button")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)


        self.setCentralWidget(self.button)

        self.setMinimumSize(700, 600)


        # set the central widget of the window
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("Already pressed")
        self.button.setEnabled(False)

        self.button.setEnabled(False)

    def the_button_was_toggled(self, checked):
        print("checked ? ", checked)
"""

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        drop_down = QComboBox()
        #widget.addItems(["One", "Two", "Three"])
        drop_down.addItems([str(random.randint(0,10000)), str(random.randint(0,10000)), str(random.randint(0,10000))])
        drop_down.setMaxCount(10)

        # The default signal from currentIndexChanged sends the index
        drop_down.currentIndexChanged.connect(self.index_changed)

        # The same signal can send a text string
        drop_down.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(drop_down)


    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s): # s is a str
        print(s)


# you need one (and only one) QApplication instance per application
# pass in sys.argv to allow command line arguments for your app.
# if you know you won't use command line arguments QApplication([]) works too
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # IMPORTANT!! Windows are hidden by default

# start the event loop
app.exec_()

# your application wont reach her until you exit and the event loop has stopped
dow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Push This Button")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)


        self.setCentralWidget(self.button)

        self.setMinimumSize(700, 600)


        # set the central widget of the window
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("Already pressed")
        self.button.setEnabled(False)

        self.button.setEnabled(False)

    def the_button_was_toggled(self, checked):
        print("checked ? ", checked)
"""

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        drop_down = QComboBox()
        #widget.addItems(["One", "Two", "Three"])
        drop_down.addItems([str(random.randint(0,10000)), str(random.randint(0,10000)), str(random.randint(0,10000))])
        drop_down.setMaxCount(10)

        # The default signal from currentIndexChanged sends the index
        drop_down.currentIndexChanged.connect(self.index_changed)

        # The same signal can send a text string
        drop_down.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(drop_down)


    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s): # s is a str
        print(s)


# you need one (and only one) QApplication instance per application
# pass in sys.argv to allow command line arguments for your app.
# if you know you won't use command line arguments QApplication([]) works too
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # IMPORTANT!! Windows are hidden by default

# start the event loop
app.exec_()

# your application wont reach her until you exit and the event loop has stopped
