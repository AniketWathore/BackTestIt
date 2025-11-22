# From provided, but remove get_current_price real-time; enhance get_historical_data
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime
import pandas as pd

class AlpacaData:
    def __init__(self, api_key, api_secret):
        self.client = StockHistoricalDataClient(api_key, api_secret)
    
    def get_historical_data(self, symbol, start, end, timeframe=TimeFrame.Day):
        request = StockBarsRequest(
            symbol_or_symbols=symbol,
            timeframe=timeframe,
            start=start,
            end=end,
            feed="iex"  # Free tier
        )
        bars = self.client.get_stock_bars(request)
        df = bars.df.reset_index()
        if 'symbol' in df.columns:
            df = df[df['symbol'] == symbol]
        return df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]