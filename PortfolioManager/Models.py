from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

class SqlTreeModel(QStandardItemModel):
    def __init__(self, parent, headers, tableName, rootNode):
        QStandardItemModel.__init__(self, parent)

        self.setHorizontalHeaderLabels(headers)

        items = dict()

        query = QSqlQuery('select * from %s where sup_cd is not null order by seq, cd' %tableName)
        prevCd = rootNode
        parentItem = QStandardItem(rootNode)

        self.appendRow(parentItem)
        children = 0
        while query.next():
            cd = query.value(0)
            name = query.value(1)
            sup_cd = query.value(2)

            if prevCd != sup_cd :
                children = 0
                parentItem = items[sup_cd]
                prevCd = sup_cd

            cdChildItem = QStandardItem(cd)
            nameChildItem = QStandardItem(name)
            supChildItem = QStandardItem(sup_cd)
            items[cd] = cdChildItem
            parentItem.setChild(children, 0, cdChildItem)
            parentItem.setChild(children, 1, nameChildItem)
            parentItem.setChild(children, 2, supChildItem)
            children += 1

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