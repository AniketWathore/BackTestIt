import numpy as np

def calculate_metrics(returns):
    sharpe = np.sqrt(252) * returns.mean() / returns.std() if returns.std() != 0 else 0
    drawdown = (returns.cumsum().expanding().max() - returns.cumsum()).max()
    win_rate = (returns > 0).mean()
    return {'sharpe': sharpe, 'max_drawdown': drawdown, 'win_rate': win_rate}