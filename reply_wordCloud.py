# -*- coding: utf-8 -*-

from datetime import datetime
startTime = datetime.now()

LINKS = []
HASH_TAGS = []

WORDS = []

import os

from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()
language = "en"

import numpy as np
import matplotlib.pyplot as plt
import re
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from IPython.display import Image as im

import pandas as pd
import numpy as np

def word_cloud(csv_file):

  df= pd.read_csv(csv_file)

  #df['no_of_mentions'] = df['text'].str.count("@")

  df['tags_removed'] = df['text'].apply(lambda x : x[x.find(" ")+1: ]+" " )
  """## Removing Mentions"""
  df['tags_removed'] =  df['tags_removed'].apply(lambda x: x[x.find(" ")+1: ] if ("@" in x) else x)
  """### Removing links"""
  #for x in df['text']:
  for x in df['tags_removed']:
    if ("http" in x):
      link = x[x.find("http") : x.find(" ")+1]
      #print(link)
      LINKS.append(link)

  df['links_removed'] =  df['tags_removed'].apply(lambda x: x[x.find(" ")+1: ] if ("http" in x) else x)
  df = df.drop(columns=['tags_removed'])
  """Dropping null rows"""
  #countinh the str len in each row
  # df['links_removed'].apply(lambda x: len(x))
  df = df.replace("", np.nan)
  df = df.dropna(subset=['links_removed'])
  ## Word Cloud
  ###**Using the key Phrase extraction feature**
  All_sentences = list(df['links_removed'])
  #All_sentences
  for sentence in All_sentences:
    document = client.specific_resource_analysis(
      body={"document": {"text": sentence }}, 
      params={'language': language, 'resource': 'relevants'})
    for mainlemma in document.main_lemmas:
      WORDS.append(mainlemma.value)
 
  #mask = np.array(Image.open(r'C:\Users\Pravallika Myneni\Desktop\Vaccine-Sent-NLP-word-cloud\twitter mask.jpg'))

  wc = WordCloud(background_color="white", max_words=2000)
  clean_string = ','.join(WORDS)
  wc.generate(clean_string)

  fig = plt.figure(figsize=(10,10))
  plt.imshow(wc, interpolation='bilinear')
  plt.axis("off")
  plt.show()
  return fig

  #print(datetime.now() - startTime)

#word_cloud("replies-post.csv")
