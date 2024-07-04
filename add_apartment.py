from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from ui.add_apartment import Ui_Form
from User import User
from api_requests.api_requests import post_apartments


class AddApartment(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

        self.user = User()

        # self.apartmentName = self.ui.lineEditName.text()
        # self.apartmentAddress = self.ui.lineEditAddress.text()

    def initSignals(self):
        self.ui.pushButtonAddApartmentForm.clicked.connect(self.onPushButtonAddApartmentForm)

    def onPushButtonAddApartmentForm(self):

        status = post_apartments(self.user.credentials, self.user.user_id, self.ui.lineEditName.text(), self.ui.lineEditAddress.text())
        if status == 201:
            QMessageBox.information(self, f'Статус: {status}', f'Квартира добавлена')
        else:
            QMessageBox.warning(self, f'Ошибка. Статус: {status}', f'Квартира не добавлена')
        self.close()
