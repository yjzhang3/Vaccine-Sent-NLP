# -*- coding: utf-8 -*-

from re import DEBUG
from PIL.Image import HAMMING
from flask import Flask, render_template, request, session
from matplotlib.pyplot import bar
import pandas as pd
import numpy as np
from reply_wordCloud import *

app = Flask(__name__)

def retrieve_list_csv(csv):
    df = pd.read_csv(csv)

    ## grab list of sentiments and calculate range of all
    sentiment_list = df.iloc[:,0].tolist()
    
    bar_values = [0] * 20
    bar_labels = np.linspace(-100, 100, 21).tolist()

    # print(csv)
    
    #finding frequency of numbers within a range (range of 20 from -100 to 100)
    hist = np.histogram(sentiment_list, bins=bar_labels)
    bar_values = hist[0].tolist()
                     
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

    ##currently false to prevent webscraping in the beginning
    if False:
        post_analysis()

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
    
    return render_template('login.html', title='Sentiment Analysis', 
    CA=CA[0], DE= DE[0], HA=HA[0], NJ=NJ[0], NY=NY[0], OH=OH[0], WV=WV[0])

# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")
