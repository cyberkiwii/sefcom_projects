import sys
from PySide2.QtCore import*
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QComboBox


class ComboBox(QWidget):
    def __int__(self):
        super().__init__()

        """
        ranNumLIST = ['h', 'j', 'k']
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(50, 50, 400, 35)
        self.comboBox.addItems(ranNumLIST)
        """

        numList = ['one', 'two', 'three']
        numChoice = QComboBox()
        numChoice.addItems(numList)

        self.btn1 = QPushButton('OK', self)
        self.btn1.clicked.connect(self.getComboValue)

    def getComboValue(self):
        print((self.comboBox.currentText(), self.comboBox.currentIndex()))

app = QApplication(sys.argv)

cb = ComboBox()
cb.show()

sys.exit(app.exec_())