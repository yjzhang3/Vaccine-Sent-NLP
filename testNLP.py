import os
os.environ["EAI_USERNAME"] = 'yjzhang3@bu.edu'
os.environ["EAI_PASSWORD"] = 'w8#BFmUg@A'

from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

text = "I appreciate the effort to put money back into our local economy but I'm still going to social distance and wait"

language = "en"

output = client.specific_resource_analysis(
    body={"document": {"text": text}}, 
    params={'language': language, 'resource': 'sentiment'
})

print("sentiment:", output.sentiment.overall)
