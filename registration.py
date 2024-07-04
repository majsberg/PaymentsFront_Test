from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox

from ui.registration_form import Ui_Form
from api_requests.api_requests import post_user


class Registration(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

        self.login = None
        self.password = None
        self.password_confirm = None

    def initSignals(self):
        self.ui.pushButtonAddUser.clicked.connect(self.registration)
        self.ui.pushButtonCancel.clicked.connect(self.cancel)

    def registration(self):
        self.login = self.ui.lineEditLoginR.text()
        self.password = self.ui.lineEditPasswordR.text()
        self.password_confirm = self.ui.lineEditPassword2R.text()

        self.login = self.login.strip()
        self.password = self.password.strip()
        self.password_confirm = self.password_confirm.strip()

        if self.password == self.password_confirm:
            status_code = post_user(self.login, self.password)
            if status_code == 201:
                QMessageBox.information(self, "Успех", f'Вы прошли регистрацию. \nВаш логин {self.login}')
            else:
                QMessageBox.warning(self, "Ошибка", f'Зарегистрироваться не удалось. \nСтатус ошибки: {status_code}')
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", f'Введенные пароли не совпадают')

    def cancel(self):
        self.close()