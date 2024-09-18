# without API
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] =  # "Your Name"
email["to"] =  # "Email of who you wish to send to"
email["subject"] = "This email is from Python!"

email.set_content(html.substitute({"name": "Dilesh"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(  # "Your Email", "Email of who you wish to send to")
    smtp.send_message(email)
    print("Email sent!")
