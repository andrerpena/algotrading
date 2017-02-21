import pandas as pd
from pandas.compat import StringIO

import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates


def plot_candlestick(df, ax=None, fmt="%Y-%m-%d"):
    if ax is None:
        fig, ax = plt.subplots()
    idx_name = df.index.name
    dat = df.reset_index()[[idx_name, "Open", "High", "Low", "Close"]]
    dat[df.index.name] = dat[df.index.name].map(mdates.date2num)
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(mdates.DateFormatter(fmt))
    plt.xticks(rotation=45)
    _ = candlestick_ohlc(ax, dat.values, width=.6, colorup='g', alpha=1)
    ax.set_xlabel(idx_name)
    ax.set_ylabel("OHLC")
    return ax


data = """Date,Stock,Open,High,Low,Close,Volume
2016-09-29,KESM,7.92,7.98,7.92,7.97,149400
2016-09-30,KESM,7.96,7.97,7.84,7.9,29900
2016-10-04,KESM,7.8,7.94,7.8,7.93,99900
2016-10-05,KESM,7.93,7.95,7.89,7.93,77500
2016-10-06,KESM,7.93,7.93,7.89,7.92,130600
2016-10-07,KESM,7.91,7.94,7.91,7.92,103000"""
df = pd.read_csv(StringIO(data), index_col='Date', parse_dates=True)

ax = plot_candlestick(df)

print(ax)

plt.tight_layout()
# plt.savefig("candle.png")
plt.show()
