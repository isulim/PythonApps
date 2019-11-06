"""
Smallest possible website made in Flask, deployed on Heroku.
[Heroku deploy](https://morning-harbor-41773.herokuapp.com/)
"""

from flask import Flask, render_template

from pandas_datareader import data
from datetime import datetime, timedelta
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/chart')
def chart():
    start = datetime.today() - timedelta(days=60)
    end = datetime.today()
    company = data.DataReader(name="GOOG", data_source="yahoo", start=start, end=end)

    p = figure(x_axis_type='datetime', width=1000, height=400, sizing_mode="scale_width")
    p.title.text = "Google Financial Data"
    p.title.text_font_size = '20pt'
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
    cdn_js = CDN.js_files[0]

    return render_template('chart.html', js_script=js_script, div=div, cdn_js=cdn_js)


if __name__ == "__main__":
    app.run(debug=True)
