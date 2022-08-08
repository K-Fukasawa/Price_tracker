
#1 Extract data from internet (URL, API setup)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# s = Service('C:/Users/kai.fukasawa/Documents/GitHub/chromedriver')  #< Print your filepath to Chromedriver here.
# driver = webdriver.Chrome(service=s)

import requests
from bs4 import BeautifulSoup

# Data extraction for LTO7 @Backupworks
# FUJI
URL = "https://www.backupworks.com/Fujifilm-LTO-7-tape-media-16456574.aspx"
pageBWFFL7 = requests.get(URL)
soup = BeautifulSoup(pageBWFFL7.content, "html.parser")
priceBWFF7 = soup.find_all("span", class_="prod-detail-cost-value")
# HPE
URL = "https://www.backupworks.com/HP-LTO-7-tape-cartridge-C7977A.aspx"
pageBWHPEL7 = requests.get(URL)
soup = BeautifulSoup(pageBWHPEL7.content, "html.parser")
priceBWHPE7 = soup.find_all("span", class_="prod-detail-cost-value")
# QTM
URL = "https://www.backupworks.com/Quantum-LTO-7-tape-cartridge-MR-L7MQN-01.aspx"
pageBWQTML7 = requests.get(URL)
soup = BeautifulSoup(pageBWQTML7.content, "html.parser")
priceBWQTM7 = soup.find_all("span", class_="prod-detail-cost-value")
# IBM
URL = "https://www.backupworks.com/IBM-LTO-7-tape-media-38L7302.aspx"
pageBWIBML7 = requests.get(URL)
soup = BeautifulSoup(pageBWIBML7.content, "html.parser")
priceBWIBM7 = soup.find_all("span", class_="prod-detail-cost-value")


# Data extraction for LTO7 @TapeBackup
# FUJI
URL = "https://www.tape4backup.com/collections/lto-7-tapes/products/fuji-16456574-nr-lto-7-data-backup-tape-new-repacked"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bFF7 = soup.find("span", class_="price")
# HPE
URL = "https://www.tape4backup.com/collections/lto-7-tapes/products/hpe-c7977a-nr-lto-7-data-backup-tape-new-repacked"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bHPE7 = soup.find("span", class_="price")
# QTM
URL = "https://www.tape4backup.com/collections/lto-7-tapes/products/quantum-lto-7-data-backup-tape-new-repacked"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bQTM7 = soup.find("span", class_="price")
# IBM
URL = "https://www.tape4backup.com/collections/lto-7-tapes/products/ibm-38l7302-nr-lto-7-data-backup-tape-new-repacked"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bIBM7 = soup.find("span", class_="price")

# Create list
L7price_list = [
    [priceBWFF7, priceBWHPE7, priceBWQTM7, priceBWIBM7],
    [pricet4bFF7, pricet4bHPE7, pricet4bQTM7, pricet4bIBM7]
]
# print(L7price_dict)
# print(type(L7price_dict))
# Create list
# L7price_list = [pricet4bFF7, pricet4bHPE7, pricet4bQTM7, pricet4bIBM7]
# print(L7price_list)

index = ["BacupWorks", "Tape4Backup"]
columns = ["FUJI", "HPE", "Quantum", "IBM"]

# FF
# "DONE"
# "https://www.backupworks.com/FujiFilm-LTO-8-Cartridge-16551221.aspx"
# "https://www.backupworks.com/FujiFilm-LTO-9-Tape-Media-16659047.aspx"

# IBM
# "DONE"
# "https://www.backupworks.com/IBM-LTO-8-tape-cartridge-01PL041.aspx"
# "https://www.backupworks.com/IBM-LTO-9-tape-media-02XW568.aspx"

# Quantum
# "DONE"
# "https://www.backupworks.com/Quantum-LTO-8-Tape-media-MR-L8MQN-01.aspx"
# "https://www.backupworks.com/Quantum-LTO-9-Tape-media-MR-L9MQN-01.aspx"

# HPE
# "DONE"
# ""
# ""

#2 Convert bs4 element into dataframe

import pandas as pd
df = pd.DataFrame(L7price_list, index=index,columns=columns)
# df = pd.DataFrame(L7price_dict, index=index, columns=["Backup Works"])
print(type(df))
print(df)
print(type(priceBWFF7))
print(type(pricet4bFF7))

#X Access to website
# driver.get("https://www.backupworks.com/FujiFilm-LTO-9-Tape-Media-16659047.aspx")
# print(driver.title) #> Google
# driver.save_screenshot("search_page.png")
#X-2 Find element
#X-3 Interact with element

#3 Inspect data and store as df




## Product part #s

# LTO7: Fuji(16456574), HPE(C7977A), IBM(38L7302), QUANTUM(MR-L7MQN-01)
# LTO8: Fuji(16551221), HPE(Q2078A), IBM(01PL041), QUANTUM(MR-L8MQN-01)
# LTO9: Fuji(16659047), HPE(Q2079A), IBM(02XW568), QUANTUM(MR-L9MQN-01)


#3 Sortout Data



#4 Store onto excel(online) file


#5 Automate process using Heroku (monthly)


#6 Send update with URL by email (monthly)


#7 Add dashboard to email??