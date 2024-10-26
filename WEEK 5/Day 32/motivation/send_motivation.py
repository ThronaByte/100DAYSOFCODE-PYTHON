import random
import smtplib
import datetime as dt


MY_MAIL = "jadevictor247@gmail.com"
PASSWORD="YOUR-PASSWORD"

now = dt.datetime.now()
weekday = now.month
print(weekday)
if weekday == 5:
    with open('quotes.txt') as quote_file:
        all_quote = quote_file.readlines()
        quote= random.choice(all_quote)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs="thronabyte@gmail.com",
                            msg=f"Subject:It's Monday\n\n{quote}")

