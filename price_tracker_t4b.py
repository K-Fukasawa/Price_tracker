
#1 Extract data from internet (URL, API setup)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# s = Service('C:/Users/kai.fukasawa/Documents/GitHub/chromedriver')  #< Print your filepath to Chromedriver here.
# driver = webdriver.Chrome(service=s)

import requests
from bs4 import BeautifulSoup

# Data extraction for LTO7 @Backupworks
# FUJI
URL = "https://www.tape4backup.com/collections/lto-7-tapes/products/fuji-16456574-nr-lto-7-data-backup-tape-new-repacked"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bFF7 = soup.find("span", class_="price")
#print(pricet4bFF7)

URL = "https://www.tape4backup.com/collections/lto-7-tapes/products/hpe-c7977a-nr-lto-7-data-backup-tape-new-repacked"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bHPE7 = soup.find("span", class_="price")
#print(pricet4bHPE7)

URL = "https://www.tape4backup.com/collections/lto-7-tapes/products/quantum-lto-7-data-backup-tape-new-repacked"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bQTM7 = soup.find("span", class_="price")
#print(pricet4bQTM7)

URL = "https://www.tape4backup.com/collections/lto-7-tapes/products/ibm-38l7302-nr-lto-7-data-backup-tape-new-repacked"
paget4b = requests.get(URL)
soup = BeautifulSoup(paget4b.content, "html.parser")
pricet4bIBM7 = soup.find("span", class_="price")
#print(pricet4bIBM7)

# Create list
L7price_list = [pricet4bFF7, pricet4bHPE7, pricet4bQTM7, pricet4bIBM7]
print(L7price_list)

#2 Convert bs4 element into dataframe

# import pandas as pd
# df = pd.DataFrame(L7price_list, index=["Connection"])#,columns=columns)
# df = pd.DataFrame(L7price_dict, index=index, columns=["Backup Works"])
# print(type(df))
# print(df)


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