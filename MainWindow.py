from PySide6.QtWidgets import QMainWindow, QMessageBox
from MainMenu import MainMenu
from mainWidget import MainWidget


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)

        main_menu.about.triggered.connect(self.aboutTriggered)  # сигнал для нажатия по пункту "О программе"

        mainWidget = MainWidget()
        self.setCentralWidget(mainWidget)


    def aboutTriggered(self):  # слот для отображения информации в окне "О программе"
        title = 'Коммуналка'
        text = ('Программа для учета договоров\n' +
                'с энергоснабжающими компаниями')
        QMessageBox.about(self, title, text)
