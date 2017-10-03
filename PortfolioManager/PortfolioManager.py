import sys
from PyQt4.QtGui import *
from Data import *
from Dialogs import *

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    try:
        if sys.argv.index("--init") > 0:
            DatabaseSetup.populateData()
            pass
    except ValueError as e:
        print("Assuming DB is populated %s" %e)

    if not DataLayer.openConnection():
        sys.exit(1)

    window = MyForm()
    window.show()

    sys.exit(app.exec_())