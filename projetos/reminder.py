'''
A script that sends a reminder email to the user
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def main():
    reminder = Reminder()
    reminder.send()
    
class Reminder:
    pass
    
    def send(self):
        pass


if __name__ == '__main__':
    main()
