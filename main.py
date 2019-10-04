from smtplib import SMTP
import csv
from global_variables import *
from definitions.definitions import *


def main():
    with open('./emails.csv', 'r') as email_list:
        new_email_list = csv.reader(email_list)

        with SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login('<email>', '<password>')
            subject = EMAIL_SUBJECT[0]

            for fname, lname, email in new_email_list:
                create_login(fname, lname)

                body = email_greeting % fname + '\n\n' + \
                       email_body + '\n\n' + \
                       email_closing % site_hyperlinks[0] + '\n' + \
                       email_user_credentials % (create_login(fname, lname), create_password(fname, lname)) + '\n\n' + \
                       email_time_period + '\n' + \
                       signature

                msg = f'Subject: {subject}\n\n{body}'

                smtp.sendmail('<from email>', email, msg)


if __name__ == '__main__':
    main()
