import sys
import random
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPalette, QColor

# todo size the windows!

#todo set up color and theme maybe ???




class Window1(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random Number Generator")

        QBtn1 = QDialogButtonBox.Ok | QDialogButtonBox.Cancel




        # label that explains to user what to do
        label = QLabel('Choose a number from the random number generator!\n')


        # This call and executes the combo box defined
        # redefines them so they can be used
        num1, num2, num3 = self.get_nums()
        print("\nThe number generated and given to the user are: ", num1, num2, num3)

        numList = [str(num1), str(num2), str(num3)]
        self.numChoice = QComboBox()

        # numChoice.setStyleSheet("background-color: black;")  # TODO set background color for the combo box
        # numChoice.setStyleSheet("color: white;")
        self.numChoice.addItems(numList)

        self.buttonBox = QDialogButtonBox(QBtn1)
        self.buttonBox.accepted.connect(self.okay_button)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()


        self.layout.addWidget(label)
        self.layout.addWidget(self.numChoice)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    # creates the ComboBox that is a random number generator.

    # this function gets the numbers that are given to the user in the ComboBox
    def get_nums(self):
        x = 0

        # while the x is NOT 4, the while function will repeat in order to get random values that are NOT the same.
        while x != 4:
            # Gets the random numbers that are between 1 and 10
            print("Generating Numbers...")
            ran1 = random.randint(0, 10)
            ran2 = random.randint(0, 10)
            ran3 = random.randint(0, 10)
            print("The generated numbers are: ", ran1, ran2, ran3)

            # Checks to see if any of the numbers generated are the same
            if ran1 != ran2 and ran2 != ran3 and ran1 != ran3:

                # If none of the numbers are the same, the program continues and gives those numbers to the user.
                print("\nDONE! None of the numbers are the same.")
                x = 4
                # when the if value is true, x is set to 4 and the while loop ends


            else:

                # if any of the numbers are the same, x is set to 2 so the while loop restarts
                print("But two or more of the numbers are the same! It will re-generate the numbers\n")
                x = 2

        # returns the checked random values to be put in the ComboBox
        return ran1, ran2, ran3

    def okay_button(self):
        input1 = self.numChoice.currentText()
        print("the user chose", input1)

        self.accept()
        print("User clicked the OK button")

        win2 = Window2(input1)
        win2.exec_()


class Window2(QDialog):
    def __init__(self, num):
        super().__init__()

        self.setWindowTitle("Number Choice")

        self.finalNum = num

        QBtn2 = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn2)
        self.buttonBox.accepted.connect(self.accept)


        self.layout = QVBoxLayout()


        # label that explains to user what to do
        text = QLabel('The number you chose is \n' + self.finalNum)
        #todo add a code that puts the number they chose

        self.layout.addWidget(text)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")

        startButton = QPushButton("Press here to start")
        startButton.clicked.connect(self.start_code)
        self.setCentralWidget(startButton)

    def start_code(self):
        print("User clicked the Start Button")

        win1 = Window1()
        win1.exec_()



app = QApplication(sys.argv)

main = MainWindow()

main.show()
app.exec_()