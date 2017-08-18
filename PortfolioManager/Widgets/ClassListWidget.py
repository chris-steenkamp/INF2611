from PyQt4.QtGui import *
from Widgets.ClassList import *

class ClassListWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def getDialog(self, mdiArea):
        dialog = QMdiSubWindow()
        dialog.setWidget(ClassListWidget())
        dialog.setWindowTitle("Financial Instrument Classes")
        mdiArea.addSubWindow(dialog)
        return dialog