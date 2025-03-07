import requests

url = "http://127.0.0.1:8000/summarize"
data = {"text": "The rapid advancement of artificial intelligence has sparked widespread discussions about its potential impact on society. From automating mundane tasks to revolutionizing healthcare and transportation, AI's capabilities are vast and constantly evolving. However, concerns about job displacement, ethical considerations, and the potential for misuse also loom large. Experts emphasize the importance of responsible development and deployment of AI technologies, advocating for robust regulatory frameworks and ongoing dialogue to ensure that AI benefits humanity as a whole. Furthermore, the need for increased public understanding of AI's capabilities and limitations is crucial to mitigate fears and foster informed decision-making. As AI continues to integrate into our daily lives, its influence will undoubtedly shape the future in profound ways."}
response = requests.post(url, json=data)
print(response.json())  # Prints the summarized text
