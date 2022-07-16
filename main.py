##################### Normal Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib

MY_EMAIL = 'kodiugos@gmail.com'
PWD = 'llhytkakbfhnikci'
today = dt.datetime.now()
MONTH = today.month
DAY = today.day
letter_list = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
random_letter = random.choice(letter_list)
placeholder = '[NAME]'
# HINT 2: Use pandas to read the birthdays.csv
data_file = pd.read_csv('birthdays.csv')
birthday_dict = data_file.to_dict(orient='records')
print(birthday_dict)

for item in birthday_dict:
    name = item['name']
    email = item['email']
    year = item['email']
    month = item['month']
    day = item['day']
    if MONTH == month and DAY == day:
        with open(f'letter_templates/{random_letter}', mode='r') as letter:
            letter_body = letter.read()
            new_content = letter_body.replace(placeholder, name)
        with smtplib.SMTP('smtp.gmail.com') as connection:
            # Secure the connection
            connection.starttls()
            # login the user
            connection.login(user=MY_EMAIL, password=PWD)
            # send email
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f'Subject:Happy Birthday\n\n{new_content}'
            )

    else:
        print('No bodies birthday today!!!')
