# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\..\..\Screens\AllocateFinancialInstrument.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 175)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.txtDate = QtGui.QDateEdit(Form)
        self.txtDate.setObjectName(_fromUtf8("txtDate"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtDate)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.lstInstruments = QtGui.QComboBox(Form)
        self.lstInstruments.setObjectName(_fromUtf8("lstInstruments"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lstInstruments)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lstPortfolios = QtGui.QComboBox(Form)
        self.lstPortfolios.setObjectName(_fromUtf8("lstPortfolios"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lstPortfolios)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.txtUnits = QtGui.QSpinBox(Form)
        self.txtUnits.setObjectName(_fromUtf8("txtUnits"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.txtUnits)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_4.setText(_translate("Form", "Purchase Date", None))
        self.label.setText(_translate("Form", "Instrument Code", None))
        self.label_2.setText(_translate("Form", "Portfolio Code", None))
        self.label_3.setText(_translate("Form", "Number of Units", None))

