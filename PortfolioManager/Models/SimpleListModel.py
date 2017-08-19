from PyQt4.QtCore import *
from PyQt4.QtGui import *

class SimpleListModel(QAbstractTableModel):
    def __init__(self, parent, instrumentList, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)

        self.list = instrumentList
        self.header = header

    def rowCount(self, parent = QModelIndex()):
        return len(self.list)

    def columnCount(self, parent = QModelIndex()):
        return len(self.list[0])

    def data(self, index, role = Qt.DisplayRole):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None

        return self.list[index.row()][index.column()]

    def headerData(self, col, orientation = Qt.Horizontal, role = Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None