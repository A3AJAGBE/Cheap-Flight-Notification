import os
from twilio.rest import Client
import smtplib
from dotenv import load_dotenv
load_dotenv()

# Twilio configs
ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

# Email config
EMAIL = os.environ.get('GMAIL')
PASSWORD = os.environ.get('GMAIL_PASS')
RECEIVER_EMAIL = os.environ.get('YMAIL')


class Notification:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        """This function sends an SMS"""
        message = self.client.messages.create(
            body=f"{message} - A3AJAGBE LOW FLIGHT FINDER",
            from_=os.environ.get('TWILIO_NUMBER'),
            to=os.environ.get('MY_NUMBER'),
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_email(self, message):
        """This function sends an email"""
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=EMAIL, password=PASSWORD)
            conn.sendmail(from_addr=EMAIL,
                          to_addrs=RECEIVER_EMAIL,
                          msg=f"Subject:Low flight price Notification\n\n{message}")
