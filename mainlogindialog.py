from PyQt5 import QtCore, QtGui, QtWidgets
from logindialog import Ui_LoginDialog

#继承运行界面的类
class LoginDialog(QtWidgets.QDialog,Ui_LoginDialog):
    #构造函数    
    def __init__(self):
        QtWidgets.QDialog.__init__(self)    #调用父类的构造函数
        Ui_LoginDialog.__init__(self)    #调用父类的构造函数
        self.setupUi(self)  #将自已赋值给setupUi()
        self.loginPushButton.clicked.connect(self.mylogin)  #将槽函数mylogin与loginPushButton按钮的点击信号连接起来
        self.registerPushButton.clicked.connect(self.myregister)    #将槽函数myregister与registerPushButton按钮的点击信号连接起来
    #定义槽函数mylogin
    def mylogin(self):
        print("我已登录……")
    #定义槽函数myregister
    def myregister(self):
        print("我已注册……")
