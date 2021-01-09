import smtplib

my_email = "xxxxxxxxxx@gmail.com"
password = "xxxxxxxxxxxxxxxxxxxx"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #a way to secure our connection
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="xxxxxxxxxx@naver.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )
#

import datetime as dt
now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()

print(now)
print(year)
print(day_of_week)

date_of_birth = dt.datetime(year=1990, month=2, day=20, hour=4)
print(date_of_birth)