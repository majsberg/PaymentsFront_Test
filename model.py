from PySide6.QtCore import QAbstractTableModel
from PySide6.QtCore import Qt
from api_requests.api_requests import get_contracts
from datetime import datetime
from User import User


class Model(QAbstractTableModel):

    def __init__(self):
        super().__init__()
        self.user = User()
        self.user.contracts = get_contracts(self.user.credentials)
        print(self.user.contracts)
        if len(self.user.contracts) > 0:  # проверка на пустой список договоров
            self.new_data = self.cooking_data(self.user.contracts)
            self.work_status = True
        else:
            self.work_status = False  # чтобы модель не уходила в ошибку и не обрабатывала данных

    def updated_data(self):
        self.beginResetModel()
        self.user.contracts = get_contracts(self.user.credentials)
        if len(self.user.contracts) > 0:
            self.work_status = True
            self.new_data = self.cooking_data(self.user.contracts)
        self.endResetModel()

    def cooking_data(self, data):
        new_data = []
        for each in data:
            add_data = []
            for key in each:
                if key in ["id", "name", "date", "provider", "type", "created_at", "updated_at"]:
                    if key == "date":
                        date = datetime.fromisoformat(each.get(key))
                        dt = date.strftime('%d.%m.%Y')
                        add_data.append(dt)
                    elif key in ["created_at", "updated_at"]:
                        date = datetime.fromisoformat(each.get(key))
                        dt = date.strftime('%d.%m.%Y %H:%M:%S')
                        add_data.append(dt)
                    else:
                        add_data.append(each.get(key))
            new_data.append(add_data)
        return new_data

    def rowCount(self, parent=None):
        if self.work_status is True:
            return len(self.new_data)

    def columnCount(self, parent=None):
        if self.work_status is True:
            return len(self.new_data[0])

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if self.work_status is True:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.new_data[index.row()][index.column()]

    def headerData(self, section, orientation, role=Qt):
        if self.work_status is True:
            if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
                return ["id", "№ договора", "Дата договора", "Поставщик", "Тип", "Дата создания", "Дата изменения"][section]
            return None
