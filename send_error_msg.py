# app/email_service.py

import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")

def error_message():
    error_html = f"""
        <html>
          <body>
    
            <b> Exception Details: </b> Exception: {exception}
            <b>
                {message}
            </b>
    
          </body>
        </html>
        """

    error_msg = Mail(from_email=SENDER_EMAIL_ADDRESS, 
                        to_emails=SENDER_EMAIL_ADDRESS,
                        subject="Error Message: LTO Pricing Tracker", 
                        html_content=error_html)
    
    client = SendGridAPIClient(SENDGRID_API_KEY)
    response = client.send(error_msg)
    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
    print(response.status_code) #> 202 indicates SUCCESS

error_message()