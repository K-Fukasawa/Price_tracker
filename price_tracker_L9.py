
#1 Extract data from internet (URL, API setup)

import requests
from bs4 import BeautifulSoup

# Data extraction for LTO9 @Backupworks
# FUJI
URL = "https://www.backupworks.com/FujiFilm-LTO-9-Tape-Media-16659047.aspx"
pageBWFFL9 = requests.get(URL)
soup = BeautifulSoup(pageBWFFL9.content, "html.parser")
priceBWFFL9 = soup.find("span", class_="prod-detail-cost-value").text
# HPE
URL = "https://www.backupworks.com/HP-LTO-9-Tape-Media-Q2079A.aspx"
pageBWHPEL9 = requests.get(URL)
soup = BeautifulSoup(pageBWHPEL9.content, "html.parser")
priceBWHPEL9 = soup.find("span", class_="prod-detail-cost-value").text
# QTM
URL = "https://www.backupworks.com/Quantum-LTO-9-Tape-media-MR-L9MQN-01.aspx"
pageBWQTML9 = requests.get(URL)
soup = BeautifulSoup(pageBWQTML9.content, "html.parser")
priceBWQTML9 = soup.find("span", class_="prod-detail-cost-value").text
# IBM
URL = "https://www.backupworks.com/IBM-LTO-9-tape-media-02XW568.aspx"
pageBWIBML9 = requests.get(URL)
soup = BeautifulSoup(pageBWIBML9.content, "html.parser")
priceBWIBML9 = soup.find("span", class_="prod-detail-cost-value").text

# Data extraction for LTO9 @Tape4Backup
# FUJI
URL = "https://www.tape4backup.com/collections/lto-9-tapes/products/fuji-lto-9-backup-tape-retail-x-1-16659047"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bFFL9_3 = soup.find("span", class_="price")
pricet4bFFL9_2 = list(pricet4bFFL9_3.stripped_strings)
pricet4bFFL9 = "\n\n".join(pricet4bFFL9_2) 
# HPE
URL = "https://www.tape4backup.com/collections/lto-9-tapes/products/hpe-lto-9-backup-tape-retail-x-1-q2079a"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bHPEL9_3 = soup.find("span", class_="price")
pricet4bHPEL9_2 = list(pricet4bHPEL9_3.stripped_strings)
pricet4bHPEL9 = "\n\n".join(pricet4bHPEL9_2) 
# QTM
URL = "https://www.tape4backup.com/collections/lto-9-tapes/products/quantum-lto-9-backup-tape-retail-x-1-mr-l9mqn-01"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bQTML9_3 = soup.find("span", class_="price")
pricet4bQTML9_2 = list(pricet4bQTML9_3.stripped_strings)
pricet4bQTML9 = "\n\n".join(pricet4bQTML9_2) 
# IBM
URL = "https://www.tape4backup.com/collections/lto-9-tapes/products/ibm-lto-9-backup-tape-retail-x-1-02xw568"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bIBML9_3 = soup.find("span", class_="price")
pricet4bIBML9_2 = list(pricet4bIBML9_3.stripped_strings)
pricet4bIBML9 = "\n\n".join(pricet4bIBML9_2) 

# Data extraction for LTO9 @Tape&Media
# FUJI
URL = "https://tapeandmedia.com/fuji-lto-9-tape-with-barium-ferrite-bafe-16659047/"
pagetamFFL9 = requests.get(URL)
soup = BeautifulSoup(pagetamFFL9.content, "html.parser")
pricetamFFL9 = soup.find("span", class_="price price--withoutTax price--main").text
# HPE
URL = "https://tapeandmedia.com/hpe-lto-9-tape-with-barium-ferrite-bafe-q2079a/"
pagetamHPEL9 = requests.get(URL)
soup = BeautifulSoup(pagetamHPEL9.content, "html.parser")
pricetamHPEL9 = soup.find("span", class_="price price--withoutTax price--main").text
# QTM
URL = "https://tapeandmedia.com/quantum-lto-9-tape-with-barium-ferrite-bafe-mr-l9mqn-01/"
pagetamQTML9 = requests.get(URL)
soup = BeautifulSoup(pagetamQTML9.content, "html.parser")
pricetamQTML9 = soup.find("span", class_="price price--withoutTax price--main").text
# IBM
URL = "https://tapeandmedia.com/ibm-lto-9-tape-with-barium-ferrite-bafe-02XW568/"
pagetamIBML9 = requests.get(URL)
soup = BeautifulSoup(pagetamIBML9.content, "html.parser")
pricetamIBML9 = soup.find("span", class_="price price--withoutTax price--main").text


# Create list
L9price_list = [
    [priceBWFFL9, priceBWHPEL9, priceBWQTML9, priceBWIBML9],
    [pricet4bFFL9, pricet4bHPEL9, pricet4bQTML9, pricet4bIBML9],
    [pricetamFFL9, pricetamHPEL9, pricetamQTML9, pricetamIBML9]
]

index = ["BackupWorks", "Tape4Backup", "Tape&Media"]
columns = ["FUJI", "HPE", "QTM", "IBM"]


#2 Convert bs4 element into dataframe

import pandas as pd
df9 = pd.DataFrame(L9price_list, index=index,columns=columns)
# df9 = df9.replace({"FUJI":{"$":""}, "HPE":{"$":""}, "QTM":{"$":""}, "IBM":{"$":""}})
df9['FUJI'] = df9['FUJI'].str.replace("$","", regex=True).astype(float)
df9['HPE'] = df9['HPE'].str.replace("$","", regex=True).astype(float)
df9['QTM'] = df9['QTM'].str.replace("$","", regex=True).astype(float)
df9['IBM'] = df9['IBM'].str.replace("$","", regex=True).astype(float)
pd.options.display.float_format = "${:,.2f}".format


#3 Export data to excel spreadsheet
import datetime
writer = pd.ExcelWriter("internet_pricing_LTO9_{}.xlsx".format(pd.Timestamp.now().strftime("%Y-%m-%d")), engine = "xlsxwriter")
df9.to_excel(writer, sheet_name="LTO9")

workbook = writer.book
worksheet = writer.sheets["LTO9"]

format = workbook.add_format({"num_format": "$#,##0.00"})
worksheet.set_column("A:A", 14, )
worksheet.set_column("B:E", 10, format)

writer.save()

# df9 = pd.DataFrame(L9price_dict, index=index, columns=["Backup Works"])
# print(type(df9))
print("---------------------------------------")
print("LTO9 Pricing as of", pd.Timestamp.now().strftime("%Y-%m-%d")+":")
print(df9)
print("---------------------------------------")




## Product part #s

# LTO9: Fuji(16456574), HPE(C7977A), IBM(38L9302), QUANTUM(MR-L9MQN-01)
# LTO9: Fuji(16551221), HPE(Q2078A), IBM(01PL041), QUANTUM(MR-L9MQN-01)
# LTO9: Fuji(16659047), HPE(Q2079A), IBM(02XW568), QUANTUM(MR-L9MQN-01)


#3 Sortout Data



#4 Store onto excel(online) file


#5 Automate process using Heroku (monthly)


#6 Send update with URL by email (monthly)


#7 Add dashboard to email??