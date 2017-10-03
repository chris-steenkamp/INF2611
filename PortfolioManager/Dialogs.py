from PyQt4 import QtGui, QtCore, QtSql
from Data import *
from Widgets import *
from Models import *

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = MainFormWidget()
        self.ui.setupUi(self)

        self.ui.actionClass_List.triggered.connect(self.showClasses)
        self.ui.actionInstrument_List.triggered.connect(self.showInstruments)
        self.ui.actionInvestment_Holdings.triggered.connect(self.showInvestments)
        self.ui.actionCreateInstrument.triggered.connect(self.createInstruments)
        self.ui.actionAllocateToPortfolio.triggered.connect(self.allocateInstruments)
        self.ui.actionInstrument_Prices.triggered.connect(self.showPrices)

        self.ui.actionCascade.triggered.connect(self.ui.mdiArea.cascadeSubWindows)
        self.ui.actionTile.triggered.connect(self.ui.mdiArea.tileSubWindows)
        self.ui.actionNext.triggered.connect(self.ui.mdiArea.activateNextSubWindow)
        self.ui.actionPrevious.triggered.connect(self.ui.mdiArea.activatePreviousSubWindow)
        self.ui.actionClose_All.triggered.connect(self.ui.mdiArea.closeAllSubWindows)
        self.ui.actionClose_Current.triggered.connect(self.ui.mdiArea.closeActiveSubWindow)

        self.setWindowTitle("Portfolio Manager")

    def showClasses(self):
        ClassListDialog.showDialog(self.ui.mdiArea)

    def showInstruments(self):
        FinancialInstrumentListDialog.showDialog(self.ui.mdiArea)

    def showInvestments(self):
        InvestmentHoldingsDialog.showDialog(self.ui.mdiArea)

    def createInstruments(self):
        FinancialInstrumentDialog.showDialog(self.ui.mdiArea)
    
    def allocateInstruments(self):
        InstrumentAllocationDialog.showDialog(self.ui.mdiArea)

    def showPrices(self):
        InstrumentPricingDialog.showDialog(self.ui.mdiArea)

class BaseDialog(QtGui.QDialog):
    def __init__(self, ui, parent, title):
        QtGui.QDialog.__init__(self, parent)

        self.ui = ui
        self.ui.setupUi(self)

        self.parent = parent
        if type(self.parent) is QtGui.QMdiArea:
            self.dialog = QtGui.QMdiSubWindow()
            self.dialog.setWidget(self)
            self.parent.addSubWindow(self.dialog)
        else:
            self.dialog = self
        
        self.dialog.setWindowTitle(title)
        self.accepted.connect(self.__accept)
        self.rejected.connect(self.__reject)

    def __accept(self):
        self.close()

    def __reject(self):
        self.close()

    def closeEvent(self, event):
        if type(self.parent) is QtGui.QMdiArea:
            self.parent.removeSubWindow(self.dialog)

        super(BaseDialog, self).closeEvent(event)

        self.destroy()

    @staticmethod
    def showDialog(baseDialog):
        dialog = baseDialog.dialog
        if type(baseDialog.parent) is QtGui.QMdiArea:
            return dialog.show()
        else:
            return dialog.exec_()

class FinancialInstrumentDialog(BaseDialog):
    def __init__(self, parent, activeRecord, title):
        BaseDialog.__init__(self, FinancialInstrumentWidget(), parent, title)

        self.model = QtSql.QSqlRelationalTableModel(self)
        self.model.setTable("financial_instrument")

        classCdIndex = self.model.fieldIndex("class_cd")
        classCdRelation = QtSql.QSqlRelation("instrument_class", "cd", "name")
        self.model.setRelation(classCdIndex, classCdRelation)

        self.model.select()

        self.mapper = QtGui.QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)


        self.mapper.setItemDelegate(QtSql.QSqlRelationalDelegate(self))

        self.mapper.addMapping(self.ui.txtInstrumentCode, self.model.fieldIndex("code"))
        self.mapper.addMapping(self.ui.txtInstrumentName, self.model.fieldIndex("name"))
        self.mapper.addMapping(self.ui.lstClassCode, classCdIndex)

        relationModel = self.model.relationModel(classCdIndex)
        self.ui.lstClassCode.setModel(relationModel)
        self.ui.lstClassCode.setModelColumn(relationModel.fieldIndex("name"))

        if activeRecord == -1:
            row = self.model.rowCount()
            self.model.insertRow(row)
            self.mapper.setCurrentIndex(row)
        else:
            self.mapper.setCurrentIndex(activeRecord)

        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Save).clicked.connect(self.saveChanges)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Discard).clicked.connect(self.discardChanges)

    def saveChanges(self):
        self.mapper.submit()
        self.accept()

    def discardChanges (self):
        self.mapper.revert()
        self.reject()

    @staticmethod
    def showDialog(parent = None, activeRecord = -1, title = "Create New Financial Instrument"):
        return BaseDialog.showDialog(FinancialInstrumentDialog(parent, activeRecord, title))

class FinancialInstrumentListDialog(BaseDialog):
    def __init__(self, parent, title):
        BaseDialog.__init__(self, DefaultTableViewWidget(), parent, title)

        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("financial_instrument")

        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.ui.tableView.setModel(self.model)
        self.model.select()

        self.ui.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Save|QtGui.QDialogButtonBox.Ok)

        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Save).clicked.connect(self.editCurrent)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Save).setText("&Edit")

        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.addNew)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText("Add &New")

    def editCurrent(self):
        current = self.ui.tableView.currentIndex()
        row = current.row()

        if row >= 0 and FinancialInstrumentDialog.showDialog(activeRecord = row, title = "Edit Financial Instruments") == QDialog.Accepted:
            self.model.select()

    def addNew(self):
        if FinancialInstrumentDialog.showDialog(activeRecord = -1, title = "Create New Financial Instruments") == QDialog.Accepted:
            self.model.select()

    @staticmethod
    def showDialog(parent, title =  "View All Financial Instruments"):
        return BaseDialog.showDialog(FinancialInstrumentListDialog(parent, title))

class InstrumentAllocationDialog(BaseDialog):
    def __init__(self, parent, activeRecord, title):
        BaseDialog.__init__(self, InstrumentAllocationWidget(), parent, title)
            
        self.model = QtSql.QSqlRelationalTableModel(self)
        self.model.setTable("instrument_invested_in")

        instrumentIndex = self.model.fieldIndex("financial_instrument_no")
        instrumentRelation = QtSql.QSqlRelation("investment_asset", "no", "name")
        self.model.setRelation(instrumentIndex, instrumentRelation)

        portfolioIndex = self.model.fieldIndex("investment_portfolio_no")
        portfolioRelation = QtSql.QSqlRelation("investment_portfolio", "no", "name")
        self.model.setRelation(portfolioIndex, portfolioRelation)

        self.model.select()

        self.mapper = QtGui.QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)

        self.mapper.setItemDelegate(QtSql.QSqlRelationalDelegate(self))

        self.mapper.addMapping(self.ui.txtDate, self.model.fieldIndex("start_date"))
        self.mapper.addMapping(self.ui.txtUnits, self.model.fieldIndex("units_held"))

        self.mapper.addMapping(self.ui.lstPortfolios, portfolioIndex)
        self.mapper.addMapping(self.ui.lstInstruments, instrumentIndex)

        instrumentRelationModel = self.model.relationModel(instrumentIndex)
        self.ui.lstInstruments.setModel(instrumentRelationModel)
        self.ui.lstInstruments.setModelColumn(instrumentRelationModel.fieldIndex("name"))

        portfolioRelationModel = self.model.relationModel(portfolioIndex)
        self.ui.lstPortfolios.setModel(portfolioRelationModel)
        self.ui.lstPortfolios.setModelColumn(portfolioRelationModel.fieldIndex("name"))

        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Save).clicked.connect(self.saveChanges)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Discard).clicked.connect(self.discardChanges)

        if activeRecord == -1:
            row = self.model.rowCount()
            self.model.insertRow(row)
            self.mapper.setCurrentIndex(row)
        else:
            self.mapper.setCurrentIndex(activeRecord)

    def saveChanges(self):
        self.mapper.submit()
        self.accept()

    def discardChanges (self):
        self.mapper.revert()
        self.reject()

    @staticmethod
    def showDialog(parent = None, activeRecord = -1, title = "Allocate Financial Instrument"):
        BaseDialog.showDialog(InstrumentAllocationDialog(parent, activeRecord, title))

class ClassListDialog(BaseDialog):
    def __init__(self, parent, title):
        BaseDialog.__init__(self, DefaultTreeViewWidget(), parent, title)

        self.model = SqlTreeModel(self, DataLayer.getClassHeaders(), 'instrument_class', 'FIN')
        self.ui.treeView.setModel(self.model)

    @staticmethod
    def showDialog(parent, title = "View Instrument Classes"):
        return BaseDialog.showDialog(ClassListDialog(parent, title))

class InvestmentHoldingsDialog(BaseDialog):
    def __init__(self, parent, title):
        BaseDialog.__init__(self, DefaultTableViewWidget(), parent, title)
        
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("instrument_invested_in")
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()

        self.ui.tableView.setModel(self.model)

        self.ui.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Save|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel)

        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Save).clicked.connect(self.editCurrent)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Save).setText("&Edit Selected")

        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.addNew)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText("Add &New")

        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.deleteCurrent)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setText("&Delete Selected")

    def editCurrent(self):
        row = self.ui.tableView.currentIndex().row()

        if row >= 0 and InstrumentAllocationDialog.showDialog(activeRecord = row, title = "Edit Current Position") == QDialog.Accepted:
            self.model.select()

    def addNew(self):
        if InstrumentAllocationDialog.showDialog(activeRecord = -1, title = "Create New Instrument Allocation") == QDialog.Accepted:
            self.model.select()

    def deleteCurrent(self):
        index = self.ui.tableView.currentIndex().row()

        if index >= 0 and YesNoMessageBox(self, 'Delete Record?', 'Are you sure you want to delete this entry from the database?').exec_() == QMessageBox.Yes:
            self.model.removeRow(index)
            self.model.submitAll()
            self.model.select()

    @staticmethod
    def showDialog(parent, title =  "View Instrument Allocations"):
        return BaseDialog.showDialog(InvestmentHoldingsDialog(parent, title))

class InstrumentPricingDialog(BaseDialog):
    def __init__(self, parent, title):
        BaseDialog.__init__(self, DefaultTableViewWidget(), parent, title)
        
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("instrument_valuation")
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()

        self.ui.tableView.setModel(self.model)

        self.ui.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.NoButton)

    @staticmethod
    def showDialog(parent, title =  "View Instrument Price History"):
        return BaseDialog.showDialog(InstrumentPricingDialog(parent, title))

class YesNoMessageBox(QMessageBox):
    def __init__(self, parent, title, text, icon = QMessageBox.Question, buttons = QMessageBox.Yes | QMessageBox.No):
        QMessageBox.__init__(self, parent)

        self.setIcon(icon)
        self.setText(text)
        self.setWindowTitle(title)
        self.setStandardButtons(buttons)
