# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIView.ui'
#
# Created: Mon May 11 09:32:29 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.resultBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.resultBrowser.setGeometry(QtCore.QRect(400, 140, 321, 41))
        self.resultBrowser.setObjectName("resultBrowser")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 200, 110, 32))
        self.pushButton.setObjectName("pushButton")
        self.StoreListView = QtGui.QTextBrowser(self.centralwidget)
        self.StoreListView.setGeometry(QtCore.QRect(50, 50, 241, 471))
        self.StoreListView.setObjectName("StoreListView")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 56, 13))
        self.label.setObjectName("label")
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 490, 110, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.newst = QtGui.QTextEdit(self.centralwidget)
        self.newst.setGeometry(QtCore.QRect(410, 390, 331, 31))
        self.newst.setObjectName("newst")
        self.newadd = QtGui.QTextEdit(self.centralwidget)
        self.newadd.setGeometry(QtCore.QRect(410, 450, 331, 31))
        self.newadd.setObjectName("newadd")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 400, 56, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 460, 71, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuSss = QtGui.QMenu(self.menubar)
        self.menuSss.setObjectName("menuSss")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSss.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "走起～", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "待选列表", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "新增店面", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "新增店名", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "新增店地址", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSss.setTitle(QtGui.QApplication.translate("MainWindow", "今天去哪吃？", None, QtGui.QApplication.UnicodeUTF8))

