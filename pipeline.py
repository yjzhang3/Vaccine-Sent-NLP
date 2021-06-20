from reply_scraper import scraper
from reply_NLP import *
from reply_wordCloud import *
from collections import Counter
import itertools
import csv
tweet_list = ["https://twitter.com/therecount/status/1392853246725791745",
              "https://twitter.com/DE_MisesCaucus/status/1397239498111655947",
              "https://twitter.com/GavinNewsom/status/1398025553274277890",
              "https://twitter.com/GavinNewsom/status/1398025553274277890",
              "https://twitter.com/thehill/status/1400119546078433284",
              "https://twitter.com/HawaiiNewsNow/status/1402677284348338177",
              "https://twitter.com/HawaiiNewsNow/status/1402677284348338177"]
state_name = ["New York","Delaware","California","Ohio","West Virginia","Hawaii","New Jersey"]
f1 = "replies" + state_name[1] + ".csv"
f2 = "post-replies" + state_name[1] + ".csv"
scraper(tweet_list[1],f1)
[l1,l2,l3] = Sent(f1)

scores = sorted(l1) # sort from least to most
c1 = Counter(l2)
c2 = Counter(l3)

behav_traits = []
emot_traits = []
behav_freq = []
emot_freq = []

for key in c1.items():
    behav_traits.append(key[0])
    behav_freq.append(key[1])

for key in c2.items():
    emot_traits.append(key[0])
    emot_freq.append(key[1])

rows = zip(scores,behav_traits,behav_freq,emot_traits,emot_freq)
with open(f2, "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)


def driver(t_list,s_list):
    for num in range(len(t_list)):
        f1 = "replies" + state_name[num] + ".csv"
        f2 = "post-replies" + state_name[num] + ".csv"
        scraper(tweet_list[num],f1) # scrape
        [l1,l2,l3] = Sent(f1) # analysis results

        scores = sorted(l1) # sort from least to most
        c1 = Counter(l2) # count unique elements and frequency
        c2 = Counter(l3)

        behav_traits = []
        emot_traits = []
        behav_freq = []
        emot_freq = []

        # generate two lists, one with traits, one with frequencies
        for key in c1.items():
            behav_traits.append(key[0])
            behav_freq.append(key[1])

        for key in c2.items():
            emot_traits.append(key[0])
            emot_freq.append(key[1])

        rows = zip(scores,behav_traits,behav_freq,emot_traits,emot_freq)
        with open(f2, "w") as f:
            writer = csv.writer(f)
            for row in rows:
                writer.writerow(row)




        
