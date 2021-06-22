from reply_scraper import scraper
from reply_NLP import *
# from reply_wordCloud import *
from collections import Counter
from itertools import zip_longest
import csv
import pandas as pd
import os
import time

tweet_list = ["https://twitter.com/therecount/status/1392853246725791745",
              "https://twitter.com/DE_MisesCaucus/status/1397239498111655947",
              "https://twitter.com/GavinNewsom/status/1398025553274277890",
              "https://twitter.com/nytimes/status/1398028759534551041",
              "https://twitter.com/thehill/status/1400119546078433284",
              "https://twitter.com/HawaiiNewsNow/status/1402677284348338177",
              "https://twitter.com/GovMurphy/status/1389269510612467716"]

state_name = ["New York","Delaware","California","Ohio","West Virginia","Hawaii","New Jersey"]

# tweet_list = ["https://twitter.com/therecount/status/1392853246725791745"]
# state_name = ["New York"]

#analyzes sentiment scores, behavioral, and emotional traits
def post_analysis(t_list, s_list):

    results_state_list = []

    #iterating through twitter list
    for num in range(len(t_list)):
        
        #creation of csv files
        f1 = "./csv/replies" + state_name[num] + ".csv"
        f2 = "./csv/post-replies" + state_name[num] + ".csv"
        if need2Scrape(f1):
            scraper(tweet_list[num],f1) # scrape
        [l1,l2,l3] = Sent(f1) # analysis results

        scores = sorted(l1) 
        c1 = Counter(l2) # count unique elements and frequency 
        c2 = Counter(l3) 
        
        #lists that contain to hold all unique scores, behavior, emotional traits
        behav_traits = []
        emot_traits = []
        behav_freq = []
        emot_freq = [] 

        # generate two lists, one with traits, one with frequencies and append to csv
        # behavioral
        for key in c1.items():
            behav_traits.append(key[0])
            behav_freq.append(key[1])

        # emotional
        for key in c2.items():
            emot_traits.append(key[0])
            emot_freq.append(key[1])

        #creation of csv 
        with open(f2, "w", newline='') as f:
            writer = csv.writer(f)
            header = ["sent", "emot", "emot_f", "behav", "behav_f"]
            writer.writerow(header)
            for i1, i2, i3, i4, i5 in zip_longest(scores,behav_traits,behav_freq,emot_traits,emot_freq):
                writer.writerow([i1, i2, i3, i4, i5])
        
        print("Finished creation of CSV")    
        
        results_list = [scores, behav_traits, emot_traits, behav_freq, emot_freq]
        results_state_list.append(results_list)
    
    return results_state_list

# results_state = post_analysis(tweet_list , state_name)
# print (results_state)
# df = pd.read_csv(f2)
# print(df)

# col_1 = df.iloc[:,0].tolist()
# print(col_1)

def need2Scrape(filename):
    if os.path.isfile(filename) and time.time()-os.path.getmtime(filename) < 1180800:
        return False
    else:
        return True
