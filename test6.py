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



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)

        # builds the window as a widget, specifies the layout (as grid), and makes the label text
        window = QWidget()
        window.setFixedSize(QSize(1400, 800))  # sets the window size
        layout = QGridLayout()  # GRID LAYOUT
        label = QLabel('Choose a number from the random number generator!')
        space = QLabel('                  ')

        window.show()

        # ↓
        self.__main()

    def __main(self):
        # Making window centered ↓
        self.__makeWindowCenter()

        # Window customizing ↓
        self.setWindowTitle('Free Hash Checker')

        # Clipboard setup ↓
        self.__clipboard = QApplication.clipboard()
        self.__clipboard.clear(mode=self.__clipboard.Clipboard)

        # Resetting progress bar ↓
        self.ui.progressBarHashCaclulation.reset()

        # Updating about information ↓
        self.__aboutInformationSetter()

        # Default Button's Behaviour Set ↓
        self.ui.buttonSelectFile.clicked.connect(self.__buttonSelectFile_Func)
        self.ui.buttonHashCalculate.clicked.connect(
            self.__buttonHashCalculate__Func)
        self.ui.buttonClearHashBox.clicked.connect(
            self.__buttonClearHashBox_Func)
        self.ui.buttonCopyToClipboard.clicked.connect(
            self.__buttonCopyToClipboard_Func)
        self.ui.buttonCheckHash.clicked.connect(self.__buttonCheckHash_Func)

        # Default ToolTip Information Setter ↓
        self.__toolTipInfoSetter()

        # Set License Text ↓
        self.ui.licenseTextBrowser.setText(informationManger().getLicense())

        # Hiding Menu Bar and Status Bar ↓
        self.ui.menubar.hide()
        self.ui.statusbar.hide()

        # Showing application update ↓
        # self.__updateMessageBox()

    def __updateMessageBox(self):
        appUpdates = updateManager()
        if appUpdates.haveUpdate() is True:
            updateData = appUpdates.getUpdateData()
            message: str = """<html><head/><body><p>Version: {0}</p><p>Go to download page, 
            <a style=\"text-decoration: none\" href=\"{1}\">Click Here</a></p></body></html>""".format(
                updateData['version'], updateData['update'])
            QMessageBox.information(self, 'New update!', message,
                                    QMessageBox.Ok, QMessageBox.Ok)
        else:
            pass

    # For launching windows in center ↓
    def __makeWindowCenter(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QGuiApplication.primaryScreen().geometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    # Close button behaviour ↓
    # noinspection PyCallingNonCallable
    @Slot(QCloseEvent)
    def closeEvent(self, event: QCloseEvent):
        buttonReply = QMessageBox.question(self, 'Warning', "Sure to exit?",
                                           QMessageBox.Ok | QMessageBox.Cancel,
                                           QMessageBox.Cancel)
        if buttonReply == QMessageBox.Ok:
            try:
                self.__hashCalculator.terminateThread()
            except AttributeError:
                pass
            event.accept()
        else:
            event.ignore()

    def __aboutInformationSetter(self):
        info = informationManger()
        self.ui.developerName.setText(info.developerName)
        self.ui.developerEmail.setText(info.developerEmail)
        self.ui.logoCreditName.setText(info.logoCreditName)
        self.ui.logoCreditEmail.setText(info.logoCreditEmail)
        self.ui.icons8Credit.setText(info.icons8Credit)
        self.ui.sourceCodeLink.setText(info.sourceCodeLink)
        self.ui.applicationVersion.setText(info.applicationVersion)

    # Default ToolTip Information Setter↓
    def __toolTipInfoSetter(self):
        self.ui.buttonSelectFile.setToolTip('Click to select file.')
        self.ui.buttonHashCalculate.setToolTip('Start calculation.')
        self.ui.buttonClearHashBox.setToolTip('Clear all.')
        self.ui.buttonClearCheckHashBox.setToolTip('C')
        self.ui.buttonCopyToClipboard.setToolTip('Copy hash to the clipboard.')
        self.ui.buttonCheckHash.setToolTip(
            'Paste & Check hash matching result.')
        self.ui.lineEditFileExplore.setToolTip(
            'Selected file location will be shown here.')
        self.ui.lineEditHashBox.setToolTip(
            'Calculated hash will be shown here.')
        self.ui.progressBarHashCaclulation.setToolTip(
            'Calculation\'s progress will be shown here.')
        self.ui.buttonClearCheckHashBox.setToolTip('Clear pasted hash.')
        self.ui.lineEditCheckHashBox.setToolTip(
            'Pasted hash will be shown here for matching.')
        self.ui.developerName.setToolTip(informationManger().developerName)
        info = informationManger()
        self.ui.developerName.setToolTip(info.developerNameTooltip)
        self.ui.developerEmail.setToolTip(info.developerEmailTooltip)
        self.ui.logoCreditName.setToolTip(info.logoCreditNameTooltip)
        self.ui.logoCreditEmail.setToolTip(info.logoCreditEmailTooltip)
        self.ui.icons8Credit.setToolTip(info.icons8CreditTooltip)
        self.ui.sourceCodeLink.setToolTip(info.sourceCodeLinkTooltip)
        self.ui.applicationVersion.setToolTip(info.applicationVersionTooltip)
        self.ui.licenseTextBrowser.setToolTip(info.licenseTextBrowserTooltip)

    def __buttonSelectFile_Func(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        # noinspection PyTypeChecker
        fileName = dialog.getOpenFileName(self, self.tr(u"Select a File"),
                                          str(), self.tr(u"All Files (*)"))
        fileName = fileName[0]
        if fileName:
            self.ui.lineEditFileExplore.clear()
            self.ui.lineEditFileExplore.setText(fileName)
            self.ui.labelFileExplore.setPixmap(QPixmap(":ok/ok.png"))
            logging.info('File selected "{0}"'.format(fileName))
            try:
                self.ui.buttonHashCalculate.clicked.disconnect()
            except RuntimeError:
                pass
            self.ui.buttonHashCalculate.clicked.connect(
                self.__buttonHashCalculate__Func)

    def __buttonHashCalculate__Func(self):
        if not os.path.isfile(self.ui.lineEditFileExplore.text()):
            # noinspection PyTypeChecker
            QMessageBox().warning(None, 'Warning',
                                  'Please select a file to continue!',
                                  QMessageBox.Ok)
        else:
            self.__hashCalculator = HashingMethods()
            self.__hashCalculator.setHashName(
                self.ui.comboBoxHashChoices.currentText())
            self.__hashCalculator.setFileLoc(
                self.ui.lineEditFileExplore.text())
            self.__hashCalculator.signalEmitter.calculatedHash.connect(
                self.__on_finished_hash_calculation)
            self.__hashCalculator.signalEmitter.progressBarValue.connect(
                self.__on_going_progressbar)
            self.__hashCalculator.start()
            if self.__hashCalculator.isRunning():
                self.ui.progressBarHashCaclulation.setFormat('%p%')
                self.ui.buttonHashCalculate.setText('Cancel')
                self.ui.buttonHashCalculate.setIcon(
                    QIcon(':/cancel/cancel.png'))
                self.ui.buttonHashCalculate.clicked.disconnect()
                self.ui.buttonHashCalculate.clicked.connect(
                    self.__btnHashCalculatorThreadCanceler_Func)



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

