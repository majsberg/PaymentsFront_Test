from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox

from ui.login_form import Ui_Form
from api_requests.api_requests import get_user
from User import User


import base64


class LoginPassword(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.credentials = None
        self.answer = None
        self.user_id = None
        self.username = None

        self.status = False

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

        self.ui.lineEditLogin.setPlaceholderText("Введите логин")
        self.ui.lineEditPassword.setPlaceholderText("Введите пароль")

    def initSignals(self):
        self.ui.pushButton.clicked.connect(self.onPushButtonClicked)
        self.ui.pushButtonRegestry.clicked.connect(self.onPushButtonRegestryClicked)

    def onPushButtonClicked(self):
        login = self.ui.lineEditLogin.text()
        password = self.ui.lineEditPassword.text()
        self.credentials = base64.b64encode(f'{login}:{password}'.encode('utf-8')).decode('utf-8')
        self.answer = get_user(self.credentials)
        try:
            self.user_id = self.answer[0]['id']
            self.username = self.answer[0]['username']
            self.close()
            print(self.credentials)
            print(type(self.credentials))
            # print(self.user_id)
            self.status = True
            current_user = User()
            current_user.username = self.username
            current_user.user_id = self.user_id
            current_user.credentials = self.credentials
        except:
            QMessageBox.warning(self, "Ошибка", f'Неправильный логин или пароль')

    def onPushButtonRegestryClicked(self):
        self.close()
        # self.status = False
