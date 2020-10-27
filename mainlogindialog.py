from PyQt5 import QtCore, QtGui, QtWidgets
from logindialog import Ui_LoginDialog

class LoginDialog(QtWidgets.QDialog,Ui_LoginDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_LoginDialog.__init__(self)
        self.setupUi(self)
        self.loginPushButton.clicked.connect(self.mylogin)
        self.registerPushButton.clicked.connect(self.myregister)

    def mylogin(self):
        print("我已登录……")

    def myregister(self):
        print("我已注册……")
