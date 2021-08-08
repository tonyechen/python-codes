import smtplib

sender = "anchen082016@gmail.com"
receiver = "anchen082016@gmail.com"
password = ""
subject = "Python email test"
body = "I wrote an email! :D"

message = f"""From: testing {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender, password)
print("Logged in...")

server.sendmail(sender, receiver, message)
print("Email has been sent!")