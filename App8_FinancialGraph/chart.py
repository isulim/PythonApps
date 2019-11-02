from pandas_datareader import data
from datetime import datetime, timedelta
from bokeh.plotting import figure, show, output_file

start = datetime(2019, 3, 1)
end = datetime(2019, 10, 10)
apple = data.DataReader(name="AAPL", data_source="yahoo", start=start, end=end)

p = figure(x_axis_type='datetime', width=1000, height=400, sizing_mode="scale_width")
p.title.text = "Candlestick chart"
p.grid.grid_line_alpha = 0.5

hossa = apple.index[apple.Close > apple.Open]
bessa = apple.index[apple.Close < apple.Open]
stable = apple.index[apple.Close == apple.Open]

for day in hossa:
    p.segment(x0=day, y0=apple.loc[day].High, x1=day, y1=apple.loc[day].Low, color='black')
    p.quad(left=day - timedelta(hours=6), right=day + timedelta(hours=6),
           top=apple.loc[day].Close, bottom=apple.loc[day].Open, fill_color='green',
           line_color='black')

for day in bessa:
    p.segment(x0=day, y0=apple.loc[day].High, x1=day, y1=apple.loc[day].Low, color='black')
    p.quad(left=day - timedelta(hours=6), right=day + timedelta(hours=6),
           top=apple.loc[day].Open, bottom=apple.loc[day].Close, fill_color='red',
           line_color='black')

for day in stable:
    p.segment(x0=day, y0=apple.loc[day].High, x1=day, y1=apple.loc[day].Low, color='black')
    p.quad(left=day - timedelta(hours=6), right=day + timedelta(hours=6),
           top=apple.loc[day].Open, bottom=apple.loc[day].Close, fill_color='grey',
           line_color='black')

output_file('CS.html')
show(p)
