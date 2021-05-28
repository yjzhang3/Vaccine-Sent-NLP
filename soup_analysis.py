from expertai.nlapi.cloud.client import ExpertAiClient
from bs4 import BeautifulSoup
import requests
import re

# extracting from reuter article on the hamas and palestine
URL = "https://www.reuters.com/world/middle-east/gaza-truce-between-israel-hamas-begins-mediated-by-egypt-2021-05-20/" 
# extracting from reuter article on the hamas and palestine
URL2 = "https://en.wikipedia.org/wiki/Israel"

response = requests.get(URL2)
# need to install lxml
soup = BeautifulSoup(response.text, 'lxml')

article_searches = soup.find_all(text = re.compile("israel"))

line_num = 1
for search_result in article_searches:
    print(str(line_num), end = " ")
    print(search_result, end='\n\n')
    line_num+=1 


# sentiment analysis
client = ExpertAiClient()

title = soup.select("#firstHeading")[0].text
paragraphs = soup.select("p")

counter = 0
for para in paragraphs:
    print(counter)
    print (para.text)
    counter += 1

print(counter)

## issue with reading there is some characters that it cannot read

total_body = '\n'.join([para.text for para in paragraphs[0:10]])

text = total_body

language= 'en'

output = client.specific_resource_analysis(
    body={"document": {"text": text}}, 
    params={'language': language, 'resource': 'sentiment'
})

# Output overall sentiment

print("Output overall sentiment:")
print(output.sentiment.overall)


# Response status code: 413
# Traceback (most recent call last):
#   File "/Users/jennasun/Desktop/NLP/soup_analysis.py", line 46, in <module>
#     output = client.specific_resource_analysis(
#   File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/expertai/nlapi/cloud/client.py", line 118, in specific_resource_analysis
#     return self.process_response(response)
#   File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/expertai/nlapi/cloud/client.py", line 80, in process_response
#     raise ExpertAiRequestError(
# expertai.nlapi.common.errors.ExpertAiRequestError: Response status code: 413