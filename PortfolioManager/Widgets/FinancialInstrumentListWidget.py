from PyQt4.QtGui import *
from Widgets.FinancialInstrumentList import *
from Data.DataLayer import *

class FinancialInstrumentListWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        for i in DataLayer().getInstruments():
            self.ui.lstInstruments.addItem(i)

    def getDialog(self, mdiArea):
        dialog = QMdiSubWindow()
        dialog.setWidget(FinancialInstrumentListWidget())
        dialog.setWindowTitle("List of Financial Instruments")
        mdiArea.addSubWindow(dialog)
        return dialog