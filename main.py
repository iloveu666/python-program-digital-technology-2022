import sys
from pathlib import Path
import os.path
from os import path
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QMessageBox, QMainWindow
from PyQt5.uic.properties import QtWidgets, QtCore, QtGui
from pathlib import Path 

# ==== manual modules ===== 
import manual 

class Signup_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # ====== window properties ======
        self.setWindowTitle("Signing Up!")
        self.resize(610, 532)
        self.setStyleSheet("background-color: #white")

        self.signup_label = QLabel(self)
        self.signup_label.move(100, 70)
        self.signup_label.setText("Sign Up")
        self.signup_label.setStyleSheet("font-size:24px")

        # ====== email, name and password input ======
        self.email_input = QLineEdit(self)
        self.email_input.move(100, 140)
        self.email_input.resize(260, 45)
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet(
            "background:#CBC3E3; border:1px solid #a9a9a9;border-radius:3px;font-size:18px;")
        self.email_input.setFocus()

        self.name_input = QLineEdit(self)
        self.name_input.move(100, 220)
        self.name_input.resize(260, 45)
        self.name_input.setPlaceholderText("Name")
        self.name_input.setStyleSheet(
            "background:#CBC3E3; border:1px solid #CBC3E3;border-radius:3px;font-size:18px;")
        self.name_input.setFocus()

        self.password_input = QLineEdit(self)
        self.password_input.move(100, 300)
        self.password_input.resize(260, 45)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setStyleSheet(
            "background:#CBC3E3; border:1px solid #a9a9a9;border-radius:3px;font-size:18px;")
        self.password_input.setFocus()

        self.button_1 = QPushButton("Click To Sign Up!", self)
        self.button_1.move(100, 370)
        self.button_1.resize(190, 40)
        self.button_1.setStyleSheet("background:#CBC3E3; font-size:19px; color:#ffffff;border-radius:3px;")
        self.button_1.clicked.connect(self.create_account)

        # ====== alert message box ======
        self.alert_message = QMessageBox()


    def create_account(self):
        #  ====== geting the input values ======
        self.error_flag = False
        self.null_error = False
        self.email_exists_error = False
        self.email_validation_error = False
        self.valid_email = None
        self.password_length_error = False

        self.email_input_value = self.email_input.text()
        self.name_input_value = self.name_input.text()
        self.password_input_value = self.password_input.text()

        # ====== trim value ======
        self.email_input_value = self.email_input_value.strip()
        self.name_input_value = self.name_input_value.strip()
        self.password_input_value = self.password_input_value.strip()

        # ====== detect errors ======
        if (self.email_input_value == "") or (self.name_input_value == "") or (self.password_input_value == ""):
            self.error_flag = True
            self.null_error = True

        # ====== email validation ======
        self.valid_email = manual.email_validation(self.email_input_value)
        if not self.valid_email:
            self.error_flag = True
            self.email_validation_error = True

        # ====== password length ======
        if len(self.password_input_value) < 6:
            self.error_flag = True
            self.password_length_error = True

        # ====== check if email exists or user_data file exists ======
        if path.exists("user_data.txt"):
            with open(Path("user_data.txt"), 'r') as self.read_file:
                self.file_data = self.read_file.read().replace('\n', '')
                self.file_data = self.file_data.split(';;')
                self.file_data = self.file_data[:-1]
                for self.counter_one in self.file_data:
                    self.data_line_split = self.counter_one.split(',,')
                    if self.data_line_split[0] == self.email_input_value:
                        self.error_flag = True
                        self.email_exists_error = True
                        break

        else:
            self.create_file = open("user_data.txt", "w")
            self.create_file.write("")

        # ====== define error sequence null error > valid email error > password length error > email exists error ======
        if self.error_flag:
            if self.email_exists_error:
                self.error = "This email address exists"
            if self.password_length_error:
                self.error = "Password must be at least 6 characters long"
            if self.email_validation_error:
                self.error = "Email address is not valid"
            if self.null_error:
                self.error = "Please enter all the fields"
            self.alert_message.setText(self.error)
            self.alert_message.setWindowTitle("Error")
        #  ====== if no error ======
        else:
            self.append_file = open('user_data.txt', 'a')
            self.append_file.write(self.email_input_value+',,' + self.password_input_value+',,' + self.name_input_value + ';;')
            self.append_file.close()
            self.alert_message.setText("Welcome " + self.name_input_value + " ! Your account has been created ! ☺️")

        self.alert_message.exec()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Signup_Window()
    window.show()
    app.exec_() 
