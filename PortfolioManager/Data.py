import mysql.connector
from PyQt4 import QtSql

try:
    conn = mysql.connector.connect(host="localhost", user="root", passwd="root", db="portfolio_manager")
except mysql.connector.Error as e:
    print("Error connecting to database %s" %e)

cursor = conn.cursor()

class DataLayer:
    @classmethod
    def openConnection(cls):
        cls.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        cls.db.setHostName('localhost')
        cls.db.setDatabaseName('portfolio_manager')
        cls.db.setUserName('root')
        cls.db.setPassword('root')
        opened = cls.db.open()
        print(cls.db.lastError().text())

        return opened

    @staticmethod
    def getInstrumentHeaders():
        return ["Instrument Code", "Instrument Class", "Instrument Name"]

    @staticmethod
    def getInstruments():
        try:
            cursor.execute("SELECT code, name, class_cd FROM financial_instrument")
        except mysql.connector.Error:
            print("Unable to select from financial_instrument")

        return cursor.fetchall()

    @staticmethod
    def getClassHeaders():
        return ["Class Code", "Class Name", "Parent Class"]

    @staticmethod
    def getClasses():
        try:
            cursor.execute("SELECT * FROM instrument_class")
        except mysql.connector.Error:
            print("Unable to select from instrument_class")

        return cursor.fetchall()

class DatabaseSetup:
    @staticmethod
    def populateData():
        try:
            DatabaseSetup.__createInstrumentClass()
            DatabaseSetup.__initInstrumentClass()
        except mysql.connector.Error as e:
            print("Error creating class data %s" %e)

        try:
            DatabaseSetup.__initFinInstrument()
        except mysql.connector.Error as e:
            print("Error creating instrument data %s" %e)

        try:
            DatabaseSetup.__initInvestedIn()
        except mysql.connector.Error as e:
            print("Error creating invested in data %s" %e)

        try:
            DatabaseSetup.__initClients()
        except mysql.connector.Error as e:
            print("Error creating client data %s" %e)

        try:
            DatabaseSetup.__initClientShareholding()
        except mysql.connector.Error as e:
            print("Error creating client shareholding data %s" %e)

        try:
            DatabaseSetup.__initInstrumentPricing()
        except mysql.connector.Error as e:
            print("Error creating instrument pricing data %s" %e)
            

        conn.commit()

    @staticmethod
    def __createInstrumentClass():
        cursor.execute('''CREATE TABLE instrument_class (
	                        cd VARCHAR(10) PRIMARY KEY,
	                        name VARCHAR(100),
	                        sup_cd VARCHAR(10),
	                        seq INT,
	                        FOREIGN KEY (sup_cd) REFERENCES instrument_class(cd)
                        )''')

    @staticmethod
    def __initInstrumentClass():
        cursor.execute("INSERT INTO instrument_class (cd, name, seq) VALUES ('FIN', 'Financial Instrument', 1)")
        stmt = "INSERT INTO instrument_class (cd, name, sup_cd, seq) VALUES (%s, %s, %s, %s)"
        params = [
               ('FND', 'Fund', 'FIN', 2),
               ('ETF', 'Exchange Traded Fund', 'FND', 3),
               ('IPF', 'Investment Portfolio', 'FIN', 2),
               ('UTR', 'Unit Trust', 'FND', 3),
               ('CSH', 'Cash', 'FIN', 2),
               ('SHR', 'Ordinary Share', 'FIN', 2),
               ('BON', 'Bond', 'FIN', 2)
            ]
        cursor.executemany(stmt,params)
        conn.commit()

    @staticmethod
    def __initFinInstrument():
        stmt = "INSERT INTO financial_instrument (code, class_cd, name) VALUES (%s, %s, %s)"
        params = [
                ('BAL', 'IPF', 'Balanced Portfolio'),
                ('AGG', 'IPF', 'Aggressive Portfolio'),
                ('STX40', 'ETF', 'Satrix Top 40'),
                ('STXSWX', 'ETF', 'Satrix SWIX'),
                ('STXFIN', 'ETF', 'Satrix Financials'),
                ('STXRESI', 'ETF', 'Satrix Resources'),
                ('STXEMG', 'ETF', 'Satrix Emerging Markets'),
                ('R2025', 'BON', 'SA Government 2025'),
                ('ZAR', 'CSH', 'South African Rand'),
                ('USD', 'CSH', 'United States Dollar'),
                ('NPN', 'SHR', 'Naspers N Share'),
                ('MTN', 'SHR', 'MTN Ordinary Share')
            ]
        cursor.executemany(stmt,params)

    @staticmethod
    def __initInvestedIn():
        cursor.execute("INSERT INTO instrument_invested_in (start_date, investment_portfolio_no, financial_instrument_no, units_held) VALUES (str_to_date('20170101', '%Y%m%d'), 1, 3, 25)")
        cursor.execute("INSERT INTO instrument_invested_in (start_date, investment_portfolio_no, financial_instrument_no, units_held) VALUES (str_to_date('20170101', '%Y%m%d'), 1, 8, 25)")
        cursor.execute("INSERT INTO instrument_invested_in (start_date, investment_portfolio_no, financial_instrument_no, units_held) VALUES (str_to_date('20170101', '%Y%m%d'), 1, 9, 25)")
        cursor.execute("INSERT INTO instrument_invested_in (start_date, investment_portfolio_no, financial_instrument_no, units_held) VALUES (str_to_date('20170101', '%Y%m%d'), 1, 10, 2)")

        cursor.execute("INSERT INTO instrument_invested_in (start_date, investment_portfolio_no, financial_instrument_no, units_held) VALUES (str_to_date('20170101', '%Y%m%d'), 2, 3, 40)")
        cursor.execute("INSERT INTO instrument_invested_in (start_date, investment_portfolio_no, financial_instrument_no, units_held) VALUES (str_to_date('20170101', '%Y%m%d'), 2, 8, 10)")
        cursor.execute("INSERT INTO instrument_invested_in (start_date, investment_portfolio_no, financial_instrument_no, units_held) VALUES (str_to_date('20170101', '%Y%m%d'), 2, 9, 10)")
        cursor.execute("INSERT INTO instrument_invested_in (start_date, investment_portfolio_no, financial_instrument_no, units_held) VALUES (str_to_date('20170101', '%Y%m%d'), 2, 10, 10)")
        cursor.execute("INSERT INTO instrument_invested_in (start_date, investment_portfolio_no, financial_instrument_no, units_held) VALUES (str_to_date('20170101', '%Y%m%d'), 2, 11, 15)")
        cursor.execute("INSERT INTO instrument_invested_in (start_date, investment_portfolio_no, financial_instrument_no, units_held) VALUES (str_to_date('20170101', '%Y%m%d'), 2, 12, 15)")
        

    @staticmethod
    def __initClients():
        cursor.execute("INSERT INTO client (first_name, last_name, id_number, gender) VALUES ('Chris', 'Steenkamp', '8504030000000', 'M')")

    @staticmethod
    def __initClientShareholding():
        cursor.execute("INSERT INTO client_shareholding (start_date, investment_portfolio_no, client_no, shareholding_percentage) VALUES (str_to_date('20170101', '%Y%m%d'), 1, 1, 1)")
        cursor.execute("INSERT INTO client_shareholding (start_date, investment_portfolio_no, client_no, shareholding_percentage) VALUES (str_to_date('20170101', '%Y%m%d'), 2, 1, 1)")

    @staticmethod
    def __initInstrumentPricing():
        cursor.execute("INSERT INTO instrument_valuation (start_date, financial_instrument_no, unit_price, end_date) VALUES (str_to_date('20161230', '%Y%m%d'), 3, 43.72, str_to_date('20170131', '%Y%m%d'))")
        cursor.execute("INSERT INTO instrument_valuation (start_date, financial_instrument_no, unit_price, end_date) VALUES (str_to_date('20170131', '%Y%m%d'), 3, 45.89, str_to_date('20170228', '%Y%m%d'))")
        cursor.execute("INSERT INTO instrument_valuation (start_date, financial_instrument_no, unit_price, end_date) VALUES (str_to_date('20170228', '%Y%m%d'), 3, 44.32, str_to_date('20170331', '%Y%m%d'))")
        cursor.execute("INSERT INTO instrument_valuation (start_date, financial_instrument_no, unit_price, end_date) VALUES (str_to_date('20170331', '%Y%m%d'), 3, 45.50, str_to_date('20170428', '%Y%m%d'))")
        cursor.execute("INSERT INTO instrument_valuation (start_date, financial_instrument_no, unit_price, end_date) VALUES (str_to_date('20170428', '%Y%m%d'), 3, 47.27, str_to_date('20170531', '%Y%m%d'))")
        cursor.execute("INSERT INTO instrument_valuation (start_date, financial_instrument_no, unit_price, end_date) VALUES (str_to_date('20170531', '%Y%m%d'), 3, 47.01, str_to_date('20170630', '%Y%m%d'))")
        cursor.execute("INSERT INTO instrument_valuation (start_date, financial_instrument_no, unit_price, end_date) VALUES (str_to_date('20170630', '%Y%m%d'), 3, 45.95, str_to_date('20170731', '%Y%m%d'))")
        cursor.execute("INSERT INTO instrument_valuation (start_date, financial_instrument_no, unit_price, end_date) VALUES (str_to_date('20170731', '%Y%m%d'), 3, 43.72, str_to_date('20170831', '%Y%m%d'))")