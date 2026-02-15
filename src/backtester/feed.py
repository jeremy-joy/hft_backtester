"""
Docstring for backtester.feed:
This will take the bars and feed them to the engine sequqntially
"""

from backtester.events import Bar

# supply the bars/market data sequentially
class MarketDataFeed:
    def __init__(self, bars: list[Bar]):
        self._bars = bars #_ signifies private variable
    def __iter__(self):
        for bar in self._bars: 
            yield bar # emits one bar of market data at a time