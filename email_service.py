# app/email_service.py

import os
import base64
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
import datetime
import pandas as pd

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")
RECIPIENT_EMAIL_ADDRESSES = os.getenv("RECIPIENT_EMAIL_ADDRESSES")

# Test HTML
test_html = f"""
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

to_emails = RECIPIENT_EMAIL_ADDRESSES #[("email@address1", "name2"), ("email@address2", "name2")]

message = Mail(
    from_email=SENDER_EMAIL_ADDRESS,
    to_emails=to_emails, is_multiple=True,
    subject="[Monthly LTO Internet Price Tracker] {}".format(pd.Timestamp.now().strftime("%Y-%m-%d")),
    html_content="<strong>this is a test</strong>" #test_html
)

with open("Internet_Pricing_All_2022-08-09.xlsx", "rb") as f:
    data = f.read()
    f.close()
encoded_file = base64.b64encode(data).decode()

attachedFile = Attachment(
    FileContent(encoded_file),
    FileName('Internet_Pricing_All_{}.xlsx'.format(pd.Timestamp.now().strftime("%Y-%m-%d"))),
    FileType('application/xlsx'),
    Disposition('attachment')
)

# "Internet_Pricing_All_{}.xlsx".format(pd.Timestamp.now().strftime("%Y-%m-%d"))

message.attachment = attachedFile

client = SendGridAPIClient(SENDGRID_API_KEY)
response = client.send(message)
print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
print(response.status_code) #> 202 indicates SUCCESS


# send_email(example_subject, example_html)

# def send_email(subject="This is a test", html="<p>Hello World</p>", recipient_address=SENDER_EMAIL_ADDRESS):
# 
#     client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
#     print("CLIENT:", type(client))
#     print("SUBJECT:", subject)
#     #print("HTML:", html)
# 
#     message = Mail(from_email=SENDER_EMAIL_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html)
#     try:
#         response = client.send(message)
#         print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
#         print(response.status_code) #> 202 indicates SUCCESS
#         return response
#     except Exception as e:
#         print("OOPS", type(e), e)
#         return None


#if __name__ == "__main__":
#    example_subject = "[Daily Briefing] This is a test"
#
#    example_html = f"""
#    <h3>This is a test of the Daily Briefing Service</h3>
#
#    <h4>Today's Date</h4>
#    <p>Monday, January 1, 2040</p>
#
#    <h4>My Stocks</h4>
#    <ul>
#        <li>MSFT | +3%</li>
#        <li>GOOG | +2%</li>
#        <li>AAPL | +4%</li>
#    </ul>
#
#    <h4>My Forecast</h4>
#    <ul>
#        <li>10:00 AM | 65 DEGREES | CLEAR SKIES</li>
#        <li>01:00 PM | 70 DEGREES | CLEAR SKIES</li>
#        <li>04:00 PM | 75 DEGREES | CLEAR SKIES</li>
#        <li>07:00 PM | 67 DEGREES | PARTLY CLOUDY</li>
#        <li>10:00 PM | 56 DEGREES | CLEAR SKIES</li>
#    </ul>
#    """
#
#    send_email(example_subject, example_html)