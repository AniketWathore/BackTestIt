import argparse
from data.alpaca_data import AlpacaData
from api_config import ALPACA_CONFIG, SYMBOLS, TimeFrame, TIMEFRAME_MAP
from engine.backtest_engine import BacktestEngine
from strategy.text_to_strategy import TextToStrategy
from output.plot_results import plot_equity_curve, plot_trade_histogram
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', required=True, help='Strategy description')
    parser.add_argument('--symbol', required=True)
    parser.add_argument('--provider', choices=['alpaca', 'binance', 'csv'], required=True)
    parser.add_argument('--start', required=True)
    parser.add_argument('--end', required=True)
    args = parser.parse_args()
    
    # Load data
    if args.provider == 'alpaca':
        data_client = AlpacaData(ALPACA_CONFIG['api_key'], ALPACA_CONFIG['api_secret'])
    # ... similar for others
    
    data = data_client.get_historical_data(args.symbol, args.start, args.end)
    
    # Parse strategy
    parser = TextToStrategy()
    strategy = parser.parse_text(args.text, args.start, args.end)
    
    # Run backtest
    engine = BacktestEngine()
    results_df, metrics, trades = engine.run_backtest(data, strategy, args.start, args.end)
    
    # Plot
    plot_equity_curve(results_df['cum_returns'])
    plot_trade_histogram(trades)
    
    # Print metrics table
    print(pd.DataFrame([metrics]).T)

if __name__ == '__main__':
    main()