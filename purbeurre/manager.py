KEY = "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"
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail(to,subject,content):

    message = Mail(
        from_email='zwightfakezor@gmail.com',
        to_emails=to,
        subject=subject,
        html_content=content)
    try:
        sg = SendGridAPIClient(KEY)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(e.message)
        