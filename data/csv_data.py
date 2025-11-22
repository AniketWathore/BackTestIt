import pandas as pd
from datetime import datetime

class CSVData:
    def get_historical_data(self, file_path, start=None, end=None):
        df = pd.read_csv(file_path, parse_dates=['timestamp'])
        if start:
            df = df[df['timestamp'] >= datetime.strptime(start, '%Y-%m-%d')]
        if end:
            df = df[df['timestamp'] <= datetime.strptime(end, '%Y-%m-%d')]
        return df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]