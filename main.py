"""
This code automatically sends a birthday email to your loved ones!
Note: Google has since disabled access to less secure apps
"""
import datetime as dt
import random
import smtplib
import pandas as pd

MY_EMAIL = "user@gmail.com"
MY_PASSWORD = "1234qwer()"

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        content = letter_file.read()
        new_content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{new_content}"
        )
