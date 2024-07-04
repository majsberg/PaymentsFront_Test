# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainView.ui'
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
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(987, 584)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setUnderline(False)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelName = QLabel(self.groupBox)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(False)
        self.labelName.setFont(font1)

        self.horizontalLayout.addWidget(self.labelName)

        self.lineEditName = QLineEdit(self.groupBox)
        self.lineEditName.setObjectName(u"lineEditName")
        self.lineEditName.setMaximumSize(QSize(115, 16777215))
        font2 = QFont()
        font2.setItalic(True)
        font2.setUnderline(False)
        self.lineEditName.setFont(font2)
        self.lineEditName.setReadOnly(True)
        self.lineEditName.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.lineEditName)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.labelApartment = QLabel(self.groupBox)
        self.labelApartment.setObjectName(u"labelApartment")
        self.labelApartment.setMaximumSize(QSize(16777215, 16777215))
        self.labelApartment.setFont(font1)

        self.horizontalLayout.addWidget(self.labelApartment)

        self.lineEditApartment = QLineEdit(self.groupBox)
        self.lineEditApartment.setObjectName(u"lineEditApartment")
        self.lineEditApartment.setMinimumSize(QSize(350, 0))
        self.lineEditApartment.setMaximumSize(QSize(16777215, 16777215))
        self.lineEditApartment.setFont(font2)
        self.lineEditApartment.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEditApartment)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(47, 26, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButtonAdd = QPushButton(self.groupBox)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAdd.sizePolicy().hasHeightForWidth())
        self.pushButtonAdd.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setBold(False)
        font3.setUnderline(False)
        self.pushButtonAdd.setFont(font3)

        self.horizontalLayout_4.addWidget(self.pushButtonAdd)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidgetContacts = QTableWidget(self.groupBox_2)
        if (self.tableWidgetContacts.columnCount() < 4):
            self.tableWidgetContacts.setColumnCount(4)
        font4 = QFont()
        font4.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.tableWidgetContacts.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.tableWidgetContacts.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.tableWidgetContacts.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self.tableWidgetContacts.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidgetContacts.setObjectName(u"tableWidgetContacts")
        self.tableWidgetContacts.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidgetContacts.sizePolicy().hasHeightForWidth())
        self.tableWidgetContacts.setSizePolicy(sizePolicy1)
        self.tableWidgetContacts.setMinimumSize(QSize(0, 0))
        self.tableWidgetContacts.setAlternatingRowColors(False)
        self.tableWidgetContacts.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidgetContacts.horizontalHeader().setHighlightSections(True)
        self.tableWidgetContacts.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidgetContacts.verticalHeader().setVisible(True)
        self.tableWidgetContacts.verticalHeader().setCascadingSectionResizes(False)

        self.horizontalLayout_5.addWidget(self.tableWidgetContacts)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(270, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(90, 16777215))
        self.label.setFont(font4)

        self.horizontalLayout_6.addWidget(self.label)

        self.lineEdit = QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(130, 16777215))
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(90, 16777215))
        self.label_2.setFont(font4)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.groupBox_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(130, 16777215))
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.lineEdit_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(90, 16777215))
        self.label_3.setFont(font4)

        self.horizontalLayout_8.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.groupBox_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(130, 16777215))
        self.lineEdit_3.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.lineEdit_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_5.addWidget(self.groupBox_4)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(self.groupBox_3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_3.addWidget(self.tableWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setMinimumSize(QSize(0, 32))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(0, 32))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)
        self.pushButton_4.setMinimumSize(QSize(0, 32))

        self.verticalLayout_2.addWidget(self.pushButton_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addWidget(self.groupBox_3)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 987, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043c\u0443\u043d\u0430\u043b\u043a\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u0435", None))
        self.labelName.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c: ", None))
        self.lineEditName.setText("")
        self.labelApartment.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u044b:", None))
        self.lineEditApartment.setText("")
        self.pushButtonAdd.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440\u044b", None))
        ___qtablewidgetitem = self.tableWidgetContacts.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a", None));
        ___qtablewidgetitem1 = self.tableWidgetContacts.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u2116 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None));
        ___qtablewidgetitem2 = self.tableWidgetContacts.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None));
        ___qtablewidgetitem3 = self.tableWidgetContacts.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \n"
" \u0434\u043e\u0433\u043e\u0432\u043e\u0440", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u043b\u0430\u0442\u0435\u0436\u0435", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0442\u0435\u0436\u0438", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

