# This program executes all 3 programs for the 3 products,
# creates a combined excel file, and sends to specified email address.

# print("Timestamp:", timestamp.strftime("%Y-%m-%d, %H:%M"), timestamp.day_name())
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
