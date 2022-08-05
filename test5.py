import sys
import random
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPalette, QColor


app = QApplication(sys.argv)
app.setStyle('Fusion')

# Colors / Theme

default_palette = QPalette()
dark_palette = QPalette()
dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
dark_palette.setColor(QPalette.WindowText, Qt.white)
dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
dark_palette.setColor(QPalette.ToolTipText, Qt.white)
dark_palette.setColor(QPalette.Text, Qt.white)
dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ButtonText, Qt.white)
dark_palette.setColor(QPalette.BrightText, Qt.red)
dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, Qt.black)


class window1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)


class window2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # builds the window as a widget, specifies the layout (as grid), and makes the label text
        window = QWidget()
        window.setFixedSize(QSize(1400, 800)) #sets the window size
        layout = QGridLayout()  # GRID LAYOUT
        label = QLabel('Choose a number from the random number generator!')
        space = QLabel('                  ')

        window.show()

        # creates the ComboBox that is a random number generator.

        # this function gets the numbers that are given to the user in the ComboBox
        def get_nums():
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


        # redefines them so they can be used
        num1, num2, num3 = get_nums()
        print("\nThe number generated and given to the user are: ", num1, num2, num3)

        numList = [str(num1), str(num2), str(num3)]
        numChoice = QComboBox()
        numChoice.setStyleSheet("background-color: black;")  # TODO set background color for the combo box
        numChoice.setStyleSheet("color: white;")
        numChoice.addItems(numList)

        # This code creates the Buttons



        ok_btn = QPushButton("OKAY")
        # ok_btn.clicked.connect(self.ok_was_clicked)
        ok_btn.clicked.connect(self.toggle_window1)
        ok_btn.setStyleSheet("color: white; background-color: black;")  # TODO why does the color not change when click???
        # TODO set up toggle that when button is pushed it is printed to the console and an action happens :
        # if you press "okay" then a new window pops up (and the old one closes) and it prints the users number choice!
        # if you press "cancel" there is a pop up window that asked the user to confirm whether they want to close the program
        cnc_btn = QPushButton("CANCEL")
        cnc_btn.setStyleSheet("background-color: black")  # TODO change colors!
        cnc_btn.setStyleSheet("color: white;")
        # cnc_btn.clicked.connect(self.cancel_was_clicked)
        # cnc_btn.clicked.connect(toggle_window2)

        # This code sets the placement of the different widgets / objects
        layout.addWidget(space, 0, 1)
        # layout.addWidget(space, 1, 1)
        layout.addWidget(label, 4, 2)
        layout.addWidget(numChoice, 6, 2)
        layout.addWidget(space, 7, 2)
        layout.addWidget(ok_btn, 10, 9)
        layout.addWidget(cnc_btn, 10, 10)
        layout.addWidget(space, 11, 11)

        window.setLayout(layout)


    def toggle_window1(self, checked):
            if window1.isVisible():
                window1.hide()

            else:
                window1.show()


    def ok_was_clicked(self):
            ok_btn.clicked.connect(self.toggle_window1)
            print("The user clicked the 'OKAY' button!")
            # TODO make it move to the next window where the number that was selected by the user is printed
            # TODO (In the next window): "you selected { }" give an 'okay' btn and end the program


    def cancel_was_clicked(self):
            print("The user clicked the 'CANCEL' button!")
            # TODO if user selects the 'cancel' btn, then the program asks "are you sure you want to close out?" with a yes or no btn choice.
            # TODO if 'no' then the window warning closes and they can use the program.
            # TODO if 'yes' the program closes





# This code sets the placement of the different widgets / objects


w = MainWindow()
w.show()
app.exec_()


