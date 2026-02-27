"""
Docstring for portfolio.py

This file will contain the portfolio
This is where we will keep track of what we are holding

"""

class Portfolio:
    def __init__(self):
        self._equity: float # portfolio worth
        self._cash: float = 0# cash we currently have available
        self._quantity: float = 0 # quantity of the asset we currently own
    
    def setInitialCash(self, cash: float):
        self._cash = cash

    def buyAsset(self, quantity: float, buy_price: float): 
        # we update our current quantity of the stock
        self._quantity += quantity
        # reduce the cash we have
        self._cash -= buy_price
    
    def sellAsset(self, quantity: float, sell_price: float): 
        # we update our current quantity of the stock
        self._quantity -= quantity
        # reduce the cash we have
        self._cash += sell_price
