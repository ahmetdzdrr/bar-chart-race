import bar_chart_race as bcr
import yfinance as yf
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')


tickers = ['AAPL', 'NVDA', 'GOOGL', 'TSLA']
data = yf.download(tickers, start='2012-01-01', end=datetime.now())

df_combined = data['Adj Close'].resample('M').last()
df_combined = df_combined.reset_index()
df_combined['Year'] = df_combined['Date'].dt.year
df_combined['Month'] = df_combined['Date'].dt.month
df_combined = df_combined.groupby(["Year", "Month"])[tickers].last().reset_index()


bcr.bar_chart_race(
    df=df_combined,
    filename='stock_prices_race.mp4',
    title='AAPL & NVDIA & GOOGL & TSLA 2020 - 2024 Monthly Close Price History')
