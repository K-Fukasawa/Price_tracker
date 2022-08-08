
#1 Extract data from internet (URL, API setup)

import requests
from bs4 import BeautifulSoup

# Data extraction for LTO8 @Backupworks
# FUJI
URL = "https://www.backupworks.com/FujiFilm-LTO-8-Cartridge-16551221.aspx"
pageBWFFL8 = requests.get(URL)
soup = BeautifulSoup(pageBWFFL8.content, "html.parser")
priceBWFFL8 = soup.find("span", class_="prod-detail-cost-value").text
# HPE
URL = "https://www.backupworks.com/HPE-LTO-8-Tape-Media-Q2078A.aspx"
pageBWHPEL8 = requests.get(URL)
soup = BeautifulSoup(pageBWHPEL8.content, "html.parser")
priceBWHPEL8 = soup.find("span", class_="prod-detail-cost-value").text
# QTM
URL = "https://www.backupworks.com/Quantum-LTO-8-Tape-media-MR-L8MQN-01.aspx"
pageBWQTML8 = requests.get(URL)
soup = BeautifulSoup(pageBWQTML8.content, "html.parser")
priceBWQTML8 = soup.find("span", class_="prod-detail-cost-value").text
# IBM
URL = "https://www.backupworks.com/IBM-LTO-8-tape-cartridge-01PL041.aspx"
pageBWIBML8 = requests.get(URL)
soup = BeautifulSoup(pageBWIBML8.content, "html.parser")
priceBWIBML8 = soup.find("span", class_="prod-detail-cost-value").text

# Data extraction for LTO8 @Tape4Backup
# FUJI
URL = "https://www.tape4backup.com/collections/lto-8-tapes/products/fuji-16551221-lto-8-backup-tape-12tb-30tb"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bFFL8_3 = soup.find("span", class_="price")
pricet4bFFL8_2 = list(pricet4bFFL8_3.stripped_strings)
pricet4bFFL8 = "\n\n".join(pricet4bFFL8_2) 
# HPE
URL = "https://www.tape4backup.com/products/hpe-q2078a-lto-8-backup-tape-bafe-12-30-tb"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bHPEL8_3 = soup.find("span", class_="price")
pricet4bHPEL8_2 = list(pricet4bHPEL8_3.stripped_strings)
pricet4bHPEL8 = "\n\n".join(pricet4bHPEL8_2) 
# QTM
URL = "https://www.tape4backup.com/collections/lto-8-tapes/products/quantum-mr-l8mqn-01-lto-8-backup-tape"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bQTML8_3 = soup.find("span", class_="price")
pricet4bQTML8_2 = list(pricet4bQTML8_3.stripped_strings)
pricet4bQTML8 = "\n\n".join(pricet4bQTML8_2) 
# IBM
URL = "https://www.tape4backup.com/collections/lto-8-tapes/products/ibm-01pl041-lto-8-backup-tape-12tb-30tb"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bIBML8_3 = soup.find("span", class_="price")
pricet4bIBML8_2 = list(pricet4bIBML8_3.stripped_strings)
pricet4bIBML8 = "\n\n".join(pricet4bIBML8_2) 

# Data extraction for LTO8 @Tape&Media
# FUJI
URL = "https://tapeandmedia.com/fuji-lto-8-tape-ultrium-tapes-16551221.asp"
pagetamFFL8 = requests.get(URL)
soup = BeautifulSoup(pagetamFFL8.content, "html.parser")
pricetamFFL8 = soup.find("span", class_="price price--withoutTax price--main").text
# HPE
URL = "https://tapeandmedia.com/hp-lto-8-tape-ultrium-tapes-q2078A.asp"
pagetamHPEL8 = requests.get(URL)
soup = BeautifulSoup(pagetamHPEL8.content, "html.parser")
pricetamHPEL8 = soup.find("span", class_="price price--withoutTax price--main").text
# QTM
URL = "https://tapeandmedia.com/quantum-lto-8-tape-ultrium.asp"
pagetamQTML8 = requests.get(URL)
soup = BeautifulSoup(pagetamQTML8.content, "html.parser")
pricetamQTML8 = soup.find("span", class_="price price--withoutTax price--main").text
# IBM
URL = "https://tapeandmedia.com/ibm-lto-8-tape-ultrium-tapes-01PL041.asp"
pagetamIBML8 = requests.get(URL)
soup = BeautifulSoup(pagetamIBML8.content, "html.parser")
pricetamIBML8 = soup.find("span", class_="price price--withoutTax price--main").text


# Create list
L8price_list = [
    [priceBWFFL8, priceBWHPEL8, priceBWQTML8, priceBWIBML8],
    [pricet4bFFL8, pricet4bHPEL8, pricet4bQTML8, pricet4bIBML8],
    [pricetamFFL8, pricetamHPEL8, pricetamQTML8, pricetamIBML8]
]

index = ["BackupWorks", "Tape4Backup", "Tape&Media"]
columns = ["FUJI", "HPE", "QTM", "IBM"]


#2 Convert bs4 element into dataframe

import pandas as pd
df = pd.DataFrame(L8price_list, index=index,columns=columns)
# df = df.replace({"FUJI":{"$":""}, "HPE":{"$":""}, "QTM":{"$":""}, "IBM":{"$":""}})
df['FUJI'] = df['FUJI'].str.replace("$","", regex=True).astype(float)
df['HPE'] = df['HPE'].str.replace("$","", regex=True).astype(float)
df['QTM'] = df['QTM'].str.replace("$","", regex=True).astype(float)
df['IBM'] = df['IBM'].str.replace("$","", regex=True).astype(float)
pd.options.display.float_format = "${:,.2f}".format


#3 Export data to excel spreadsheet

writer = pd.ExcelWriter("internet_pricing_LTO8.xlsx", engine = "xlsxwriter")
df.to_excel(writer, sheet_name="LTO8")

workbook = writer.book
worksheet = writer.sheets["LTO8"]

format = workbook.add_format({"num_format": "$#,##0.00"})
worksheet.set_column("A:A", 14, )
worksheet.set_column("B:E", 10, format)

writer.save()

# df = pd.DataFrame(L8price_dict, index=index, columns=["Backup Works"])
print(type(df))
print(df)





## Product part #s

# LTO8: Fuji(16456574), HPE(C7977A), IBM(38L8302), QUANTUM(MR-L8MQN-01)
# LTO8: Fuji(16551221), HPE(Q2078A), IBM(01PL041), QUANTUM(MR-L8MQN-01)
# LTO9: Fuji(16659047), HPE(Q2079A), IBM(02XW568), QUANTUM(MR-L9MQN-01)


#3 Sortout Data



#4 Store onto excel(online) file


#5 Automate process using Heroku (monthly)


#6 Send update with URL by email (monthly)


#7 Add dashboard to email??