import pandas as pd
import os
from csv import reader

import matplotlib.pyplot as plt
plt.style.use('ggplot')

from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()
language = "en"


### all NLP analysis ###
def Sent(f1):

    #create lists to hold score, behavioral, and emotional triats
    score=[]
    taxonomy1 = 'behavioral-traits'
    cat1=[]
    taxonomy2 = 'emotional-traits'
    cat2=[]
    
    #open file and read each row of tweet csv
    with open(f1,'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            print(row)

            ## find sentiment scores and appending to score ## 
            output = client.specific_resource_analysis(
                body={"document": {"text": str(row)}}, 
                params={'language': language, 'resource': 'sentiment'
                })
            score.append(output.sentiment.overall)

            ## finding behavioral and appending to cat1 ##
            
            output = client.classification(
                    body={"document": {"text": str(row)}}, 
                    params={'taxonomy': taxonomy1, 'language': language})

            if len(output.categories) == 0:
                print("Neutral")
                cat1.append("Neutral")
            else:
                for i in output.categories:
                    print(i.hierarchy)
                    cat1.append(i.hierarchy[2])

            ## finding emotional and appending to cat2 ##
            output = client.classification(
                    body={"document": {"text": str(row)}}, 
                    params={'taxonomy': taxonomy2, 'language': language})

            if len(output.categories) == 0:
                print("Neutral")
                cat2.append("Neutral")
                
            else:
                for i in output.categories:
                    print(i.hierarchy)
                    cat2.append(i.hierarchy[1])

    return score,cat1,cat2


