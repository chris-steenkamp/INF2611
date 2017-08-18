import sys
from PyQt4.QtGui import *
from Forms.MainForm import *
from Widgets.ClassListWidget import *
from Widgets.FinancialInstrumentListWidget import *

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.actionClass_List, QtCore.SIGNAL('triggered()'), self.showClasses)
        QtCore.QObject.connect(self.ui.actionInstrument_List, QtCore.SIGNAL('triggered()'), self.showInstruments)

        QtCore.QObject.connect(self.ui.actionCascade, QtCore.SIGNAL('triggered()'), self.ui.mdiArea.cascadeSubWindows)
        QtCore.QObject.connect(self.ui.actionTile, QtCore.SIGNAL('triggered()'), self.ui.mdiArea.tileSubWindows)
        QtCore.QObject.connect(self.ui.actionNext, QtCore.SIGNAL('triggered()'), self.ui.mdiArea.activateNextSubWindow)
        QtCore.QObject.connect(self.ui.actionPrevious, QtCore.SIGNAL('triggered()'), self.ui.mdiArea.activatePreviousSubWindow)
        QtCore.QObject.connect(self.ui.actionClose_All, QtCore.SIGNAL('triggered()'), self.ui.mdiArea.closeAllSubWindows)
        QtCore.QObject.connect(self.ui.actionClose_Current, QtCore.SIGNAL('triggered()'), self.ui.mdiArea.closeActiveSubWindow)

    def showClasses(self):
        ClassListWidget().getDialog(self.ui.mdiArea).show()

    def showInstruments(self):
        FinancialInstrumentListWidget().getDialog(self.ui.mdiArea).sho()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyForm()
    window.show()

    sys.exit(app.exec_())