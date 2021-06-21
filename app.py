# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, render_template, request, session, Response
import os
import io
import random
import pandas as pd
import numpy as np
from ../reply_wordCloud.py import *
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from collections import Counter

app = Flask(__name__)
app.secret_key = os.urandom(12)  # Generic key for dev purposes only

#color array for background 
color = [
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(201, 203, 207, 0.2)'
    ]
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

    #finding frequency of numbers within a range (range of 20 from -100 to 100)
    for sentiment in sentiment_list:
        if sentiment < limit:
            bar_values[idx]+=1
        else:
            idx+=1
            limit = bar_labels[idx]

    ## grab the behavioral attributes and their frequencies
    pie_labels = df.iloc[:,1].dropna().tolist()
    pie_freq = df.iloc[:,2].dropna().tolist()

    ## grab the emotional attributes and their frequencies
    pie_labels2 = df.iloc[:,3].dropna().tolist()
    pie_freq2 = df.iloc[:,4].dropna().tolist()

    return render_template('login.html', title='Bitcoin Monthly Price in USD', 
    labels=bar_labels, values=bar_values, behav=pie_labels, behav_percent=pie_freq,
    emot = pie_labels2, emot_percent = pie_freq2)

# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    word_cloud("../repliesNew York.csv")
    # word_cloud("/csv/repliesNew York.csv") # when we clean up the structure
    return fig
