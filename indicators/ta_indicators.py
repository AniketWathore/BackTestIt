import talib
import pandas as pd

class TAIndicators:
    @staticmethod
    def ema(series, period):
        return pd.Series(talib.EMA(series.values, timeperiod=period), index=series.index)
    
    @staticmethod
    def rsi(series, period=14):
        return pd.Series(talib.RSI(series.values, timeperiod=period), index=series.index)
    
    # Add MACD, BBANDS, etc.