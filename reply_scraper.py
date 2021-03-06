from selenium import webdriver
import time
import csv

def scraper(tweet,filename):
    ## web scraper
    twitter = "@"+tweet.split("/")[3]
    
    chromeOpt = webdriver.ChromeOptions()

    # chromeOpt.add_argument("--headless") ## close the UI
    driver = webdriver.Chrome(options=chromeOpt)
    heightBS = driver.execute_script("return document.body.scrollHeight") ## height before scroll
    driver.get(tweet)
    time.sleep(4)
    heightAS = driver.execute_script("return document.body.scrollHeight") ## height after scroll
    texts = []

    ## while web height before scroll is smaller than after
    while heightBS < heightAS:
        heightBS = heightAS
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        ## scrape texts in tag "span"
        spans = driver.find_elements_by_tag_name("span")
        for span in spans:
            texts.append(span.text)
        heightAS = driver.execute_script("return document.body.scrollHeight")
    driver.close()

    ## clean "#xxx"s, GIFs and "@xxx"s
    for i in range(len(texts)-1,-1,-1): ## reverse order to prevent out of range
        if texts[i] == "GIF" or texts[i] == "and":
            del texts[i]
        elif texts[i] != "":
            if texts[i][0] == "#" or (texts[i][0] == "@" and texts[i] != twitter):
                del texts[i]

    ## find all replies, that are:
    ## start after the specified user "@xxx"
    ## end before the first number (number of replies)
    print(len(texts))
    replies = []
    for j in range(len(texts)):
        if texts[j] == twitter:
            untilNum = 1
            reply = ""
            while j+untilNum < len(texts) and texts[j+untilNum].isdigit() == False and texts[j+untilNum] != "" and texts[j+untilNum] != " " and texts[j+untilNum] != "Quote tweet":
                reply += texts[j+untilNum]
                untilNum += 1
            if reply != "":
                replies.append(reply)

    ## clean duplicates and other things
    replies = sorted(set(replies), key = replies.index)
    for k in range(len(replies)-1,-1,-1):
        if "Privacy policy" in replies[k]:
            del replies[k]
    if replies != []:
        del replies[0]
    else:
        print("No reply found! Please check your twitter link.")

    with open(filename,"w",encoding='utf-8-sig',newline="") as file:
        write = csv.writer(file)
        # write the header
        for reply in replies:
            write.writerow([reply])

