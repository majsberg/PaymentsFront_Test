# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_contract.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(270, 180)
        Dialog.setMinimumSize(QSize(270, 180))
        Dialog.setMaximumSize(QSize(270, 180))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_dat = QLabel(Dialog)
        self.label_dat.setObjectName(u"label_dat")

        self.gridLayout.addWidget(self.label_dat, 2, 0, 1, 1)

        self.dateEdit_date = QDateEdit(Dialog)
        self.dateEdit_date.setObjectName(u"dateEdit_date")
        self.dateEdit_date.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.dateEdit_date.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.dateEdit_date.setCalendarPopup(True)
        self.dateEdit_date.setCurrentSectionIndex(0)
        self.dateEdit_date.setDate(QDate(2001, 1, 1))

        self.gridLayout.addWidget(self.dateEdit_date, 2, 1, 1, 1)

        self.label_provider = QLabel(Dialog)
        self.label_provider.setObjectName(u"label_provider")

        self.gridLayout.addWidget(self.label_provider, 1, 0, 1, 1)

        self.comboBox_type = QComboBox(Dialog)
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.setObjectName(u"comboBox_type")

        self.gridLayout.addWidget(self.comboBox_type, 3, 1, 1, 1)

        self.label_number = QLabel(Dialog)
        self.label_number.setObjectName(u"label_number")

        self.gridLayout.addWidget(self.label_number, 0, 0, 1, 1)

        self.lineEdit_number = QLineEdit(Dialog)
        self.lineEdit_number.setObjectName(u"lineEdit_number")

        self.gridLayout.addWidget(self.lineEdit_number, 0, 1, 1, 1)

        self.comboBox_provider = QComboBox(Dialog)
        self.comboBox_provider.addItem("")
        self.comboBox_provider.addItem("")
        self.comboBox_provider.addItem("")
        self.comboBox_provider.addItem("")
        self.comboBox_provider.addItem("")
        self.comboBox_provider.addItem("")
        self.comboBox_provider.setObjectName(u"comboBox_provider")

        self.gridLayout.addWidget(self.comboBox_provider, 1, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 2)

        self.label_type = QLabel(Dialog)
        self.label_type.setObjectName(u"label_type")

        self.gridLayout.addWidget(self.label_type, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.comboBox_type.setCurrentIndex(-1)
        self.comboBox_provider.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.label_dat.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.label_provider.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a", None))
        self.comboBox_type.setItemText(0, QCoreApplication.translate("Dialog", u"\u041f\u0440\u0435\u0434\u043e\u043f\u043b\u0430\u0442\u0430", None))
        self.comboBox_type.setItemText(1, QCoreApplication.translate("Dialog", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u043f\u043b\u0430\u0442\u0435\u0436", None))
        self.comboBox_type.setItemText(2, QCoreApplication.translate("Dialog", u"\u041f\u043e\u0441\u0442\u043e\u043f\u043b\u0430\u0442\u0430", None))

        self.label_number.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.comboBox_provider.setItemText(0, QCoreApplication.translate("Dialog", u"\u0423\u043f\u0440\u0430\u0432\u043b\u044f\u044e\u0449\u0430\u044f \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044f", None))
        self.comboBox_provider.setItemText(1, QCoreApplication.translate("Dialog", u"\u041c\u041e\u042d\u041a", None))
        self.comboBox_provider.setItemText(2, QCoreApplication.translate("Dialog", u"\u041c\u043e\u0441\u0432\u043e\u0434\u043e\u043a\u0430\u043d\u0430\u043b", None))
        self.comboBox_provider.setItemText(3, QCoreApplication.translate("Dialog", u"\u041c\u043e\u0441\u044d\u043d\u0435\u0440\u0433\u043e\u0441\u0431\u044b\u0442", None))
        self.comboBox_provider.setItemText(4, QCoreApplication.translate("Dialog", u"\u0415\u041f\u0414", None))
        self.comboBox_provider.setItemText(5, QCoreApplication.translate("Dialog", u"\u0418\u043d\u0442\u0435\u0440\u043d\u0435\u0442", None))

        self.comboBox_provider.setCurrentText("")
        self.label_type.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f", None))
    # retranslateUi

