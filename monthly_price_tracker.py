# This program executes all 3 programs for the 3 products,
# creates a combined excel file, and sends to specified email address.

# execute all 3 py files:
exec(open("price_tracker_L7.py").read())
exec(open("price_tracker_L8.py").read())
exec(open("price_tracker_L9.py").read())



#3 Export data to excel spreadsheet

import datetime

timestamp = pd.Timestamp.now()
# print("Timestamp:", timestamp.strftime("%Y-%m-%d, %H:%M"), timestamp.day_name())

# from price_tracker_L7 import df7
# from price_tracker_L8 import df8
# from price_tracker_L9 import df9
# 
# writer = pd.ExcelWriter(f"internet_pricing_{timestamp}.xlsx", engine = "xlsxwriter")
# df7.to_excel(writer, sheet_name="LTO7")
# df8.to_excel(writer, sheet_name="LTO8")
# df9.to_excel(writer, sheet_name="LTO9")
# 
# workbook = writer.book
# worksheet = writer.sheets["LTO7"]
# worksheet = writer.sheets["LTO8"]
# worksheet = writer.sheets["LTO9"]
# 
# format = workbook.add_format({"num_format": "$#,##0.00"})
# worksheet.set_column("A:A", 14, )
# worksheet.set_column("B:E", 10, format)
# 
# writer.save()
