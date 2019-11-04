from pandas_datareader import data
from datetime import datetime, timedelta
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN


def generate_plot(start=(datetime.today()-timedelta(days=60)), end=datetime.today(), company="AAPL"):

    start = start
    end = end
    company = data.DataReader(name=company, data_source="yahoo", start=start, end=end)

    p = figure(x_axis_type='datetime', width=1000, height=400, sizing_mode="scale_width")
    p.title.text = "Candlestick chart"
    p.grid.grid_line_alpha = 0.5

    hossa = company.index[company.Close > company.Open]
    bessa = company.index[company.Close < company.Open]
    stable = company.index[company.Close == company.Open]

    for day in hossa:
        p.segment(x0=day, y0=company.loc[day].High, x1=day, y1=company.loc[day].Low, color='black')
        p.quad(left=day - timedelta(hours=6), right=day + timedelta(hours=6),
               top=company.loc[day].Close, bottom=company.loc[day].Open, fill_color='green',
               line_color='black')

    for day in bessa:
        p.segment(x0=day, y0=company.loc[day].High, x1=day, y1=company.loc[day].Low, color='black')
        p.quad(left=day - timedelta(hours=6), right=day + timedelta(hours=6),
               top=company.loc[day].Open, bottom=company.loc[day].Close, fill_color='red',
               line_color='black')

    for day in stable:
        p.segment(x0=day, y0=company.loc[day].High, x1=day, y1=company.loc[day].Low, color='black')
        p.quad(left=day - timedelta(hours=6), right=day + timedelta(hours=6),
               top=company.loc[day].Open, bottom=company.loc[day].Close, fill_color='grey',
               line_color='black')

    js_script, div = components(p)
    cdn_js = CDN.js_files
    cdn_css = CDN.css_files

    return js_script, div, cdn_js, cdn_css
