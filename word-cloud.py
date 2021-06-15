LINKS = []
HASH_TAGS = []
WORDS = []

import pandas as pd
import numpy as np
import os
os.environ["EAI_USERNAME"] = #username 
os.environ["EAI_PASSWORD"] = #password 

from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()
language = "en"

df= pd.read_csv("replies.csv")
df['tags_removed'] = df['text'].apply(lambda x : x[x.find(" ")+1: ]+" " )
df['tags_removed'] =  df['tags_removed'].apply(lambda x: x[x.find(" ")+1: ] if ("@" in x) else x)
for x in df['tags_removed']:
  if ("http" in x):
    link = x[x.find("http") : x.find(" ")+1]
    #print(link)
    LINKS.append(link)

df['links_removed'] =  df['tags_removed'].apply(lambda x: x[x.find(" ")+1: ] if ("http" in x) else x)
df = df.drop(columns=['tags_removed'])
df = df.replace("", np.nan)
df = df.dropna(subset=['links_removed'])

All_sentences = list(df['links_removed'])

for sentence in All_sentences:
  document = client.specific_resource_analysis(
    body={"document": {"text": sentence }}, 
    params={'language': language, 'resource': 'relevants'})
  for mainlemma in document.main_lemmas:
    WORDS.append(mainlemma.value)

import numpy as np
import matplotlib.pyplot as plt
import re
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from IPython.display import Image as im
mask = np.array(Image.open('/content/twitter mask.jpg'))
wc = WordCloud(background_color="white", max_words=2000, mask=mask)
clean_string = ','.join(WORDS)
plt.figure(figsize=(20,20))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

