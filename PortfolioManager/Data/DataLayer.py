class DataLayer:
    def __init__(self):
        pass

    def getInstruments(self):
        return ("STX40","STXSWX","STXFIN","STXRAF","STXEMG")

    def getInstrumentClasses(self):
        return (("", "FIN", "Financial Instrument"), ("FIN", "FND", "Fund"), ("FND", "ETF", "Exchange Traded Fund"), ("FIN", "IPF", "Investment Portfolio"), ("FND", "UTR", "Unit Trust"), ("FIN", "SHR", "Ordinary Share"))
