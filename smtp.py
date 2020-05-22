import smtplib

fromaddr = "rwithik@gmail.com"
toaddr = "rwithik@cet.ac.in"
print(f"From: {fromaddr}")
print(f"To: {toaddr}")
print(f"Subject: SMTP e-mail test")
print(f"Body: This is a test e-mail message.")

msg = """From: From Person <rwithik@gmail.com>
To: To Person <rwithik@cet.ac.in>
Subject: SMTP e-mail test

This is a test e-mail message.
"""


server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, "password")
server.sendmail(fromaddr, toaddr, msg)
print("Mail sent")
