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


class Notification:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        """This function sends an SMS to admin"""
        message = self.client.messages.create(
            body=f"{message} - A3AJAGBE LOW FLIGHT FINDER",
            from_=os.environ.get('TWILIO_NUMBER'),
            to=os.environ.get('MY_NUMBER'),
        )
        print(message.status)

    def send_email(self, message, emails, google_flight_link):
        """This function sends an email to member"""
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=EMAIL, password=PASSWORD)
            for email in emails:
                conn.sendmail(from_addr=EMAIL,
                              to_addrs=email,
                              msg=f"Subject:New Low Flight Price!!!\n\n{message}\n{google_flight_link}".encode('utf-8')
                              )
