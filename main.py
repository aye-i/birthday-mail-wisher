# Extra Hard Starting Project

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
from random import randint
import smtplib

my_email = "ENTER EMAIL HERE"
password = "ENTER PW HERE"

curr_date = dt.datetime.now()
curr_date_str = f"{curr_date.day}-{curr_date.month}"

bday_data = pandas.read_csv("./birthdays.csv")
bday_dict = bday_data.to_dict(orient="records")

for person in bday_dict:
    let_num = randint(1, 3)
    person_bday = f"{person['day']}-{person['month']}"
    if person_bday == curr_date_str:

        with open(f"./letter_templates/letter_{let_num}.txt") as letter_file:
            letter_data = letter_file.read()
            letter_data = letter_data.replace("[NAME]", person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=person['email'],
                                msg=f"Subject:Happy Birthday {person['name']}!\n\n{letter_data}")
