from PyQt4.QtGui import *
from Widgets.CreateFinancialInstrument import *
from Data.DataLayer import DataLayer

class CreateFinancialInstrumentWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        for i in DataLayer.getClasses():
            self.ui.lstClassCode.addItem(i[0])

    def getDialog(self, mdiArea):
        dialog = QMdiSubWindow()
        dialog.setWidget(CreateFinancialInstrumentWidget())
        dialog.setWindowTitle("Create New Financial Instrument")
        mdiArea.addSubWindow(dialog)
        return dialog