import sys
from tkinter import messagebox
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import json


database = json.load(open('database.json','r'))
print(database.keys())


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("new.ui",self)
        self.loginbutton.clicked.connect(self.loginFunc)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.create)


    def loginFunc(self):
        email = self.email.text()
        password = self.password.text()
        if email in database.keys():
            if password == database[email]:
                print("Welcome to the dashboard!")
                self.dashboard()
            else:
                print("password doesn't matches")
        else:
            messageBox = QMessageBox()
            messageBox.setIcon(QMessageBox.Warning)

            messageBox.setText("Email doesn't exists in our system.")
            messageBox.setWindowTitle("Error")
            messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)


            messageBox.exec()
            print("Email doesn't matches")


    
    def create(self):
        createacc = SignUp()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def dashboard(self):
        dash = DashBoard()
        widget.addWidget(dash)
        widget.setCurrentIndex(widget.currentIndex()+1)
    




class SignUp(QMainWindow):
    def __init__(self):
        super(SignUp, self).__init__()
        loadUi('signup.ui',self)
        self.signupbutton.clicked.connect(self.signup)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginbutton.clicked.connect(self.login)


    
    def signup(self):
        email = self.email.text()
        if self.password.text() == self.repassword.text():
            password = self.password.text()
            print("Success Login", email,'with password', password)
            messageBox = QMessageBox()
            messageBox.setIcon(QMessageBox.Information)

            messageBox.setText("SignUp done. You can go and login now")
            messageBox.setWindowTitle("Success")
            messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            messageBox.exec()
            self.login()
        else:
            print("Password doesn't match!")
    
    def login(self):
        loginacc = Login()
        widget.addWidget(loginacc)
        widget.setCurrentIndex(widget.currentIndex()+1)


class DashBoard(QMainWindow):
    def __init__(self):
        super(DashBoard, self).__init__()
        loadUi('dashboard.ui',self)
        self.codebutton.clicked.connect(self.code)
        self.youtubebutton.clicked.connect(self.youtube)
        self.timebutton.clicked.connect(self.time)
        self.logoutbutton.clicked.connect(self.login)
        
    def code(self):
        print("Opening Code")
    def youtube(self):
        print("Opening Youtube")

    def time(self):
        print("Time is")

    def login(self):
        loginacc = Login()
        widget.addWidget(loginacc)
        widget.setCurrentIndex(widget.currentIndex()+1)





app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(490)
widget.setFixedHeight(539)
widget.show()
app.exec_()