# app/email_service.py

import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")


def send_email(subject="[Daily Briefing] This is a test", html="<p>Hello World</p>", recipient_address=SENDER_EMAIL_ADDRESS):
    """
    Sends an email with the specified subject and html contents to the specified recipient,

    If recipient is not specified, sends to the admin's sender address by default.
    """
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))
    print("SUBJECT:", subject)
    #print("HTML:", html)

    message = Mail(from_email=SENDER_EMAIL_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html)
    try:
        response = client.send(message)
        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        return response
    except Exception as e:
        print("OOPS", type(e), e)
        return None


if __name__ == "__main__":
    example_subject = "[Daily Briefing] This is a test"

    example_html = f"""
    <h3>This is a test of the Daily Briefing Service</h3>

    <h4>Today's Date</h4>
    <p>Monday, January 1, 2040</p>

    <h4>My Stocks</h4>
    <ul>
        <li>MSFT | +3%</li>
        <li>GOOG | +2%</li>
        <li>AAPL | +4%</li>
    </ul>

    <h4>My Forecast</h4>
    <ul>
        <li>10:00 AM | 65 DEGREES | CLEAR SKIES</li>
        <li>01:00 PM | 70 DEGREES | CLEAR SKIES</li>
        <li>04:00 PM | 75 DEGREES | CLEAR SKIES</li>
        <li>07:00 PM | 67 DEGREES | PARTLY CLOUDY</li>
        <li>10:00 PM | 56 DEGREES | CLEAR SKIES</li>
    </ul>
    """

    send_email(example_subject, example_html)
