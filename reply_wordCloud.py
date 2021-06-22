import os
from expertai.nlapi.cloud.client import ExpertAiClient
import numpy as np
import matplotlib.pyplot as plt
import re
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from IPython.display import Image as im
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def word_cloud(csv_file):
    WORDS = []

    client = ExpertAiClient()
    language = "en"

    df= pd.read_csv(csv_file, names= ["text"], encoding= "UTF-8" )

    #removing "\n" in the text
    df['text'] = df['text'].apply(lambda x: x.replace("\n", "")if ("\n" in x) else x)    
    # Removing links
    df['links_removed'] =  df['text'].apply(lambda x: x[x.find(" ")+1: ] if ("http" in x) else x)
    df = df.drop(columns=['text'])

    #Dropping null rows
    df = df.replace("", np.nan)
    df = df.dropna(subset=['links_removed'])
    
    ##Word Cloud
    ##Using the key Phrase extraction feature
    All_sentences = list(df['links_removed'])
    for sentence in All_sentences:
        document = client.specific_resource_analysis(
            body={"document": {"text": sentence }}, 
            params={'language': language, 'resource': 'relevants'})
        for mainlemma in document.main_lemmas:
            WORDS.append(mainlemma.value)
      
    wc = WordCloud(background_color="white", max_words=2000)
    clean_string = ','.join(WORDS)
    wc.generate(clean_string)
    fig = plt.figure(figsize=(10,10))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    return fig