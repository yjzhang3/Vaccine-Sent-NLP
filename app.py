# -*- coding: utf-8 -*-

from re import DEBUG
from PIL.Image import HAMMING
from flask import Flask, redirect, url_for, render_template, request, session, Response
import os
import io
import random
from matplotlib.pyplot import bar
import pandas as pd
import numpy as np
from reply_wordCloud import *
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from collections import Counter

app = Flask(__name__)

def retrieve_list_csv(csv):
    df = pd.read_csv(csv)

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

    print(bar_values)
    ## grab the behavioral attributes and their frequencies
    pie_labels = df.iloc[:,1].dropna().tolist()
    pie_freq = df.iloc[:,2].dropna().tolist()

    ## grab the emotional attributes and their frequencies
    pie_labels2 = df.iloc[:,3].dropna().tolist()
    pie_freq2 = df.iloc[:,4].dropna().tolist()

    return bar_labels, bar_values, pie_labels, pie_freq, pie_labels2, pie_freq2

# ======== Routing =========================================================== #
# -------- Login ------------------------------------------------------------- #
@app.route('/', methods=['GET', 'POST'])
def login():

    CA = []
    DE = []
    HA = []
    NJ = []
    NY = []
    OH = []
    WV = []

    CA.append(retrieve_list_csv("./csv/post-repliesCalifornia.csv"))
    DE.append(retrieve_list_csv("./csv/post-repliesDelaware.csv"))
    HA.append(retrieve_list_csv("./csv/post-repliesHawaii.csv"))
    NJ.append(retrieve_list_csv("./csv/post-repliesNew Jersey.csv"))
    NY.append(retrieve_list_csv("./csv/post-repliesNew York.csv"))
    OH.append(retrieve_list_csv("./csv/post-repliesOhio.csv"))
    WV.append(retrieve_list_csv("./csv/post-repliesWest Virginia.csv"))
    
    print(CA[0][1])
    return render_template('login.html', title='Bitcoin Monthly Price in USD', 
   CA=CA[0], DE= DE[0], HA=HA[0], NJ=NJ[0], NY=NY[0], OH=OH[0], WV=WV[0])

    # labels=bar_labels, values=bar_values, behav=pie_labels, behav_percent=pie_freq,
    # emot = pie_labels2, emot_percent = pie_freq2

# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")
