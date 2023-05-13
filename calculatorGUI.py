from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setMinimumSize(QtCore.QSize(500, 600))
        MainWindow.setMaximumSize(QtCore.QSize(500, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(40, 460, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.divisionButton = QtWidgets.QPushButton(self.centralwidget)
        self.divisionButton.setGeometry(QtCore.QRect(340, 150, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.divisionButton.setFont(font)
        self.divisionButton.setIconSize(QtCore.QSize(20, 20))
        self.divisionButton.setObjectName("divisionButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget)
        self.equalButton.setGeometry(QtCore.QRect(290, 460, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget)
        self.zeroButton.setGeometry(QtCore.QRect(140, 390, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget)
        self.decimalButton.setGeometry(QtCore.QRect(240, 390, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget)
        self.multiplyButton.setGeometry(QtCore.QRect(340, 230, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setIconSize(QtCore.QSize(100, 100))
        self.multiplyButton.setObjectName("multiplyButton")
        self.subtractButton = QtWidgets.QPushButton(self.centralwidget)
        self.subtractButton.setGeometry(QtCore.QRect(340, 310, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.subtractButton.setFont(font)
        self.subtractButton.setObjectName("subtractButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(340, 390, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.negativeButton = QtWidgets.QPushButton(self.centralwidget)
        self.negativeButton.setGeometry(QtCore.QRect(40, 390, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.negativeButton.setFont(font)
        self.negativeButton.setObjectName("negativeButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(40, 310, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget)
        self.twoButton.setGeometry(QtCore.QRect(140, 310, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget)
        self.threeButton.setGeometry(QtCore.QRect(240, 310, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget)
        self.fourButton.setGeometry(QtCore.QRect(40, 230, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget)
        self.fiveButton.setGeometry(QtCore.QRect(140, 230, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget)
        self.sixButton.setGeometry(QtCore.QRect(240, 230, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget)
        self.sevenButton.setGeometry(QtCore.QRect(40, 150, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget)
        self.eightButton.setGeometry(QtCore.QRect(140, 150, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget)
        self.nineButton.setGeometry(QtCore.QRect(240, 150, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.numberDisplay = QtWidgets.QTextBrowser(self.centralwidget)
        self.numberDisplay.setGeometry(QtCore.QRect(40, 10, 421, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.numberDisplay.setFont(font)
        self.numberDisplay.setObjectName("numberDisplay")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.divisionButton.setText(_translate("MainWindow", "÷"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.multiplyButton.setText(_translate("MainWindow", "×"))
        self.subtractButton.setText(_translate("MainWindow", "-"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.negativeButton.setText(_translate("MainWindow", "+/-"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.nineButton.setText(_translate("MainWindow", "9"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
