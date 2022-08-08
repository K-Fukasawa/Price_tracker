
#1 Extract data from internet (URL, API setup)

import requests
from bs4 import BeautifulSoup

# Data extraction for LTO7 @Backupworks
# FUJI
URL = "https://www.backupworks.com/Fujifilm-LTO-7-tape-media-16456574.aspx"
pageBWFFL7 = requests.get(URL)
soup = BeautifulSoup(pageBWFFL7.content, "html.parser")
priceBWFFL7 = soup.find("span", class_="prod-detail-cost-value").text
# HPE
URL = "https://www.backupworks.com/HP-LTO-7-tape-cartridge-C7977A.aspx"
pageBWHPEL7 = requests.get(URL)
soup = BeautifulSoup(pageBWHPEL7.content, "html.parser")
priceBWHPEL7 = soup.find("span", class_="prod-detail-cost-value").text
# QTM
URL = "https://www.backupworks.com/Quantum-LTO-7-tape-cartridge-MR-L7MQN-01.aspx"
pageBWQTML7 = requests.get(URL)
soup = BeautifulSoup(pageBWQTML7.content, "html.parser")
priceBWQTML7 = soup.find("span", class_="prod-detail-cost-value").text
# IBM
URL = "https://www.backupworks.com/IBM-LTO-7-tape-media-38L7302.aspx"
pageBWIBML7 = requests.get(URL)
soup = BeautifulSoup(pageBWIBML7.content, "html.parser")
priceBWIBML7 = soup.find("span", class_="prod-detail-cost-value").text

# Data extraction for LTO7 @Tape4Backup
# FUJI
URL = "https://www.tape4backup.com/collections/lto-7-tapes/products/fuji-16456574-nr-lto-7-data-backup-tape-new-repacked"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bFFL7_3 = soup.find("span", class_="price")
pricet4bFFL7_2 = list(pricet4bFFL7_3.stripped_strings)
pricet4bFFL7 = "\n\n".join(pricet4bFFL7_2) #if pricet4bFFL7_2 else ""
# HPE
URL = "https://www.tape4backup.com/collections/lto-7-tapes/products/hpe-c7977a-nr-lto-7-data-backup-tape-new-repacked"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bHPEL7_3 = soup.find("span", class_="price")
pricet4bHPEL7_2 = list(pricet4bHPEL7_3.stripped_strings)
pricet4bHPEL7 = "\n\n".join(pricet4bHPEL7_2) #if pricet4bHPEL7_2 else ""
# QTM
URL = "https://www.tape4backup.com/collections/lto-7-tapes/products/quantum-lto-7-data-backup-tape-new-repacked"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bQTML7_3 = soup.find("span", class_="price")
pricet4bQTML7_2 = list(pricet4bQTML7_3.stripped_strings)
pricet4bQTML7 = "\n\n".join(pricet4bQTML7_2) #if pricet4bQTML7_2 else ""
# IBM
URL = "https://www.tape4backup.com/collections/lto-7-tapes/products/ibm-38l7302-nr-lto-7-data-backup-tape-new-repacked"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bIBML7_3 = soup.find("span", class_="price")
pricet4bIBML7_2 = list(pricet4bIBML7_3.stripped_strings)
pricet4bIBML7 = "\n\n".join(pricet4bIBML7_2) #if pricet4bIBML7_2 else ""

# Data extraction for LTO7 @Tape&Media
# FUJI
URL = "https://tapeandmedia.com/fuji-lto-7-tape-ultrium-tapes.asp"
pagetamFFL7 = requests.get(URL)
soup = BeautifulSoup(pagetamFFL7.content, "html.parser")
pricetamFFL7 = soup.find("span", class_="price price--withoutTax price--main").text
# HPE
URL = "https://tapeandmedia.com/hp-lto-7-tape-ultrium-tapes-c7977a.asp"
pagetamHPEL7 = requests.get(URL)
soup = BeautifulSoup(pagetamHPEL7.content, "html.parser")
pricetamHPEL7 = soup.find("span", class_="price price--withoutTax price--main").text
# QTM
URL = "https://tapeandmedia.com/quantum-lto-7-tape-ultrium.asp"
pagetamQTML7 = requests.get(URL)
soup = BeautifulSoup(pagetamQTML7.content, "html.parser")
pricetamQTML7 = soup.find("span", class_="price price--withoutTax price--main").text
# IBM
URL = "https://tapeandmedia.com/ibm-lto-7-tape-ultrium-tapes.asp"
pagetamIBML7 = requests.get(URL)
soup = BeautifulSoup(pagetamIBML7.content, "html.parser")
pricetamIBML7 = soup.find("span", class_="price price--withoutTax price--main").text


# Create list
L7price_list = [
    [priceBWFFL7, priceBWHPEL7, priceBWQTML7, priceBWIBML7],
    [pricet4bFFL7, pricet4bHPEL7, pricet4bQTML7, pricet4bIBML7],
    [pricetamFFL7, pricetamHPEL7, pricetamQTML7, pricetamIBML7]
]

index = ["BackupWorks", "Tape4Backup", "Tape&Media"]
columns = ["FUJI", "HPE", "QTM", "IBM"]


#2 Convert bs4 element into dataframe

import pandas as pd
df7 = pd.DataFrame(L7price_list, index=index,columns=columns)
# df7 = df7.replace({"FUJI":{"$":""}, "HPE":{"$":""}, "QTM":{"$":""}, "IBM":{"$":""}})
df7['FUJI'] = df7['FUJI'].str.replace("$","", regex=True).astype(float)
df7['HPE'] = df7['HPE'].str.replace("$","", regex=True).astype(float)
df7['QTM'] = df7['QTM'].str.replace("$","", regex=True).astype(float)
df7['IBM'] = df7['IBM'].str.replace("$","", regex=True).astype(float)
pd.options.display.float_format = "${:,.2f}".format


#3 Export data to excel spreadsheet
# import datetime
# writer = pd.ExcelWriter("internet_pricing_LTO7_{}.xlsx".format(pd.Timestamp.now().strftime("%Y-%m-%d")), engine = "xlsxwriter")
# df7.to_excel(writer, sheet_name="LTO7", startcol=0, startrow=1)
# 
# workbook = writer.book
# worksheet = writer.sheets["LTO7"]
# worksheet.write_string(0, 0, 'LTO7 Internet Pricing as of '+pd.Timestamp.now().strftime("%Y-%m-%d"))
# 
# format = workbook.add_format({"num_format": "$#,##0.00"})
# worksheet.set_column("A:A", 14, )
# worksheet.set_column("B:E", 10, format)
# 
# writer.save()

# df7 = pd.DataFrame(L7price_dict, index=index, columns=["Backup Works"])
# print(type(df7))
print("---------------------------------------")
print("LTO7 Pricing as of", pd.Timestamp.now().strftime("%Y-%m-%d")+":")
print(df7)
print("---------------------------------------")




## Product part #s

# LTO7: Fuji(16456574), HPE(C7977A), IBM(38L7302), QUANTUM(MR-L7MQN-01)
# LTO8: Fuji(16551221), HPE(Q2078A), IBM(01PL041), QUANTUM(MR-L8MQN-01)
# LTO9: Fuji(16659047), HPE(Q2079A), IBM(02XW568), QUANTUM(MR-L9MQN-01)


#3 Sortout Data



#4 Store onto excel(online) file


#5 Automate process using Heroku (monthly)


#6 Send update with URL by email (monthly)


#7 Add dashboard to email??