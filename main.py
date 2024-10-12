import requests
import json

import smtplib, ssl

api_key = "7b3c5cd21e2a457db2a883ab08ca391a"
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-09-12&sortBy=publishedAt&apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
# print(content["articles"][0]["title"])

for article in content["articles"]:
	print(article["title"])
	print(article["description"])

