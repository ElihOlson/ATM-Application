import csv

from PyQt6.QtWidgets import QMainWindow, QLineEdit
from gui import *


class Logic(QMainWindow, Ui_ATM):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.input_pin.setEchoMode(QLineEdit.EchoMode.Password)

        self.button_login.clicked.connect(lambda: self.login())
        self.button_signup.clicked.connect(lambda: self.signup())
        self.button_enter.clicked.connect(lambda: self.enter())
        self.button_exit.clicked.connect(lambda: self.exit())

        self.hidden()

        self.radio_withdrawl.setChecked(True)

        self.logged_in_first = None
        self.logged_in_last = None
        self.logged_in_pin = None

    def visible(self):
        self.label_question.setHidden(False)
        self.radio_withdrawl.setHidden(False)
        self.radio_deposite.setHidden(False)
        self.label_amount.setHidden(False)
        self.input_amount.setHidden(False)
        self.button_enter.setHidden(False)
        self.button_exit.setHidden(False)

    def hidden(self):
        self.label_question.setHidden(True)
        self.radio_withdrawl.setHidden(True)
        self.radio_deposite.setHidden(True)
        self.label_amount.setHidden(True)
        self.input_amount.setHidden(True)
        self.button_enter.setHidden(True)
        self.button_exit.setHidden(True)

    def login(self):
        try:
            first = self.input_first.text().strip()
            last = self.input_last.text().strip()
            pin = self.input_pin.text().strip()

            #checks for an existing account, then either logs in or states if the customer can't be found
            with open('info.csv', 'r', newline='') as csvfile:
                content = csv.reader(csvfile, delimiter=',')
                for row in content:
                    if len(row) >= 3 and row[0] == first and row[1] == last and row[2] == pin:
                        self.label_change.setText(f'Login Successful. Welcome back {first} {last}!')
                        self.visible()
                        balance = float(row[3])
                        self.label_balance.setText(f'Balance: ${balance}')

                        self.logged_in_first = first
                        self.logged_in_last = last
                        self.logged_in_pin = pin

                        return
            self.label_change.setText('Customer Not Found')
        except Exception as e:
            self.label_change.setText(f'An unexpected error occurred:\n {str(e)}')

    def signup(self):
        try:
            first = self.input_first.text().strip()
            last = self.input_last.text().strip()
            pin = self.input_pin.text().strip()

            #Ensures that the PIN entered is at least 4 digits
            if not pin.isdigit() or len(pin) != 4:
                raise ValueError('PIN must be a 4-digit number!')

            #checks for an existing account
            with open('info.csv', 'r', newline='') as csvfile:
                content = csv.reader(csvfile, delimiter=',')
                for row in content:
                    if len(row) >= 3 and first == row[0].strip() and last == row[1].strip() and pin == row[2].strip():
                        raise ValueError('Account already exists! Please try login.')


            #adds a new account if none was found
            with open('info.csv', 'a', newline='') as csvfile:
                content = csv.writer(csvfile, delimiter=',')
                if first == '' or last == '' or pin == '':
                    raise ValueError('NOT ALL ENTRIES HAVE BEEN FILLED')
                else:
                    self.logged_in_first = first
                    self.logged_in_last = last
                    self.logged_in_pin = pin
                    self.visible()
                    content.writerow([first, last, pin, 0.0])
                    self.label_change.setText(f'Welcome to our bank {first} {last}!')
                    balance = float(row[3])
                    self.label_balance.setText(f'Balance: ${balance}')

        except ValueError as e:
            self.label_change.setText(str(e))
        except Exception as e:
            self.label_change.setText(f'An unexpected error occurred:\n {str(e)}')

    def enter(self):
        if not self.logged_in_first or not self.logged_in_last or not self.logged_in_pin:
            self.label_balance.setText('No user is logged in. Please log in.')
            return

        try:
            amount = float(self.input_amount.text().strip())
            updated_row = []
            user_found = False

            with open('info.csv', 'r', newline='') as csvfile:
                content = csv.reader(csvfile, delimiter=',')
                for row in content:
                    if len(row) >= 4 and row[0] == self.logged_in_first and row[1] == self.logged_in_last and row[2] == self.logged_in_pin:
                        balance = float(row[3])
                        if self.radio_withdrawl.isChecked() and balance >= 0:
                            if amount > balance:
                                self.label_balance.setText(f'Please enter a valid amount.\nBalance: ${balance}')
                            else:
                                balance -= amount
                                row[3] = str(balance)
                                self.label_balance.setText(f'Balance: ${balance}')

                        elif self.radio_deposite.isChecked():
                            balance += amount
                            row[3] = str(balance)
                            self.label_balance.setText(f'Balance: ${balance}')

                        user_found = True

                    updated_row.append(row)

            if not user_found:
                self.label_balance.setText('User account not found.')

            with open('info.csv', 'w', newline='') as csvfile:
                content = csv.writer(csvfile, delimiter=',')
                content.writerows(updated_row)

        except ValueError:
            self.label_balance.setText('Please enter a valid amount.')

        except Exception as e:
            self.label_balance.setText(f'An unexpected error occurred:\n {str(e)}')

    def exit(self):
        #This function just clears the information so the user can log into a new account

        self.input_first.clear()
        self.input_last.clear()
        self.input_pin.clear()
        self.label_change.clear()
        self.radio_withdrawl.setChecked(True)
        self.input_amount.clear()
        self.label_balance.clear()

        self.hidden()

        self.logged_in_first = None
        self.logged_in_last = None
        self.logged_in_pin = None

