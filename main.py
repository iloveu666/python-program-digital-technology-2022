import sys
from os import path

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QMessageBox, QMainWindow, \
    QTextBrowser
from PyQt5.QtGui import QIcon
from PyQt5.uic.properties import QtWidgets, QtCore, QtGui
from pathlib import Path
import manual

class Forgo_Pass_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # ====== window properties ======
        self.setWindowTitle("Forgot Password ? ")
        self.resize(600, 500)
        self.setStyleSheet("backound-color: #ffffff")

        self.reset_label = QLabel(self)
        self.reset_label.move(100, 110)
        self.reset_label.setText("Find Password")
        self.reset_label.setFixedWidth(400)
        self.reset_label.setStyleSheet("font-size:24px;")

        #  ====== email, name and password input ======
        self.email_input = QLineEdit(self)
        self.email_input.move(100, 170)
        self.email_input.resize(260, 45)
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet(
            "background:#ffffff; border:1px solid #a9a9a9;border-radius:3px;font-size:18px;")
        self.email_input.setFocus()

        self.button_1 = QPushButton("Find", self)
        self.button_1.move(100, 300)
        self.button_1.resize(190, 40)
        self.button_1.setStyleSheet("background:#008b8b; font-size:19px; color:#ffffff; border-radius:3px;")
        self.button_1.clicked.connect(self.find_account)

        # ======  initialize alert message box ======
        self.alert_message = QMessageBox()

    def find_account(self):
        # ====== get input values ======
        self.error = ""
        self.error_flag = False
        self.null_error = False
        self.user_found_error = True
        self.email_validation_error = False
        self.valid_email = None

        self.user_name = ""
        self.user_password = ""
        self.email_input_value = self.email_input.text()
        self.email_input_value = self.email_input_value.strip()

        # ====== detect any errors ======
        if self.email_input_value == "":
            self.error_flag = True
            self.null_error = True

        #  ====== email validation ======
        self.valid_email = manual.email_validation()(self.email_input_value)
        if not self.valid_email:
            self.error_flag = True
            self.email_validation_error = True

        # ====== check if email exists or user_data file exists ======
        if path.exists("user_data.txt"):
            with open(Path("user_data.txt"), 'r') as self.read_file:
                self.file_data = self.read_file.read().replace('\n', '')
                self.file_data = self.file_data.split(';;')
                self.file_data = self.file_data[:-1]
                for self.counter_one in self.file_data:
                    self.data_line_split = self.counter_one.split(',,')
                    if self.data_line_split[0] == self.email_input_value:
                        self.user_found_error = False
                        self.user_password = self.data_line_split[1]
                        self.user_name = self.data_line_split[2]
                        break

            if self.user_found_error:
                self.error_flag = True

            # ====== defining errors ======
            if self.error_flag:
                if self.user_found_error:
                    self.error = "No account with this email"
                if self.email_validation_error:
                    self.error = "Email address is not valid"
                if self.null_error:
                    self.error = "Please enter your email address"
                self.alert_message.setText(self.error)
                self.alert_message.setWindowTitle("Error")
                self.alert_message.exec()

            else:
                self.alert_message.setText("Hi " + self.user_name + '! your password is ' + self.user_password)
                self.alert_message.setWindowTitle("Success")
                self.alert_message.exec()
                self.close()

        else:
            self.error = "No account with this email"
            self.alert_message.setWindowTitle("Error")
            self.alert_message.exec()
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Forgo_Pass_Window()
    window.show()
    app.exec_()
