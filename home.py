# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 235)
        Dialog.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/경기지방남부경찰청 아이콘.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.tab_main = QtWidgets.QTabWidget(Dialog)
        self.tab_main.setGeometry(QtCore.QRect(10, 80, 381, 141))
        self.tab_main.setAutoFillBackground(False)
        self.tab_main.setTabBarAutoHide(True)
        self.tab_main.setObjectName("tab_main")
        self.tab_new = QtWidgets.QWidget()
        self.tab_new.setObjectName("tab_new")
        self.li_worker = QtWidgets.QLineEdit(self.tab_new)
        self.li_worker.setGeometry(QtCore.QRect(120, 40, 113, 20))
        self.li_worker.setObjectName("li_worker")
        self.bt_new = QtWidgets.QPushButton(self.tab_new)
        self.bt_new.setGeometry(QtCore.QRect(240, 40, 75, 23))
        self.bt_new.setObjectName("bt_new")
        self.progressBar = QtWidgets.QProgressBar(self.tab_new)
        self.progressBar.setGeometry(QtCore.QRect(140, 80, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.tab_main.addTab(self.tab_new, "")
        self.tab_del = QtWidgets.QWidget()
        self.tab_del.setObjectName("tab_del")
        self.li_time = QtWidgets.QLineEdit(self.tab_del)
        self.li_time.setGeometry(QtCore.QRect(120, 40, 113, 20))
        self.li_time.setObjectName("li_time")
        self.bt_time = QtWidgets.QPushButton(self.tab_del)
        self.bt_time.setGeometry(QtCore.QRect(240, 40, 75, 23))
        self.bt_time.setObjectName("bt_time")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_del)
        self.progressBar_2.setGeometry(QtCore.QRect(140, 80, 118, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.tab_main.addTab(self.tab_del, "")
        self.bt_weekday = QtWidgets.QRadioButton(Dialog)
        self.bt_weekday.setGeometry(QtCore.QRect(130, 40, 90, 16))
        self.bt_weekday.setObjectName("bt_weekday")
        self.bt_weekend = QtWidgets.QRadioButton(Dialog)
        self.bt_weekend.setGeometry(QtCore.QRect(230, 40, 90, 16))
        self.bt_weekend.setObjectName("bt_weekend")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(110, 20, 181, 51))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.raise_()
        self.tab_main.raise_()
        self.bt_weekday.raise_()
        self.bt_weekend.raise_()

        self.retranslateUi(Dialog)
        self.tab_main.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "기동5중대 근무배치 프로그램(Ver.2.0)"))
        self.li_worker.setText(_translate("Dialog", "첫 근무자 입력"))
        self.bt_new.setText(_translate("Dialog", "확인"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_new), _translate("Dialog", "근무표 생성"))
        self.li_time.setText(_translate("Dialog", "날짜-시간 입력"))
        self.bt_time.setText(_translate("Dialog", "확인"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_del), _translate("Dialog", "\'/\' 제거"))
        self.bt_weekday.setText(_translate("Dialog", "평일"))
        self.bt_weekend.setText(_translate("Dialog", "주말"))
        self.groupBox.setTitle(_translate("Dialog", "근무표 유형"))
import myres_rc
