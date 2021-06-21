from reply_scraper import scraper
from reply_NLP import *
# from reply_wordCloud import *
from collections import Counter
import itertools
import csv

# tweet_list = ["https://twitter.com/therecount/status/1392853246725791745",
#               "https://twitter.com/DE_MisesCaucus/status/1397239498111655947",
#               "https://twitter.com/GavinNewsom/status/1398025553274277890",
#               "https://twitter.com/GavinNewsom/status/1398025553274277890",
#               "https://twitter.com/thehill/status/1400119546078433284",
#               "https://twitter.com/HawaiiNewsNow/status/1402677284348338177",
#               "https://twitter.com/HawaiiNewsNow/status/1402677284348338177"]

# state_name = ["New York","Delaware","California","Ohio","West Virginia","Hawaii","New Jersey"]

tweet_list = ["https://twitter.com/therecount/status/1392853246725791745"]
state_name = ["New York"]

#driver produces the csvs that has sentiment scores, traits, and frequencies
def create_css_results(t_list, s_list):

    results_state_list = []

    #iterationg through twitter list
    for num in range(len(t_list)):
        
        #creation of csv files
        f1 = "replies" + state_name[num] + ".csv"
        f2 = "post-replies" + state_name[num] + ".csv"
        scraper(tweet_list[num],f1) # scrape
        [l1,l2,l3] = Sent(f1) # analysis results

        scores = sorted(l1) 
        c1 = Counter(l2) # count unique elements and frequency 
        c2 = Counter(l3) 
        # (neurtral, 2), (addiction, 3)....
        
        behav_traits = []
        emot_traits = []
        behav_freq = []
        emot_freq = [] #13 rows

        # generate two lists, one with traits, one with frequencies and append to csv
        # behavioral
        for key in c1.items():
            behav_traits.append(key[0])
            behav_freq.append(key[1])

        # emotional
        for key in c2.items():
            emot_traits.append(key[0])
            emot_freq.append(key[1])

        ## note: zip cuts off/chops off by the shortest list, check for options for preservation
        rows = zip(scores,behav_traits,behav_freq,emot_traits,emot_freq)

        #creation of csv 
        with open(f2, "w") as f:
            writer = csv.writer(f)
            for row in rows:
                writer.writerow(row)

        print("Finished creation of CSV")    
        
        results_list = [scores, behav_traits, emot_traits, behav_freq, emot_freq]
        results_state_list.append(results_list)
    
    return results_state_list


create_css_results(tweet_list , state_name)
