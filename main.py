import datetime as dt
import random
import smtplib
import pandas
# my_email = "jujubala2022@gmail.com"
# password = "8a9b50eh9080hosJuJu"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email , password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="persianprogrammar@gmail.com", msg="Subject:Hello\n\nthis is body of my email")
#     connection.close()

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2001, month=9, day=9)


##########################  Monday Motivation #################################
#
# my_email = "jujubala2022@gmail.com"
# password = "8a9b50eh9080hosJuJu"
# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 1:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#
#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, to_addrs="persianprogrammar@gmail.com", msg=f"Subject: Monday Motivation\n\n{quote}")
#         connection.close()