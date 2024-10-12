import requests
import json

from send_email import send_email

api_key = "7b3c5cd21e2a457db2a883ab08ca391a"
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-09-12&sortBy=publishedAt&apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Treat strings to send email.
titles_descriptions = ["Title : " + str(article["title"]) + "\n" + 
					   "Description :" + str(article["description"]) + "\n\n" 
					   for article in content["articles"][0:20]]
message = "".join(titles_descriptions)

# generate messages and setup to send email.
username = "duck0249@gmail.com"
subject = "Today Daily news"
message = message

# Send email
send_email(username, subject, message)
 