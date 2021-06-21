# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, render_template, request, session, Response
import os
import io
import random
import pandas as pd
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from collections import Counter



app = Flask(__name__)
app.secret_key = os.urandom(12)  # Generic key for dev purposes only

# Heroku
#from flask_heroku import Heroku
#heroku = Heroku(app)

# ======== Routing =========================================================== #
# -------- Login ------------------------------------------------------------- #
@app.route('/', methods=['GET', 'POST'])
def login():
    df = pd.read_csv("post-repliesNew York.csv")

    ## grab list of sentiments and calculate range of all
    sentiment_list = df.iloc[:,0].tolist()
    
    bar_values = [0] * 20
    bar_labels = np.linspace(-100, 100, 21).tolist()

    idx = 0
    limit = bar_labels[idx+1]

    for sentiment in sentiment_list:
        if sentiment < limit:
            bar_values[idx]+=1
        else:
            idx+=1
            limit = bar_labels[idx]

    ## grab the emotional attributes and their frequencies
    pie_labels = df.iloc[:,1].dropna().tolist()
    pie_freq = df.iloc[:,2].dropna().tolist()
   

    return render_template('login.html', title='Bitcoin Monthly Price in USD', labels=bar_labels, values=bar_values, behav=bar_labels, behav_percent=pie_freq)

# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")


# @app.route('/plot.png')
# def plot_png():
#     fig = create_figure()
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)
#     return Response(output.getvalue(), mimetype='image/png')

# def create_figure():
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     xs = range(100)
#     ys = [random.randint(1, 50) for x in xs]
#     axis.plot(xs, ys)
#     return fig

# labels = [
#     'JAN', 'FEB', 'MAR', 'APR',
#     'MAY', 'JUN', 'JUL', 'AUG',
#     'SEP', 'OCT', 'NOV', 'DEC'
# ]

# values = [
#     967.67, 1190.89, 1079.75, 1349.19,
#     2328.91, 2504.28, 2873.83, 4764.87,
#     4349.29, 6458.30, 9907, 16297
# ]

# @app.route('/bar')
# def bar():
#     bar_labels=labels
#     bar_values=values
#     return render_template('bar_chart.html', title='Bitcoin Monthly Price in USD', max=17000, labels=bar_labels, values=bar_values)

# @app.route('/line')
# def line():
#     line_labels=labels
#     line_values=values
#     return render_template('line_chart.html', title='Bitcoin Monthly Price in USD', max=17000, labels=line_labels, values=line_values)

# @app.route('/pie')
# def pie():
#     pie_labels = labels
#     pie_values = values
#     return render_template('pie_chart.html', title='Bitcoin Monthly Price in USD', max=17000, set=zip(values, labels, colors))