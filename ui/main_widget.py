# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(991, 345)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setUnderline(False)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.labelName_4 = QLabel(self.groupBox_2)
        self.labelName_4.setObjectName(u"labelName_4")
        self.labelName_4.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(False)
        self.labelName_4.setFont(font1)

        self.horizontalLayout_15.addWidget(self.labelName_4)

        self.lineEditName_4 = QLineEdit(self.groupBox_2)
        self.lineEditName_4.setObjectName(u"lineEditName_4")
        self.lineEditName_4.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setItalic(True)
        font2.setUnderline(False)
        self.lineEditName_4.setFont(font2)
        self.lineEditName_4.setReadOnly(True)
        self.lineEditName_4.setClearButtonEnabled(False)

        self.horizontalLayout_15.addWidget(self.lineEditName_4)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_15)

        self.horizontalSpacer_7 = QSpacerItem(44, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.labelApartment_4 = QLabel(self.groupBox_2)
        self.labelApartment_4.setObjectName(u"labelApartment_4")
        self.labelApartment_4.setMaximumSize(QSize(16777215, 16777215))
        self.labelApartment_4.setFont(font1)

        self.horizontalLayout_16.addWidget(self.labelApartment_4)

        self.lineEditApartment_4 = QLineEdit(self.groupBox_2)
        self.lineEditApartment_4.setObjectName(u"lineEditApartment_4")
        self.lineEditApartment_4.setMinimumSize(QSize(350, 0))
        self.lineEditApartment_4.setMaximumSize(QSize(16777215, 16777215))
        self.lineEditApartment_4.setFont(font2)
        self.lineEditApartment_4.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.lineEditApartment_4)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_8 = QSpacerItem(47, 26, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_8)

        self.pushButtonAddApartment = QPushButton(self.groupBox_2)
        self.pushButtonAddApartment.setObjectName(u"pushButtonAddApartment")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAddApartment.sizePolicy().hasHeightForWidth())
        self.pushButtonAddApartment.setSizePolicy(sizePolicy)
        self.pushButtonAddApartment.setFont(font1)

        self.horizontalLayout_17.addWidget(self.pushButtonAddApartment)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_17)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableViewContracts = QTableView(self.groupBox)
        self.tableViewContracts.setObjectName(u"tableViewContracts")

        self.horizontalLayout_2.addWidget(self.tableViewContracts)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButtonAddContract = QPushButton(self.groupBox)
        self.pushButtonAddContract.setObjectName(u"pushButtonAddContract")

        self.verticalLayout_2.addWidget(self.pushButtonAddContract)

        self.pushButtonDelContract = QPushButton(self.groupBox)
        self.pushButtonDelContract.setObjectName(u"pushButtonDelContract")

        self.verticalLayout_2.addWidget(self.pushButtonDelContract)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.groupBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u041a\u0432\u0430\u0440\u0442\u0438\u0440\u0430", None))
        self.labelName_4.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c: ", None))
        self.lineEditName_4.setText("")
        self.labelApartment_4.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441 \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u044b:", None))
        self.lineEditApartment_4.setText("")
        self.pushButtonAddApartment.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440\u044b", None))
        self.pushButtonAddContract.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \n"
" \u0434\u043e\u0433\u043e\u0432\u043e\u0440", None))
        self.pushButtonDelContract.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c\n"
" \u0434\u043e\u0433\u043e\u0432\u043e\u0440", None))
    # retranslateUi

