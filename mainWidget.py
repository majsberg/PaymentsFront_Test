from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox, QDialogButtonBox

from ui.main_widget import Ui_Form
from User import User
from api_requests.api_requests import get_apartments, delete_contract
from model import Model
from add_apartment import AddApartment
from add_contract import AddContract


class MainWidget(QtWidgets.QWidget):

    def __init__(self): # credentials, user_id, username):
        super().__init__()

        # self.user = User(credentials, user_id, username)
        self.user = User()
        print(self.user.credentials)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()


        print(f'Новый user-объект из класса ApartmentInfo: {self.user}')
        print(f'credentials нового объекта из класса ApartmentInfo: {self.user.credentials}')

        self.ui.lineEditName_4.setText(self.user.username)

        apartment_info = get_apartments(self.user.credentials)
        if apartment_info:
            self.ui.lineEditApartment_4.setText(apartment_info[0]['address'])
            self.ui.pushButtonAddApartment.setDisabled(True)
            self.user.apartments = apartment_info[0]['id']  # для упрощения берем только первую квартиру
            print(f'User-apartment: {self.user.apartments}')

            self.model = Model()
            self.ui.tableViewContracts.setModel(self.model)
            self.ui.tableViewContracts.horizontalHeader().setSectionResizeMode(
                QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            self.ui.tableViewContracts.show()
            self.ui.pushButtonDelContract.setDisabled(True)

        else:
            self.ui.pushButtonAddApartment.setDisabled(False)
            self.ui.pushButtonAddContract.setDisabled(True)
            self.ui.pushButtonDelContract.setDisabled(True)

    def add(self):
        add_contract = AddContract()  # self.user.credentials, self.user.apartments)
        if add_contract.exec():
            self.model.updated_data()

    def initSignals(self):
        self.ui.pushButtonAddApartment.clicked.connect(self.addApartment)
        self.ui.pushButtonAddContract.clicked.connect(self.add)
        self.ui.tableViewContracts.clicked.connect(self.onTableViewContractsClicked)
        self.ui.pushButtonDelContract.clicked.connect(self.delete_contract)

    def onTableViewContractsClicked(self):
        # print(self.ui.tableViewContracts.currentIndex().row())
        row = self.ui.tableViewContracts.currentIndex().row()  # индекс строки с выделенной ячейкой
        contract_id = self.ui.tableViewContracts.model().index(row, 0).data()
        self.contract_id = contract_id
        self.ui.pushButtonDelContract.setEnabled(True)
        print(self.contract_id)
        return contract_id
        print("TableViewContracts.model.index.index(row, 0).data -> {}".format(self.ui.tableViewContracts.model().index(row, 0).data()))

    def delete_contract(self):
        delete_msg = QMessageBox.question(self, "Удаление договора", "Вы действительно хотите удалить выбранный договор?")
        if delete_msg.Yes:
            status = delete_contract(self.user.credentials, self.contract_id)
            if status == 204:
                self.model.updated_data()
                QMessageBox.information(self, f'Статус: {status}', f'Договор удален')
                self.ui.pushButtonDelContract.setEnabled(False)
            else:
                QMessageBox.warning(self, f'Ошибка. Статус: {status}', f'Произошла ошибка')
                self.ui.pushButtonDelContract.setEnabled(False)

    def addApartment(self):
        add_apartment = AddApartment()
        add_apartment.exec_()
