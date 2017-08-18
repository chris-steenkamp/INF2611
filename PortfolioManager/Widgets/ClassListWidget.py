from PyQt4.QtGui import *
from Widgets.ClassList import *
from Data.DataLayer import *

class ClassListWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.treeInstrumentClasses.setSelectionBehavior(QAbstractItemView.SelectRows)
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Class Code", "Class Name"])
        self.ui.treeInstrumentClasses.setModel(model)
        self.ui.treeInstrumentClasses.setUniformRowHeights(True)
        parent = QStandardItem("FIN")
        for i in DataLayer().getInstrumentClasses():
            child = QStandardItem(i[1])
            child2 = QStandardItem(i[2])
            parent.appendRow([child, child2])

        model.appendRow(parent)

    def getDialog(self, mdiArea):
        dialog = QMdiSubWindow()
        dialog.setWidget(ClassListWidget())
        dialog.setWindowTitle("Financial Instrument Classes")
        mdiArea.addSubWindow(dialog)
        return dialog