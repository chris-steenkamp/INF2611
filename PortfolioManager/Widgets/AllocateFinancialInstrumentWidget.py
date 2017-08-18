from PyQt4.QtGui import *
from Widgets.AllocateFinancialInstrument import *

class AllocateFinancialInstrumentWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def getDialog(self, mdiArea):
        dialog = QMdiSubWindow()
        dialog.setWidget(AllocateFinancialInstrumentWidget())
        dialog.setWindowTitle("Allocate Financial Instrument")
        mdiArea.addSubWindow(dialog)
        return dialog