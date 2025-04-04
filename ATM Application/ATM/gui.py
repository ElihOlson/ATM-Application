# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ATM(object):
    def setupUi(self, ATM):
        ATM.setObjectName("ATM")
        ATM.resize(300, 400)
        ATM.setMinimumSize(QtCore.QSize(300, 400))
        ATM.setMaximumSize(QtCore.QSize(300, 400))
        self.centralwidget = QtWidgets.QWidget(parent=ATM)
        self.centralwidget.setObjectName("centralwidget")
        self.input_first = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_first.setGeometry(QtCore.QRect(100, 30, 121, 20))
        self.input_first.setObjectName("input_first")
        self.label_first = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_first.setGeometry(QtCore.QRect(30, 30, 61, 16))
        self.label_first.setObjectName("label_first")
        self.label_last = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_last.setGeometry(QtCore.QRect(30, 60, 61, 16))
        self.label_last.setObjectName("label_last")
        self.label_pin = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_pin.setGeometry(QtCore.QRect(30, 90, 61, 16))
        self.label_pin.setObjectName("label_pin")
        self.input_last = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_last.setGeometry(QtCore.QRect(100, 60, 121, 20))
        self.input_last.setObjectName("input_last")
        self.input_pin = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_pin.setGeometry(QtCore.QRect(100, 90, 121, 20))
        self.input_pin.setObjectName("input_pin")
        self.label_atm = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_atm.setGeometry(QtCore.QRect(130, 10, 41, 16))
        self.label_atm.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_atm.setObjectName("label_atm")
        self.button_login = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_login.setGeometry(QtCore.QRect(90, 140, 61, 21))
        self.button_login.setObjectName("button_login")
        self.label_change = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_change.setGeometry(QtCore.QRect(20, 170, 261, 41))
        self.label_change.setText("")
        self.label_change.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_change.setObjectName("label_change")
        self.label_question = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_question.setGeometry(QtCore.QRect(20, 210, 261, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label_question.setFont(font)
        self.label_question.setAutoFillBackground(False)
        self.label_question.setStyleSheet("")
        self.label_question.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_question.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_question.setObjectName("label_question")
        self.radio_withdrawl = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radio_withdrawl.setGeometry(QtCore.QRect(70, 240, 81, 21))
        self.radio_withdrawl.setObjectName("radio_withdrawl")
        self.radio_deposite = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radio_deposite.setGeometry(QtCore.QRect(180, 240, 71, 21))
        self.radio_deposite.setObjectName("radio_deposite")
        self.label_amount = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_amount.setGeometry(QtCore.QRect(10, 270, 51, 16))
        self.label_amount.setObjectName("label_amount")
        self.input_amount = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(80, 270, 171, 16))
        self.input_amount.setObjectName("input_amount")
        self.label_balance = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_balance.setGeometry(QtCore.QRect(40, 300, 221, 30))
        self.label_balance.setText("")
        self.label_balance.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_balance.setObjectName("label_balance")
        self.button_enter = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_enter.setGeometry(QtCore.QRect(60, 330, 71, 31))
        self.button_enter.setObjectName("button_enter")
        self.button_exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(170, 330, 71, 31))
        self.button_exit.setObjectName("button_exit")
        self.button_signup = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_signup.setGeometry(QtCore.QRect(170, 140, 61, 21))
        self.button_signup.setObjectName("button_signup")
        ATM.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ATM)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 18))
        self.menubar.setObjectName("menubar")
        ATM.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ATM)
        self.statusbar.setObjectName("statusbar")
        ATM.setStatusBar(self.statusbar)

        self.retranslateUi(ATM)
        QtCore.QMetaObject.connectSlotsByName(ATM)

    def retranslateUi(self, ATM):
        _translate = QtCore.QCoreApplication.translate
        ATM.setWindowTitle(_translate("ATM", "ATM"))
        self.label_first.setText(_translate("ATM", "First Name"))
        self.label_last.setText(_translate("ATM", "Last Name"))
        self.label_pin.setText(_translate("ATM", "Enter PIN"))
        self.label_atm.setText(_translate("ATM", "ATM"))
        self.button_login.setText(_translate("ATM", "LOGIN"))
        self.label_question.setText(_translate("ATM", "Please Select Deposite or Withdrawl"))
        self.radio_withdrawl.setText(_translate("ATM", "Withdrawl"))
        self.radio_deposite.setText(_translate("ATM", "Deposite"))
        self.label_amount.setText(_translate("ATM", "Amount"))
        self.button_enter.setText(_translate("ATM", "ENTER"))
        self.button_exit.setText(_translate("ATM", "EXIT"))
        self.button_signup.setText(_translate("ATM", "SIGNUP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ATM = QtWidgets.QMainWindow()
    ui = Ui_ATM()
    ui.setupUi(ATM)
    ATM.show()
    sys.exit(app.exec())
