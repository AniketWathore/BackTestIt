import pandas as pd
import numpy as np
from engine.metrics import calculate_metrics

class BacktestEngine:
    def __init__(self, initial_capital=10000, commission=0.001):
        self.initial_capital = initial_capital
        self.commission = commission
    
    def run_backtest(self, data: pd.DataFrame, strategy, start_date, end_date):
        data = data[(data['timestamp'] >= start_date) & (data['timestamp'] <= end_date)].copy()
        data['signal'] = strategy.generate_signals(data)
        data['position'] = data['signal'].shift(1).fillna(0)
        data['returns'] = data['close'].pct_change()
        data['strategy_returns'] = data['position'] * data['returns'] - self.commission * abs(data['position'].diff())
        data['cum_returns'] = (1 + data['strategy_returns']).cumprod()
        metrics = calculate_metrics(data['strategy_returns'])
        trades = data[data['signal'] != 0]  # Log trades
        return data, metrics, trades