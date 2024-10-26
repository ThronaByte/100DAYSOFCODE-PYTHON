import pandas
from smtplib import SMTP, SMTPException
from datetime import datetime
import random

MY_MAIL = "jadevictor247@gmail.com"
PASSWORD = "YOUR-PASSWORD"

birth = datetime.now()
birth_tuple = (birth.month, birth.day)

data = pandas.read_csv('birthdays.csv')
birth_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}


if birth_tuple in birth_dict:
    birthday_person = birth_dict[birth_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])
    try:
        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_MAIL,
                                to_addrs=birthday_person['email'],
                                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )

    except SMTPException as e:
        print(f"An error occurred: {e}")
