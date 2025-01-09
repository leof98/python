# Day 32
# Learning about datetime and smtplib

from datetime import datetime
import pandas
import random
import smtplib

# EMAIL SETTINGS
MY_EMAIL = ""
PASSWORD = ""

now = datetime.now()
day = now.day
month = now.month
today = (now.day, now.month)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    bday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", bday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=bday_person['email'],
                            msg=f"Subject:Happy Birthday!\n\n{letter}")
