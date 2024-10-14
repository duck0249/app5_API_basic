import requests
import json

from send_email import send_email

api_key = "7b3c5cd21e2a457db2a883ab08ca391a"
language = "en"
topic = "telsa"

url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-09-15&sortBy=publishedAt&apiKey={api_key}&language={language}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# print(content)

# Treat strings to send email.
titles_descriptions = ["Title : " + str(article["title"]) + "\n" + 
					   "Description :" + str(article["description"]) + "\n" + 
					   "Link :" + str(article["url"]) + "\n\n"
					   for article in content["articles"][0:5]]

# Generate a meesage to send email.
message = "".join(titles_descriptions)

# generate messages and setup to send email.
username = "duck0249@gmail.com"
subject = "Today Daily news"
message = message

# Send email
send_email(username, subject, message)
