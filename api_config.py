from alpaca.data.timeframe import TimeFrame, TimeFrameUnit  # Add this line


# Alpaca Api Configuration
ALPACA_CONFIG = {
    'api_key' : 'xxx',
    'client_id' : 'xxx',
    'api_secret': 'xxx',
    'redirect_uri': 'https://paper-api.alpaca.markets/v2'
}

# Binance Api Configuration
BINANCE_CONFIG = {
    'api_key' : 'xxx',
    'api_secret' : 'xxx'
}

# Symbol mappings (different providers use different formats)
SYMBOL_MAP = {
    'alpaca': {'AAPL': 'AAPL', 'BTC': 'BTCUSD'},  # Stock/crypto
    'binance': {'BTC': 'BTCUSDT', 'ETH': 'ETHUSDT'}  # Crypto pairs
}

# Timeframe mappings
TIMEFRAME_MAP = {
    'alpaca': {
        '1min': TimeFrame(1, TimeFrame.Minute),
        '5min': TimeFrame(5, TimeFrame.Minute),
        '15min': TimeFrame(15, TimeFrame.Minute),
        '1h': TimeFrame(1, TimeFrame.Hour),
        '1d': TimeFrame(1, TimeFrame.Day)
    },
    'binance': {
        '1min': '1m',
        '5min': '5m',
        '15min': '15m',
        '1h': '1h',
        '1d': '1d'
    }
}


SYMBOLS = {
    'alpaca': ['AAPL', 'TSLA', 'AMD'],
    'binance': ['BTCUSDT', 'ETHUSDT'],
    'csv': []  # User-specified files
}

INTERVALS = {
    '1min': TimeFrame(1, TimeFrameUnit.Minute),
    '5min': TimeFrame(5, TimeFrameUnit.Minute),
    '15min': TimeFrame(15, TimeFrameUnit.Minute),
    '1h': TimeFrame(1, TimeFrameUnit.Hour),
    '1d': TimeFrame(1, TimeFrameUnit.Day),
    'custom': TimeFrame(1, TimeFrameUnit.Minute)  # As per earlier outline
}
