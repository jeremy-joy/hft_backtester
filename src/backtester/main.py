"""
Docstring for backtester.main
This is the main entry point for the backtester. It will create the feed and the engine and run the backtest.
"""
from .events import Bar
from .feed import MarketDataFeed
from .engine import BacktestEngine
from datetime import datetime

def main():
    # create some Bars for the feed
    bars = [
        Bar((2025, 3, 1), 100.00, 112.01, 96.47, 102.11),
        Bar((2025, 3, 2), 102.11, 113.01, 93.47, 103.11),
        Bar((2025, 3, 3), 103.11, 110.01, 91.47, 100.98),
        Bar((2025, 3, 4), 100.98, 111.01, 90.47, 111.03)
    ]
    feed = MarketDataFeed(bars)
    engine = BacktestEngine(feed)
    history = engine.run_backtest()
    print(history)
if __name__ == "__main__":
    main()