from PyQt4.QtGui import *
from Widgets.ClassList import *
from Models.SimpleListModel import *
from Data.DataLayer import DataLayer

class ClassListWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        tree = self.ui.treeInstrumentClasses
        #data = DataLayer()
        #model = SimpleListModel(self, data.getClasses(), data.getClassHeaders())
        #tree.setModel(model)

        tree.setHeaderLabels(DataLayer.getClassHeaders())
        parent = QTreeWidgetItem(["FIN", "Financial Instruments"])
        parent.addChild(QTreeWidgetItem(("CSH", "Cash", "FIN")))
        parent.addChild(QTreeWidgetItem(("IPF", "Investment Portfolio", "FIN")))
        parent.addChild(QTreeWidgetItem(("SHR", "Ordinary Share", "FIN")))
        fnd = QTreeWidgetItem(("FND", "Fund", "FIN"))
        fnd.addChild(QTreeWidgetItem(("ETF", "Exchange Traded Fund", "FND")))
        fnd.addChild(QTreeWidgetItem(("UTR", "Unit Trust", "FND")))
        parent.addChild(fnd)

        tree.addTopLevelItem(parent)

    def getDialog(self, mdiArea):
        dialog = QMdiSubWindow()
        dialog.setWidget(ClassListWidget())
        dialog.setWindowTitle("Financial Instrument Classes")
        mdiArea.addSubWindow(dialog)
        return dialog