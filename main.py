import sys
from PyQt5.QtWidgets import QApplication,QDialog
from mainlogindialog import LoginDialog

if __name__ == "__main__":
    app=QApplication(sys.argv)
    dl=LoginDialog()
    dl.show()
    sys.exit(app.exec_())
