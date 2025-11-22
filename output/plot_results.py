import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_equity_curve(cum_returns):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=cum_returns.index, y=cum_returns, mode='lines', name='Equity Curve'))
    fig.update_layout(title='Backtest Equity Curve', xaxis_title='Date', yaxis_title='Cumulative Return')
    fig.show()

def plot_trade_histogram(trades):
    pnl = trades['pnl']  # Assume computed
    plt.figure(figsize=(10, 6))
    sns.histplot(pnl, kde=True)
    plt.title('Trade P&L Distribution')
    plt.show()

# Heatmap for intraday performance, etc.