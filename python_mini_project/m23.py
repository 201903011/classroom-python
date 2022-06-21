from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from tkinter import filedialog , messagebox
import sys

from  dow_file  import  Ui_Frame1 

class  Course_window(object):
    def __init__(self) :
        object.__init__(self)
        self.Frame = QtWidgets.QFrame()
        self.ui = Ui_Frame1()
        self.ui.setupUi(self.Frame)
        self.Frame.show()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(339, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login = QtWidgets.QTabWidget(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(0, 10, 341, 561))
        self.login.setMinimumSize(QtCore.QSize(341, 561))
        self.login.setMaximumSize(QtCore.QSize(341, 561))
        self.login.setStyleSheet("")
        self.login.setTabPosition(QtWidgets.QTabWidget.North)
        self.login.setUsesScrollButtons(False)
        self.login.setDocumentMode(False)
        self.login.setTabsClosable(False)
        self.login.setMovable(False)
        self.login.setTabBarAutoHide(False)
        self.login.setObjectName("login")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Logbut = QtWidgets.QPushButton(self.tab)
        self.Logbut.setGeometry(QtCore.QRect(80, 350, 191, 51))
        self.Logbut.setStyleSheet("\n"
"QPushButton{\n"
"\n"
"border-radius: 10px ;\n"
"background-color: rgb(71, 147, 227);\n"
"\n"
"}")
        self.Logbut.setText("")
        self.Logbut.setObjectName("Logbut")
        self.Logbut.clicked.connect(self.gotoSecond)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(140, 360, 61, 31))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 490, 51, 16))
        self.label_2.setStyleSheet("background-color: rgb(71, 147, 227);\n"
"border-radius:5px;\n"
"")
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(self.tab)
        self.username.setGeometry(QtCore.QRect(80, 160, 191, 31))
        self.username.setStyleSheet("border-radius: 7px ;\n"
"background-color: rgb(197, 197, 197);")
        self.username.setText("")
        self.username.setObjectName("username")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(90, 200, 121, 21))
        self.label_3.setObjectName("label_3")
        self.password = QtWidgets.QLineEdit(self.tab)
        self.password.setGeometry(QtCore.QRect(80, 250, 191, 31))
        self.password.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius: 7px ;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(90, 290, 111, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(130, 20, 81, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../logo.png"))
        self.label_5.setObjectName("label_5")
        self.login.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.user = QtWidgets.QLineEdit(self.tab_2)
        self.user.setGeometry(QtCore.QRect(60, 100, 221, 31))
        self.user.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius: 7px;")
        self.user.setObjectName("user")
        self.passwoed = QtWidgets.QLineEdit(self.tab_2)
        self.passwoed.setGeometry(QtCore.QRect(60, 290, 221, 31))
        self.passwoed.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius: 7px;")
        self.passwoed.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwoed.setObjectName("passwoed")
        self.confpass = QtWidgets.QLineEdit(self.tab_2)
        self.confpass.setGeometry(QtCore.QRect(60, 360, 221, 31))
        self.confpass.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius: 7px;")
        self.confpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confpass.setObjectName("confpass")
        self.email = QtWidgets.QLineEdit(self.tab_2)
        self.email.setGeometry(QtCore.QRect(60, 220, 221, 31))
        self.email.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius: 7px;")
        self.email.setObjectName("email")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(70, 130, 121, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(70, 250, 121, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(70, 320, 121, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(70, 390, 121, 21))
        self.label_14.setObjectName("label_14")
        self.Logbut_3 = QtWidgets.QPushButton(self.tab_2)
        self.Logbut_3.setGeometry(QtCore.QRect(70, 430, 201, 51))
        self.Logbut_3.setStyleSheet("\n"
"QPushButton{\n"
"\n"
"border-radius: 10px ;\n"
"background-color: rgb(71, 147, 227);\n"
"\n"
"}")
        self.Logbut_3.setText("")
        self.Logbut_3.setObjectName("Logbut_3")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(120, 440, 121, 31))
        self.label_15.setStyleSheet("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(130, 20, 81, 61))
        self.label_16.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("../logo.png"))
        self.label_16.setObjectName("label_16")
        self.firstname = QtWidgets.QLineEdit(self.tab_2)
        self.firstname.setGeometry(QtCore.QRect(60, 160, 61, 31))
        self.firstname.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius: 7px;")
        self.firstname.setObjectName("firstname")
        self.lastname = QtWidgets.QLineEdit(self.tab_2)
        self.lastname.setGeometry(QtCore.QRect(220, 160, 61, 31))
        self.lastname.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius: 7px;")
        self.lastname.setObjectName("lastname")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(60, 190, 61, 21))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(220, 190, 71, 21))
        self.label_18.setObjectName("label_18")
        self.firstname_2 = QtWidgets.QLineEdit(self.tab_2)
        self.firstname_2.setGeometry(QtCore.QRect(140, 160, 61, 31))
        self.firstname_2.setStyleSheet("background-color: rgb(197, 197, 197);\n"
"border-radius: 7px;")
        self.firstname_2.setObjectName("firstname_2")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(130, 190, 71, 21))
        self.label_19.setObjectName("label_19")
        self.login.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 339, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.login.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#fefefe;\">Login</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Login</span></p></body></html>"))
        self.username.setPlaceholderText(_translate("MainWindow", "username"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#4793e3;\">   Username</span></p></body></html>"))
        self.password.setPlaceholderText(_translate("MainWindow", "password"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#4793e3;\">Password</span></p></body></html>"))
        self.login.setTabText(self.login.indexOf(self.tab), _translate("MainWindow", "Login"))
        self.user.setPlaceholderText(_translate("MainWindow", "username"))
        self.passwoed.setPlaceholderText(_translate("MainWindow", "password"))
        self.confpass.setPlaceholderText(_translate("MainWindow", "confirm password"))
        self.email.setPlaceholderText(_translate("MainWindow", "email@e.com"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#4793e3;\">   Username</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#4793e3;\">Email</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#4793e3;\">Password</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#4793e3;\">Confirm Password</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#fefefe;\">Sign Up</span></p></body></html>"))
        self.firstname.setPlaceholderText(_translate("MainWindow", "Name"))
        self.lastname.setPlaceholderText(_translate("MainWindow", "surname"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#4793e3;\">First Name</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#4793e3;\">Last Name</span></p></body></html>"))
        self.firstname_2.setPlaceholderText(_translate("MainWindow", "Name"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#4793e3;\">Middle Name</span></p></body></html>"))
        self.login.setTabText(self.login.indexOf(self.tab_2), _translate("MainWindow", "Sign up"))

    def gotoSecond(self) :
        import sys
        self.app1 = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Frame1()
        self.ui.setupUi(Ui_Frame1)
        print("kopjdjgojkg")
        self.Ui_Frame1.show()
        
        sys.exit(app.exec_())
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    print("kopjdjgojkg")
    MainWindow.show()
    sys.exit(app.exec_())
