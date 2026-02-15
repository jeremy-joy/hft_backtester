"""
Docstring for backtester.engine
This is the main engine of the backtester. It will take in the bars from the feed
"""
from .feed import MarketDataFeed
from datetime import datetime

class BacktestEngine: 
    def __init__(self, feed: MarketDataFeed):
        self._feed = feed
        self._history: list[tuple[datetime, float]] = []
    # should process the feed i.e. iterate through the bars
    # record something for each bar, i.e. ts, close for now.
    def run_backtest(self):
        self._history = [] # reset history
        # we need to get each bar from the feed. 
        for bar in self._feed: 
            self._history.append((bar.ts, bar.close))
        return self._history