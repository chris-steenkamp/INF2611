'''Contains all dialogs of the application'''
from PyQt4 import QtGui, QtCore, QtSql
from Data import DatabaseSetup, DataLayer
from Widgets import DefaultTableViewWidget, DefaultTreeViewWidget
from Widgets import FinancialInstrumentWidget, InstrumentAllocationWidget, MainFormWidget
from Models import SqlTreeModel

class MyForm(QtGui.QMainWindow):
    '''The main form of the application'''
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = MainFormWidget()
        self.ui.setupUi(self)

        self.ui.actionClass_List.triggered.connect(self.show_classes)
        self.ui.actionInstrument_List.triggered.connect(self.show_instruments)
        self.ui.actionInvestment_Holdings.triggered.connect(self.show_investments)
        self.ui.actionCreateInstrument.triggered.connect(self.create_instruments)
        self.ui.actionAllocateToPortfolio.triggered.connect(self.allocate_instruments)
        self.ui.actionInstrument_Prices.triggered.connect(self.show_prices)

        self.ui.actionCascade.triggered.connect(self.ui.mdiArea.cascadeSubWindows)
        self.ui.actionTile.triggered.connect(self.ui.mdiArea.tileSubWindows)
        self.ui.actionNext.triggered.connect(self.ui.mdiArea.activateNextSubWindow)
        self.ui.actionPrevious.triggered.connect(self.ui.mdiArea.activatePreviousSubWindow)
        self.ui.actionClose_All.triggered.connect(self.ui.mdiArea.closeAllSubWindows)
        self.ui.actionClose_Current.triggered.connect(self.ui.mdiArea.closeActiveSubWindow)

        self.setWindowTitle("Portfolio Manager")

    def show_classes(self):
        '''Show the list of classes'''
        ClassListDialog.show_dialog(self.ui.mdiArea)

    def show_instruments(self):
        '''Show the list of instruments'''
        FinancialInstrumentListDialog.show_dialog(self.ui.mdiArea)

    def show_investments(self):
        '''Show current investments'''
        InvestmentHoldingsDialog.show_dialog(self.ui.mdiArea)

    def create_instruments(self):
        '''Create a new instrument'''
        FinancialInstrumentDialog.show_dialog(self.ui.mdiArea)

    def allocate_instruments(self):
        '''Allocate an instrument'''
        InstrumentAllocationDialog.show_dialog(self.ui.mdiArea)

    def show_prices(self):
        '''Show list of prices'''
        InstrumentPricingDialog.show_dialog(self.ui.mdiArea)

class BaseDialog(QtGui.QDialog):
    '''Represents the base of all other dialogs and provides
    static methods for showing a new dalog'''
    def __init__(self, interface, parent, title):
        QtGui.QDialog.__init__(self, parent)

        self.interface = interface
        self.interface.setupUi(self)

        self.parent = parent
        if  isinstance(self.parent, QtGui.QMdiArea):
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

    def close_event(self, event):
        if type(self.parent) is QtGui.QMdiArea:
            self.parent.removeSubWindow(self.dialog)

        super(BaseDialog, self).closeEvent(event)

        self.destroy()

    @staticmethod
    def show_dialog(base_dialog):
        dialog = base_dialog.dialog
        if type(base_dialog.parent) is QtGui.QMdiArea:
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

        self.mapper.addMapping(self.interface.txtInstrumentCode, self.model.fieldIndex("code"))
        self.mapper.addMapping(self.interface.txtInstrumentName, self.model.fieldIndex("name"))
        self.mapper.addMapping(self.interface.lstClassCode, classCdIndex)

        relationModel = self.model.relationModel(classCdIndex)
        self.interface.lstClassCode.setModel(relationModel)
        self.interface.lstClassCode.setModelColumn(relationModel.fieldIndex("name"))

        if activeRecord == -1:
            row = self.model.rowCount()
            self.model.insertRow(row)
            self.mapper.setCurrentIndex(row)
        else:
            self.mapper.setCurrentIndex(activeRecord)

        self.interface.buttonBox.button(QtGui.QDialogButtonBox.Save).clicked.connect(self.saveChanges)
        self.interface.buttonBox.button(QtGui.QDialogButtonBox.Discard).clicked.connect(self.discardChanges)

    def saveChanges(self):
        self.mapper.submit()
        self.accept()

    def discardChanges (self):
        self.mapper.revert()
        self.reject()

    @staticmethod
    def show_dialog(parent = None, activeRecord = -1, title = "Create New Financial Instrument"):
        return BaseDialog.show_dialog(FinancialInstrumentDialog(parent, activeRecord, title))

class FinancialInstrumentListDialog(BaseDialog):
    def __init__(self, parent, title):
        BaseDialog.__init__(self, DefaultTableViewWidget(), parent, title)

        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("financial_instrument")

        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.interface.tableView.setModel(self.model)
        self.model.select()

        self.interface.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Save|QtGui.QDialogButtonBox.Ok)

        self.interface.buttonBox.button(QtGui.QDialogButtonBox.Save).clicked.connect(self.edit_current)
        self.interface.buttonBox.button(QtGui.QDialogButtonBox.Save).setText("&Edit")

        self.interface.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.add_new)
        self.interface.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText("Add &New")

    def edit_current(self):
        current = self.interface.tableView.currentIndex()
        row = current.row()

        if row >= 0 and FinancialInstrumentDialog.show_dialog(activeRecord = row, title = "Edit Financial Instruments") == QtGui.QDialog.Accepted:
            self.model.select()

    def add_new(self):
        if FinancialInstrumentDialog.show_dialog(activeRecord = -1, title = "Create New Financial Instruments") == QtGui.QDialog.Accepted:
            self.model.select()

    @staticmethod
    def show_dialog(parent, title =  "View All Financial Instruments"):
        return BaseDialog.show_dialog(FinancialInstrumentListDialog(parent, title))

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

        self.mapper.addMapping(self.interface.txtDate, self.model.fieldIndex("start_date"))
        self.mapper.addMapping(self.interface.txtUnits, self.model.fieldIndex("units_held"))

        self.mapper.addMapping(self.interface.lstPortfolios, portfolioIndex)
        self.mapper.addMapping(self.interface.lstInstruments, instrumentIndex)

        instrumentRelationModel = self.model.relationModel(instrumentIndex)
        self.interface.lstInstruments.setModel(instrumentRelationModel)
        self.interface.lstInstruments.setModelColumn(instrumentRelationModel.fieldIndex("name"))

        portfolioRelationModel = self.model.relationModel(portfolioIndex)
        self.interface.lstPortfolios.setModel(portfolioRelationModel)
        self.interface.lstPortfolios.setModelColumn(portfolioRelationModel.fieldIndex("name"))

        self.interface.buttonBox.button(QtGui.QDialogButtonBox.Save).clicked.connect(self.saveChanges)
        self.interface.buttonBox.button(QtGui.QDialogButtonBox.Discard).clicked.connect(self.discardChanges)

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
    def show_dialog(parent = None, activeRecord = -1, title = "Allocate Financial Instrument"):
        BaseDialog.show_dialog(InstrumentAllocationDialog(parent, activeRecord, title))

class ClassListDialog(BaseDialog):
    def __init__(self, parent, title):
        BaseDialog.__init__(self, DefaultTreeViewWidget(), parent, title)

        self.model = SqlTreeModel(self, DataLayer.getClassHeaders(), 'instrument_class', 'FIN')
        self.interface.treeView.setModel(self.model)

    @staticmethod
    def show_dialog(parent, title = "View Instrument Classes"):
        return BaseDialog.show_dialog(ClassListDialog(parent, title))

class InvestmentHoldingsDialog(BaseDialog):
    def __init__(self, parent, title):
        BaseDialog.__init__(self, DefaultTableViewWidget(), parent, title)
        
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("instrument_invested_in")
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()

        self.interface.tableView.setModel(self.model)

        self.interface.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Save|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel)

        self.interface.buttonBox.button(QtGui.QDialogButtonBox.Save).clicked.connect(self.edit_current)
        self.interface.buttonBox.button(QtGui.QDialogButtonBox.Save).setText("&Edit Selected")

        self.interface.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.add_new)
        self.interface.buttonBox.button(QtGui.QDialogButtonBox.Ok).setText("Add &New")

        self.interface.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.delete_current)
        self.interface.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setText("&Delete Selected")

    def edit_current(self):
        row = self.interface.tableView.currentIndex().row()

        if row >= 0 and InstrumentAllocationDialog.show_dialog(activeRecord = row, title = "Edit Current Position") == QtGui.QDialog.Accepted:
            self.model.select()

    def add_new(self):
        if InstrumentAllocationDialog.show_dialog(activeRecord = -1, title = "Create New Instrument Allocation") == QtGui.QDialog.Accepted:
            self.model.select()

    def delete_current(self):
        index = self.interface.tableView.currentIndex().row()

        if index >= 0 and YesNoMessageBox(self, 'Delete Record?', 'Are you sure you want to delete this entry from the database?').exec_() == QtGui.QMessageBox.Yes:
            self.model.removeRow(index)
            self.model.submitAll()
            self.model.select()

    @staticmethod
    def show_dialog(parent, title =  "View Instrument Allocations"):
        return BaseDialog.show_dialog(InvestmentHoldingsDialog(parent, title))

class InstrumentPricingDialog(BaseDialog):
    def __init__(self, parent, title):
        BaseDialog.__init__(self, DefaultTableViewWidget(), parent, title)
       
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("instrument_valuation")
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()

        self.interface.tableView.setModel(self.model)

        self.interface.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.NoButton)

    @staticmethod
    def show_dialog(parent, title =  "View Instrument Price History"):
        return BaseDialog.show_dialog(InstrumentPricingDialog(parent, title))

class YesNoMessageBox(QtGui.QMessageBox):
    def __init__(self, parent, title, text, icon = QtGui.QMessageBox.Question, buttons = QtGui.QMessageBox.Yes | QtGui.QMessageBox.No):
        QMessageBox.__init__(self, parent)

        self.setIcon(icon)
        self.setText(text)
        self.setWindowTitle(title)
        self.setStandardButtons(buttons)
