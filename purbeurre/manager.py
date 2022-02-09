from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

KEY = os.environ.get("SENDGRID_API_KEY")
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python


def send_mail(to, subject, content):
    message = Mail(
        from_email="zwightfakezor@gmail.com",
        to_emails=to,
        subject=subject,
        html_content=content,
    )
    try:
        sg = SendGridAPIClient(KEY)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(e.message)
