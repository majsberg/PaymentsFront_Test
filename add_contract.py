from datetime import date, datetime

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from ui.add_contract import Ui_Dialog
from User import User
from api_requests.api_requests import post_contract


class AddContract(QtWidgets.QDialog):

    def __init__(self):  # credentials, apartment_id
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.initSignals()
        self.user = User()
        # self.credentials = credentials
        # self.apartment_id = apartment_id

        self.ui.dateEdit_date.setDate(date.today())

    def initSignals(self):
        self.ui.buttonBox.accepted.connect(self.onPushButtonOK)

    def onPushButtonOK(self):

        status = post_contract(self.user.credentials, self.ui.lineEdit_number.text(),
                               self.ui.dateEdit_date.dateTime().toString('yyyy-MM-dd'),
                               self.ui.comboBox_provider.currentText(), self.ui.comboBox_type.currentText(),
                               self.user.apartments)
        print(type(self.user.apartments))
        if status == 201:
            QMessageBox.information(self, f'Статус: {status}', f'Данные добавлены')
        else:
            QMessageBox.warning(self, f'Ошибка. Статус: {status}', f'Данные не внесены')
