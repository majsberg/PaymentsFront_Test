# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_apartment.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(850, 52)
        Form.setMinimumSize(QSize(850, 0))
        Form.setMaximumSize(QSize(900, 60))
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelName = QLabel(Form)
        self.labelName.setObjectName(u"labelName")

        self.horizontalLayout_2.addWidget(self.labelName)

        self.lineEditName = QLineEdit(Form)
        self.lineEditName.setObjectName(u"lineEditName")
        self.lineEditName.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.lineEditName)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelAdress = QLabel(Form)
        self.labelAdress.setObjectName(u"labelAdress")

        self.horizontalLayout.addWidget(self.labelAdress)

        self.lineEditAddress = QLineEdit(Form)
        self.lineEditAddress.setObjectName(u"lineEditAddress")
        self.lineEditAddress.setMinimumSize(QSize(400, 0))

        self.horizontalLayout.addWidget(self.lineEditAddress)

        self.pushButtonAddApartmentForm = QPushButton(Form)
        self.pushButtonAddApartmentForm.setObjectName(u"pushButtonAddApartmentForm")

        self.horizontalLayout.addWidget(self.pushButtonAddApartmentForm)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u044b", None))
        self.labelName.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u044b:", None))
        self.labelAdress.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441 \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u044b: ", None))
        self.pushButtonAddApartmentForm.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

