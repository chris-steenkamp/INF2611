from PyQt4.QtGui import *
from Widgets.AllocateFinancialInstrument import *
from Data.DataLayer import DataLayer

class AllocateFinancialInstrumentWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
            
        instruments = DataLayer.getInstruments()
        for i in instruments:
            if i[1] == "IPF":
                self.ui.lstPortfolios.addItem(i[0])
            else:
                self.ui.lstInstruments.addItem(i[0])

    def getDialog(self, mdiArea):
        dialog = QMdiSubWindow()
        dialog.setWidget(AllocateFinancialInstrumentWidget())
        dialog.setWindowTitle("Allocate Financial Instrument")
        mdiArea.addSubWindow(dialog)
        return dialog