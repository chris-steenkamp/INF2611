'''Main '''
import sys
from PyQt4 import QtGui
from Data import DatabaseSetup, DataLayer
from Dialogs import MyForm

if __name__ == "__main__":
    APP = QtGui.QApplication(sys.argv)

    try:
        if sys.argv.index("--init") > 0:
            DatabaseSetup.populateData()
    except ValueError as ex:
        print("Assuming DB is populated %s" %ex)

    if not DataLayer.openConnection():
        sys.exit(1)

    WINDOW = MyForm()
    WINDOW.show()

    sys.exit(APP.exec_())
