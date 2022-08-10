# This program combines the monthly price tracker with the email service.
# By uploading this program to an online server and have it run automatically,
# we can generate and send pricing reports without executing the program manually from command line.

# Generate report & excel file.

import os
import base64
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
import datetime
import pandas as pd

from price_tracker_L7 import df7
from price_tracker_L8 import df8
from price_tracker_L9 import df9

writer = pd.ExcelWriter("Internet_Pricing_All_{}.xlsx".format(pd.Timestamp.now().strftime("%Y-%m-%d")))
df7.to_excel(writer, sheet_name="LTO7", startcol=0, startrow=1)
df8.to_excel(writer, sheet_name="LTO8", startcol=0, startrow=1)
df9.to_excel(writer, sheet_name="LTO9", startcol=0, startrow=1)

workbook = writer.book

worksheet = writer.sheets["LTO7"]
worksheet.write_string(0, 0, 'LTO7 Internet Pricing as of '+pd.Timestamp.now().strftime("%Y-%m-%d"))
# worksheet.write_string(0, 0, 'LTO7 Internet Pricing as of '+pd.Timestamp.now().strftime("%Y-%m-%d"))
format = workbook.add_format({"num_format": "$#,##0.00"})
worksheet.set_column("A:A", 14, )
worksheet.set_column("B:E", 10, format)

worksheet = writer.sheets["LTO8"]
worksheet.write_string(0, 0, 'LTO8 Internet Pricing as of '+pd.Timestamp.now().strftime("%Y-%m-%d"))
# worksheet.write_string(0, 0, 'LTO8 Internet Pricing as of '+pd.Timestamp.now().strftime("%Y-%m-%d"))
format = workbook.add_format({"num_format": "$#,##0.00"})
worksheet.set_column("A:A", 14, )
worksheet.set_column("B:E", 10, format)

worksheet = writer.sheets["LTO9"]
worksheet.write_string(0, 0, 'LTO9 Internet Pricing as of '+pd.Timestamp.now().strftime("%Y-%m-%d"))
# worksheet.write_string(0, 0, 'LTO9 Internet Pricing as of '+pd.Timestamp.now().strftime("%Y-%m-%d"))
format = workbook.add_format({"num_format": "$#,##0.00"})
worksheet.set_column("A:A", 14, )
worksheet.set_column("B:E", 10, format)

writer.save()

print("_____________________________________________")

# Send created excel file using Sendgrid API

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")
RECIPIENT_EMAIL_ADDRESS = os.getenv("RECIPIENT_EMAIL_ADDRESS")

if RECIPIENT_EMAIL_ADDRESS and ("," in RECIPIENT_EMAIL_ADDRESS):
    RECIPIENT_EMAIL_ADDRESS = [email.strip() for email in RECIPIENT_EMAIL_ADDRESS.split(",")]

to_emails = RECIPIENT_EMAIL_ADDRESS #[("email@address1", "name2"), ("email@address2", "name2")]

message = Mail(
    from_email=SENDER_EMAIL_ADDRESS,
    to_emails=to_emails, is_multiple=True,
    subject="[Monthly LTO Internet Price Tracker] {}".format(pd.Timestamp.now().strftime("%Y-%m-%d")),
    html_content="<strong>LTO internet pricing report attached.</strong>"
)

with open("Internet_Pricing_All_{}.xlsx".format(pd.Timestamp.now().strftime("%Y-%m-%d")), "rb") as f:
    data = f.read()
    f.close()
encoded_file = base64.b64encode(data).decode()

attachedFile = Attachment(
    FileContent(encoded_file),
    FileName('Internet_Pricing_All_{}.xlsx'.format(pd.Timestamp.now().strftime("%Y-%m-%d"))),
    FileType('application/xlsx'),
    Disposition('attachment')
)

message.attachment = attachedFile

client = SendGridAPIClient(SENDGRID_API_KEY)
response = client.send(message)
print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
print(response.status_code) #> 202 indicates SUCCESS
