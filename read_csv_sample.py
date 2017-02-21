import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick2_ochl
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

df = pd.read_csv('./data/VALE3Daily.csv', parse_dates=True, index_col=0)

df['5ma'] = df['Close'].rolling(window=5).mean()
df['20ma'] = df['Close'].rolling(window=20).mean()

df_ohlc = df['Close'].resample('10D').ohlc()
print(df_ohlc.tail())
#df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)


ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1 )
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1 )

ax1.plot(df.index, df['Close'])
ax1.plot(df.index, df['5ma'])
ax1.plot(df.index, df['20ma'])
ax2.bar(df.index, df['Volume'])

#plt.show()