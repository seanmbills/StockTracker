class WatchOrder:
    def __init__(self, abbrev, lowSell, highSell, lowBuy, highBuy):
        self.abbrev = abbrev.upper()
        self.lowSell = lowSell
        self.highSell = highSell
        self.lowBuy = lowBuy
        self.highBuy = highBuy

    def getAbbrev(self):
        return self.abbrev

    def getLowSell(self):
        return self.lowSell

    def getHighSell(self):
        return self.highSell

    def getLowBuy(self):
        return self.lowBuy

    def getHighBuy(self):
        return self.highBuy

    def updateLowSell(self, newSell):
        self.lowSell = newSell

    def updateHighSell(self, newSell):
        self.highSell = newSell

    def updateLowBuy(self, newBuy):
        self.lowBuy = newBuy

    def updateHighBuy(self, newBuy):
        self.highBuy = newBuy

    def __eq__(self, other):
        return self.abbrev.upper() == other.abbrev.upper()
