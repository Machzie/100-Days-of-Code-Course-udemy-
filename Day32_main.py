# Day 32 Project - Automated Birthday Email App

import smtplib
import datetime as dt
import random
import pandas as pd
import os

now = dt.datetime.now()
current_month = now.month
current_day = now.day

my_email = "********@gmail.com" # Note: email redacted for GitHub
my_password = "**********"  # Note: pw redacted for GitHub

letters_list = os.listdir("./letter_templates")
chosen_letter = random.choice(letters_list)

birthdays_df = pd.read_csv("birthdays.csv")

for index, row in birthdays_df.iterrows():
    if row['month'] == current_month and row['day'] == current_day:

        with open(f"./letter_templates/{chosen_letter}", "r") as file:
            bd_letter = file.read()
            bd_letter = bd_letter.replace("[NAME]", row['name'])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=row['email'],
                                msg=f"Subject:Happy birthday!\n\n{bd_letter}")
