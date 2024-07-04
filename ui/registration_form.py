# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration_form.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(210, 220)
        Form.setMaximumSize(QSize(210, 220))
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelLogin = QLabel(Form)
        self.labelLogin.setObjectName(u"labelLogin")

        self.verticalLayout.addWidget(self.labelLogin)

        self.lineEditLoginR = QLineEdit(Form)
        self.lineEditLoginR.setObjectName(u"lineEditLoginR")

        self.verticalLayout.addWidget(self.lineEditLoginR)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelPassword = QLabel(Form)
        self.labelPassword.setObjectName(u"labelPassword")

        self.verticalLayout_2.addWidget(self.labelPassword)

        self.lineEditPasswordR = QLineEdit(Form)
        self.lineEditPasswordR.setObjectName(u"lineEditPasswordR")
        self.lineEditPasswordR.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.lineEditPasswordR)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelPassword2 = QLabel(Form)
        self.labelPassword2.setObjectName(u"labelPassword2")

        self.verticalLayout_3.addWidget(self.labelPassword2)

        self.lineEditPassword2R = QLineEdit(Form)
        self.lineEditPassword2R.setObjectName(u"lineEditPassword2R")
        self.lineEditPassword2R.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_3.addWidget(self.lineEditPassword2R)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonAddUser = QPushButton(Form)
        self.pushButtonAddUser.setObjectName(u"pushButtonAddUser")

        self.horizontalLayout.addWidget(self.pushButtonAddUser)

        self.pushButtonCancel = QPushButton(Form)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        self.pushButtonCancel.setCheckable(False)

        self.horizontalLayout.addWidget(self.pushButtonCancel)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.labelLogin.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.lineEditLoginR.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d", None))
        self.labelPassword.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.lineEditPasswordR.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.labelPassword2.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.lineEditPassword2R.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u043e\u0432\u0442\u0440\u043e\u043d\u043e \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButtonAddUser.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

