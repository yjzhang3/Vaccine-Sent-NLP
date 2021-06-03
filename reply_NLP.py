import pandas as pd
import os
os.environ["EAI_USERNAME"] = 'yjzhang3@bu.edu'
os.environ["EAI_PASSWORD"] = 'w8#BFmUg@A'

from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()
language = "en"


df = pd.read_csv("replies.csv")
df["sentiment score"] = ""
score=[]

for index, row in df.iterrows():
    text = row['text'].encode("ascii", "ignore") # make sure all characters are unicode
    #print(text)
    output = client.specific_resource_analysis(
        body={"document": {"text": str(text)}}, 
        params={'language': language, 'resource': 'sentiment'
    })
    #print("sentiment:", output.sentiment.overall)
    score.append(output.sentiment.overall)

df["sentiment score"]= score
df.to_csv("replies_wscore.csv")

