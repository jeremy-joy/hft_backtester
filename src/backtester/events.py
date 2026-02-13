"""
Defines the key event types used in this backtesing engine. 
This module contains: 
- Bar: the market data for a single time interval
- Order: Strategy trade request (i.e. Buy, Sell, Hold )
- Fill: The execution result

These events are the messages that get passed around the system
"""
from dataclasses import dataclass
from datetime import datetime
from typing import optional

@dataclass(frozen =True)
class Bar:
    ts: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float | None

@dataclass(frozen=True)
class Order:
    ts: datetime
    symbol: str
    side: str
    quantity: float
    order_type: str #MARKET or LIMIT

@dataclass(frozen=True)
class Fill:
    ts: datetime
    symbol: str
    side: str
    quantity: float
    price: float
    fees: float





