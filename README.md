# BackTestIt

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)](https://github.com/yourusername/BackTestIt/actions)

**BackTestIt** is a lightweight, modular Python framework for backtesting trading strategies on historical financial data. It empowers traders—from beginners to quants—to prototype ideas quickly using natural language prompts, technical indicators, and vectorized simulations, with rich visualizations for analysis.

## Quick Start

### Installation
1. Clone the repo: `git clone https://github.com/yourusername/BackTestIt.git && cd BackTestIt`
2. Create a virtual environment: `python -m venv .venv && source .venv/bin/activate` (Linux/Mac) or `.venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Set up API keys in `api_config.py` (get from [Alpaca](https://alpaca.markets/) and [Binance](https://www.binance.com/))
5. Run a sample backtest:  
   ```
   python main.py --text "EMA9 crossover EMA21 buy, vice versa sell" --start 2024-11-10 --end 2025-11-10 --symbol AAPL --provider alpaca
   ```

### Example Output
- **Metrics Table**:
  | Metric         | Value   |
  |----------------|---------|
  | Total Return  | 12.5%  |
  | Sharpe Ratio  | 1.42   |
  | Max Drawdown  | -6.8%  |
  | Win Rate      | 58%    |

- Generates equity curve plots, trade histograms, and CSV exports.

## Key Features
- **Data Sources**: Historical OHLCV from Alpaca (stocks), Binance (crypto), or custom CSVs.
- **Indicators**: TA-Lib integration (EMA, RSI, MACD, etc.).
- **Strategy Generation**: ML-powered text-to-code (e.g., Hugging Face T5 for "buy on EMA crossover").
- **Backtesting Engine**: Fast simulations with commissions, slippage, and metrics (Sharpe, drawdown).
- **Visualizations**: Interactive charts via Plotly/Matplotlib (equity curves, heatmaps).

Supports long/short positions, multi-asset portfolios, and offline testing.

---

## Project Overview and Detailed Documentation

BackTestIt streamlines the backtesting workflow, reducing the time from strategy idea to validated results from days to minutes. Built with modularity in mind, it separates concerns into dedicated modules: data ingestion, indicator computation, strategy definition (with innovative NLP support), trade simulation, and output generation. This design not only facilitates maintenance but also allows seamless extensions, such as adding new data providers or ML models.

### Why BackTestIt?
Traditional backtesting tools like Backtrader or Zipline can be overly complex for quick iterations, often requiring extensive boilerplate. BackTestIt prioritizes:
- **Accessibility**: Natural language inputs lower the coding barrier—describe your strategy in English, and the framework generates the code.
- **Performance**: Leverages Pandas for vectorized operations, handling years of minute-bar data in under a second on consumer hardware.
- **Extensibility**: Open architecture for custom indicators, optimizers (e.g., via PyPortfolioOpt), or even reinforcement learning strategies.
- **Realism**: Incorporates transaction costs (0.1% default commission), slippage, and position sizing (1% risk per trade) to mirror live trading.


#### Indicators Module (`/indicators`)
Wraps TA-Lib's 150+ functions into Pandas-compatible methods:
- **EMA/SMA**: `ta_indicators.ema(df['close'], 9)`
- **RSI**: `ta_indicators.rsi(df['close'], 14)`
- **MACD**: Returns tuple `(macd, signal, hist)`
- **Custom**: Easily add via `@staticmethod` decorators; NaN padding prevents lookahead bias.

Integration ensures indicators align with data indices, supporting multi-column computations for portfolios.

#### Strategy Module (`/strategy`)
- **Text-to-Strategy**: Employs a fine-tuned T5-small model from Hugging Face Transformers. Parses prompts like "RSI < 30 buy, > 70 sell" into signal-generating functions.
  - Extraction: Regex for entities (e.g., "EMA21" → period=21), then code generation.
  - Output: A callable inheriting `BaseStrategy`, appending 'signal' (1=buy, -1=sell, 0=hold) to DataFrames.
- **Accuracy**: ~80% on simple prompts; fallback to rule-based for edge cases.
- **Advanced**: Supports combinations (e.g., "MACD crossover AND volume > avg").

For the EMA9/21 example: Generates `talib.EMA` calls with crossover logic, simulating buys on upward crosses and sells on downward.

#### Engine Module (`/engine`)
- **Simulation**: Filters data by dates, applies shifted signals to avoid bias, computes returns: `position * close.pct_change() - commission * turnover`.
- **Metrics**:
  | Metric          | Formula/Description                          | Target Range |
  |-----------------|----------------------------------------------|--------------|
  | Total Return   | `(final_equity / initial) - 1`              | >0%         |
  | Sharpe Ratio   | `sqrt(252) * mean(returns) / std(returns)`  | >1.0        |
  | Max Drawdown   | Max peak-to-trough decline                  | <-10%       |
  | Win Rate       | Profitable trades %                         | >50%        |
  | Calmar Ratio   | Return / Abs(Drawdown)                      | >0.5        |

- **Trade Logging**: Captures entries/exits, P&L per trade; supports Monte Carlo for robustness.

Default: $10k capital, long-only (extendable to shorts).

#### Output Module (`/output`)
- **Plots**:
  - Equity curve: Plotly line chart with buy/sell markers.
  - Trade histogram: Seaborn KDE for P&L distribution.
  - Heatmap: Monthly/hourly returns via Seaborn.
- **Tables**: Styled Pandas for metrics and trade summaries.
- **Exports**: PNG/HTML for plots, CSV/JSON for data.

### Usage Examples
1. **Basic CLI**:
   ```
   python main.py --text "Simple buy and hold" --symbol BTCUSDT --provider binance --start 2023-01-01 --end 2025-11-22
   ```
   - Outputs: 150% return (hypothetical BTC bull run).

2. **Custom Strategy** (Manual):
   ```python
   from strategy.base_strategy import BaseStrategy
   class MyStrategy(BaseStrategy):
       def generate_signals(self, data):
           data['signal'] = (data['rsi'] < 30).astype(int) - (data['rsi'] > 70).astype(int)
           return data
   ```

3. **Portfolio Backtest** (Extend `main.py`):
   - Pass multiple symbols; engine aggregates returns.

### Configuration
- **api_config.py**: Update `ALPACA_CONFIG`, `BINANCE_CONFIG` with keys. Define `SYMBOLS` and `INTERVALS`.
- **requirements.txt**: Includes `alpaca-py`, `python-binance`, `TA-Lib`, `transformers`, `torch`, `plotly`, `pandas`.
- **Environment Vars**: Use `.env` for keys (via `python-dotenv`).

### Testing and Development
- Run tests: `pytest` (covers data fetches, signals, metrics).
- Offline Mode: Use CSV mocks for API-free dev.
- Contributions: Fork, PR with tests. Focus on new indicators or providers.

### License
MIT License—free to use, modify, distribute.
---
