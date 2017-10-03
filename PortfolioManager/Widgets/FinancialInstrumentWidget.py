# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FinancialInstrumentWidget.ui'
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
        Form.resize(400, 161)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lstClassCode = QtGui.QComboBox(Form)
        self.lstClassCode.setObjectName(_fromUtf8("lstClassCode"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lstClassCode)
        self.txtInstrumentCode = QtGui.QLineEdit(Form)
        self.txtInstrumentCode.setObjectName(_fromUtf8("txtInstrumentCode"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtInstrumentCode)
        self.txtInstrumentName = QtGui.QLineEdit(Form)
        self.txtInstrumentName.setObjectName(_fromUtf8("txtInstrumentName"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtInstrumentName)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Discard|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.txtInstrumentCode)
        self.label_2.setBuddy(self.txtInstrumentName)
        self.label_3.setBuddy(self.lstClassCode)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.txtInstrumentCode, self.txtInstrumentName)
        Form.setTabOrder(self.txtInstrumentName, self.lstClassCode)
        Form.setTabOrder(self.lstClassCode, self.buttonBox)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Instrument Code", None))
        self.label_2.setText(_translate("Form", "Instrument Name", None))
        self.label_3.setText(_translate("Form", "Class Code", None))

