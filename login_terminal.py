import sys
from os import path
from tkinter.tix import NoteBook
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QMessageBox, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.uic.properties import QtWidgets, QtCore, QtGui
from pathlib import Path
from user_add_note import Add_Note_Window
from singining_up import Signup_Window
from main import Forgo_Pass_Window



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.new_signup_window = None
        self.new_forgo_pass_window = None
        self.note_window = None

        # ====== window properties ======
        self.setWindowTitle("Login")
        self.resize(710, 632)
        self.setStyleSheet("background-color:#black;")

        self.login_label = QLabel(self)
        self.login_label.move(100, 100)
        self.login_label.setText("Log In")
        self.login_label.setStyleSheet("font-size:24px")

        self.email_input = QLineEdit(self)
        self.email_input.move(100, 170)
        self.email_input.resize(260, 45)
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet(
            "background:#ffffff; border:1px solid #a9a9a9;border-radius:3px;font-size:18px;")
        self.email_input.setFocus()

        self.password_input = QLineEdit(self)
        self.password_input.move(100, 250)
        self.password_input.resize(260, 45)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setStyleSheet(
            "background:#ffffff; border:1px solid #a9a9a9;border-radius:3px;font-size:18px;")
        self.password_input.setFocus()

        self.button_1 = QPushButton("Log In", self)
        self.button_1.move(100, 330)
        self.button_1.resize(190, 40)
        self.button_1.setStyleSheet("background:#CBC3E3; font-size:19px; color:#ffffff; border-radius:3px;")
        self.button_1.clicked.connect(self.login_action)

        self.button_2 = QPushButton("Sign Up", self)
        self.button_2.move(360, 330)
        self.button_2.resize(190, 40)
        self.button_2.setStyleSheet("background:#CBC3E3; font-size:19px; color:#ffffff; border-radius:3px;")
        self.button_2.clicked.connect(lambda: self.new_signup_window())

        self.button_3 = QPushButton("Forgot Password", self)
        self.button_3.move(100, 410)
        self.button_3.resize(190, 40)
        self.button_3.setStyleSheet("background:#CBC3E3; font-size:19px; color:#ffffff; border-radius:3px;")
        self.button_3.clicked.connect(self.create_forgot_password_window)

        self.alert_message = QMessageBox()

        self.email_input_value = ""
        self.password_input_value = ""
        
    def create_signup_window(self):
        self.new_signup_window = Signup_Window()
        self.new_signup_window.show()
    def create_forgot_password_window(self):
           self.new_forgo_pass_window = Forgo_Pass_Window()
           self.new_forgo_pass_window.show()

    def login_action(self):
        # ====== error logs ======
        self.error_flag = False
        self.null_error = False
        self.authentication_error = True
        self.file_error = False
        self.error = ""

        self.user_data_file = None
        self.append_file = None
        self.read_file = None
        self.file_data = None
        self.data_line_split = None
        self.create_file = None

        self.email_input_value = None
        self.name_input_value = None
        self.password_input_value = None

        self.counter_one = None
        self.counter_two = None

        # ====== login data ======
        self.user_name = ""
        self.user_email = ""

        # ====== input value ======
        self.email_input_value = self.email_input.text()
        self.password_input_value = self.password_input.text()

        # ====== trim value ======
        self.email_input_value = self.email_input_value.strip()
        self.password_input_value = self.password_input_value.strip()

        if (self.email_input_value == "") or (self.password_input_value == ""):
            self.error_flag = True
            self.null_error = True

        if not self.null_error:
            if Path("user_data.txt").exists():
                with open(Path("user_data.txt"), 'r') as self.read_file:
                    self.file_data = self.read_file.read().replace('\n', '')
                    self.file_data = self.file_data.split(';;')
                    self.file_data = self.file_data[:-1]
                    for self.counter_one in self.file_data:
                        self.data_line_split = self.counter_one.split(',,')
                        if self.data_line_split[0] == self.email_input_value:
                            if self.data_line_split[1] == self.password_input_value:
                                self.authentication_error = False
                                self.user_email = self.data_line_split[0]
                                self.user_name = self.data_line_split[2]
                                break
                # ====== switching the error flag status ======
                if self.authentication_error:
                    self.error_flag = True
                else:
                     self.error_flag = False
            # ====== creating the file ======
            else:
                self.create_file = open("user_data.txt", "w")
                self.create_file.write("")
                self.file_error = True
                self.error_flag = True


        if self.error_flag:
            if self.authentication_error:
                self.error = "Incorrect email or password"
            if self.null_error:
                self.error = "Please enter your email and password"
            if self.file_error:
                self.error = "Something went wrong"

            self.alert_message.setText(self.error)
            self.alert_message.setWindowTitle("Error")
            self.alert_message.exec()
        else:
            self.alert_message.setText("Welcome " + self.user_name)
            self.alert_message.setWindowTitle("Success")
            self.close()
         #   self.note_window = Note_Window(self.user_email, self.user_name)
            self.note_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Window()
    gui.show()
    app.exec_()
