# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\..\..\Screens\MainForm.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.verticalLayout.addWidget(self.mdiArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menuMaintenance = QtGui.QMenu(self.menubar)
        self.menuMaintenance.setObjectName(_fromUtf8("menuMaintenance"))
        self.menuWindow = QtGui.QMenu(self.menubar)
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Exit = QtGui.QAction(MainWindow)
        self.action_Exit.setObjectName(_fromUtf8("action_Exit"))
        self.actionClass_List = QtGui.QAction(MainWindow)
        self.actionClass_List.setObjectName(_fromUtf8("actionClass_List"))
        self.actionInstrument_List = QtGui.QAction(MainWindow)
        self.actionInstrument_List.setObjectName(_fromUtf8("actionInstrument_List"))
        self.actionCascade = QtGui.QAction(MainWindow)
        self.actionCascade.setObjectName(_fromUtf8("actionCascade"))
        self.actionTile = QtGui.QAction(MainWindow)
        self.actionTile.setObjectName(_fromUtf8("actionTile"))
        self.actionNext = QtGui.QAction(MainWindow)
        self.actionNext.setObjectName(_fromUtf8("actionNext"))
        self.actionPrevious = QtGui.QAction(MainWindow)
        self.actionPrevious.setObjectName(_fromUtf8("actionPrevious"))
        self.actionClose_All = QtGui.QAction(MainWindow)
        self.actionClose_All.setObjectName(_fromUtf8("actionClose_All"))
        self.actionClose_Current = QtGui.QAction(MainWindow)
        self.actionClose_Current.setObjectName(_fromUtf8("actionClose_Current"))
        self.actionCreateInstrument = QtGui.QAction(MainWindow)
        self.actionCreateInstrument.setObjectName(_fromUtf8("actionCreateInstrument"))
        self.actionAllocateToPortfolio = QtGui.QAction(MainWindow)
        self.actionAllocateToPortfolio.setObjectName(_fromUtf8("actionAllocateToPortfolio"))
        self.menu_File.addAction(self.actionClose_Current)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menuMaintenance.addAction(self.actionClass_List)
        self.menuMaintenance.addAction(self.actionInstrument_List)
        self.menuMaintenance.addSeparator()
        self.menuMaintenance.addAction(self.actionCreateInstrument)
        self.menuMaintenance.addAction(self.actionAllocateToPortfolio)
        self.menuWindow.addAction(self.actionCascade)
        self.menuWindow.addAction(self.actionTile)
        self.menuWindow.addAction(self.actionNext)
        self.menuWindow.addAction(self.actionPrevious)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionClose_All)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuMaintenance.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Exit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menuMaintenance.setTitle(_translate("MainWindow", "&View", None))
        self.menuWindow.setTitle(_translate("MainWindow", "Window", None))
        self.action_Exit.setText(_translate("MainWindow", "E&xit", None))
        self.actionClass_List.setText(_translate("MainWindow", "Instrument &Classes", None))
        self.actionClass_List.setStatusTip(_translate("MainWindow", "Maintain Available Instruments", None))
        self.actionInstrument_List.setText(_translate("MainWindow", "&Financial Instruments", None))
        self.actionCascade.setText(_translate("MainWindow", "&Cascade", None))
        self.actionTile.setText(_translate("MainWindow", "&Tile", None))
        self.actionNext.setText(_translate("MainWindow", "&Next", None))
        self.actionPrevious.setText(_translate("MainWindow", "&Previous", None))
        self.actionClose_All.setText(_translate("MainWindow", "Close &All", None))
        self.actionClose_All.setShortcut(_translate("MainWindow", "Ctrl+Shift+F4", None))
        self.actionClose_Current.setText(_translate("MainWindow", "&Close", None))
        self.actionClose_Current.setShortcut(_translate("MainWindow", "Ctrl+F4", None))
        self.actionCreateInstrument.setText(_translate("MainWindow", "Create Financial Instrument", None))
        self.actionAllocateToPortfolio.setText(_translate("MainWindow", "Allocate Instrument to &Portfolio", None))

