import smtplib, ssl
import os
from email.mime.text import MIMEText

HOST = "smtp.gmail.com"
PORT = "465"


def send_email(username, subject, message):


	# username = "duck0249@gmail.com"
	password = os.getenv("PASSWORD_GOOGLE")

	message = MIMEText(message, _charset="UTF-8")
	message["Subject"] = "Daily News"
	message["From"] = username
	receiver = "duck0249@gmail.com"
	message["To"] = receiver
	
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
		server.login(username, password)
		server.sendmail(username, receiver, message.as_string())

	print("Email sent successfully.")

# if __name__ == "__main__":
# 	sending_email("duck0249@naver.com", "Hello, it is the test.")
