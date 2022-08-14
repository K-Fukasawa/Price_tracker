# Extract data from internet
import requests
from bs4 import BeautifulSoup

try:
    #1 Data extraction for LTO9 @Backupworks
    # QTM Bare HH Internal SAS
    URL = "https://www.backupworks.com/Quantum-LTO-9-internal-tape-drive-TD-L92AN-BR.aspx"
    page_bw_qtm_l9d = requests.get(URL)
    soup = BeautifulSoup(page_bw_qtm_l9d.content, "html.parser")
    price_bw_qtm_l9d = soup.find("span", class_="prod-detail-cost-value").text

except Exception as e:
    print(e, "LTO9 drive error")
    from send_error_msg import error_message
    error_message()

l9_price_list = [
    [price_bw_qtm_l9d]
]

index = ["BackupWorks"]
columns = ["QTM"]

import pandas as pd
df9d = pd.DataFrame(l9_price_list, index=index,columns=columns)
df9d['QTM'] = df9d['QTM'].str.replace("$","", regex=True).str.replace(",","", regex=True).astype(float)
pd.options.display.float_format = "${:,.0f}".format

print("---------------------------------------")
print("LTO9 Drive Pricing as of", pd.Timestamp.now().strftime("%Y-%m-%d")+":")
print(df9d)
print("---------------------------------------")

#Export data to excel spreadsheet
if __name__ == "__main__":
    import datetime
    writer = pd.ExcelWriter("internet_pricing_LTO9_drive_{}.xlsx".format(pd.Timestamp.now().strftime("%Y-%m-%d")))
    df9d.to_excel(writer, sheet_name="LTO9", startcol=0, startrow=1)

    workbook = writer.book
    worksheet = writer.sheets["LTO9"]
    worksheet.write_string(0, 0, 'LTO9 Internet Pricing as of '+pd.Timestamp.now().strftime("%Y-%m-%d"))

    format = workbook.add_format({"num_format": "$#,##0.00"})
    worksheet.set_column("A:A", 14, )
    worksheet.set_column("B:E", 10, format)

    writer.save()
