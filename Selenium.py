from selenium import webdriver
import time

## web scraper
# startTime = time.time()
chromeOpt = webdriver.ChromeOptions()
chromeOpt.add_argument("--headless") ## close the UI
driver = webdriver.Chrome(options=chromeOpt)
heightBS = driver.execute_script("return document.body.scrollHeight") ## height before scroll
driver.get("https://twitter.com/CDCgov/status/1392911350058323973")
# driver.get("https://twitter.com/thehill/status/1400119546078433284")
time.sleep(3)
heightAS = driver.execute_script("return document.body.scrollHeight") ## height after scroll
texts = []
## while web height before scroll is smaller than after
while heightBS < heightAS:
    heightBS = heightAS
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    ## scrape texts in tag "span"
    spans = driver.find_elements_by_tag_name("span")
    for span in spans:
        texts.append(span.text)
    heightAS = driver.execute_script("return document.body.scrollHeight")
driver.close()
# endTime = time.time()
# timeConsume = endTime - startTime


## clean "#xxx"s, GIFs and "@xxx"s
for i in range(len(texts)-1,-1,-1): ## reverse order to prevent out of range
    if texts[i] == "" or texts[i] == "GIF" or texts[i] == "和" or texts[i] == "and" or texts[i] == " ":
        del texts[i]
    elif texts[i][0] == "#" or (texts[i][0] == "@" and texts[i] != "@CDCgov"):
        del texts[i]


## find all replies, that are:
## start after the specified user "@xxx"
## end before the first number (number of replies)
replies = []
for j in range(len(texts)):
    if texts[j] == "@CDCgov":
        untilNum = 1
        reply = ""
        while j+untilNum < len(texts) and texts[j+untilNum].isdigit() == False:
            reply += texts[j+untilNum]
            untilNum += 1
        if reply != "":
            replies.append(reply)

## clean duplicates and ads
replies = sorted(set(replies), key = replies.index)
for k in range(len(replies)-1,-1,-1):
    if "©" in replies[k]:
        del replies[k]