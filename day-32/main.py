import smtplib

my_email = "ayushhsingh33@gmail.com"
password = "sHitDam@1708"

connection = smtplib.SMTP("smtp.google.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="ayushrajput1780@gmail.com", msg="hello")
connection.close()