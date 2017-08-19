class DataLayer:
    @staticmethod
    def getInstrumentHeaders():
        return ["Instrument Code", "Instrument Class", "Instrument Name"]

    @staticmethod
    def getInstruments():
        return (("Balanced", "IPF", "Balanced Portfolio"),
                ("Aggressive", "IPF", "Aggressive Portfolio"),
                ("STX40", "ETF", "Satrix Top 40"),
                ("STXSWX", "ETF", "Satrix SWIX"),
                ("STXFIN", "ETF", "Satrix Financials"),
                ("STXRESI", "ETF", "Satrix Resources"),
                ("STXEMG", "ETF", "Satrix Emerging Markets"))

    @staticmethod
    def getClassHeaders():
        return ["Class Code", "Class Name", "Parent Class"]

    @staticmethod
    def getClasses():
        return (("FIN", "Financial Instrument", ""), 
               ("FND", "Fund", "FIN"),
               ("ETF", "Exchange Traded Fund", "FND"),
               ("IPF", "Investment Portfolio", "FIN"),
               ("UTR", "Unit Trust", "FND"),
               ("CSH", "Cash", "FIN"),
               ("SHR", "Ordinary Share", "FIN"))
