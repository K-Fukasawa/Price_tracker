
#1 Extract data from internet (URL, API setup)

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# s = Service('C:/Users/kai.fukasawa/Documents/GitHub/chromedriver')  #< Print your filepath to Chromedriver here.
# driver = webdriver.Chrome(service=s)

import requests
from bs4 import BeautifulSoup

# Data extraction for LTO7 @Backupworks
# FUJI
URL = "https://www.connection.com/product/fujifilm-6tb-15tb-lto-7-ultrium-data-cartridge-w-case/16456574/32027865?cac=Result"
pageBWFFL7 = requests.get(URL)
soup = BeautifulSoup(pageBWFFL7.content, "html.parser")
priceCOFF7 = soup.find(itemprop="price").get("content")
# HPE
# URL = "https://www.connection.com/product/hpe-15tb-lto-7-ultrium-rw-data-cartridge/c7977a/30982439?cac=Result"
# pageBWHPEL7 = requests.get(URL)
# soup = BeautifulSoup(pageBWHPEL7.content, "html.parser")
# priceBWHPE7 = soup.find_all()
# QTM
# URL = "https://www.connection.com/product/quantum-lto-7-ultrium-tape-cartridge/mr-l7mqn-01/30860087?cac=Result"
# pageBWQTML7 = requests.get(URL)
# soup = BeautifulSoup(pageBWQTML7.content, "html.parser")
# priceBWQTM7 = soup.find_all()
# IBM
# URL = "https://www.connection.com/product/ibm-lto-7-ultrium-data-cartridge/38l7302/31777672?cac=Result"
# pageBWIBML7 = requests.get(URL)
# soup = BeautifulSoup(pageBWIBML7.content, "html.parser")
# priceBWIBM7 = soup.find_all()

# Create list
L7price_list = [priceCOFF7] # , priceBWHPE7, priceBWQTM7, priceBWIBM7],

# print(L7price_dict)
# print(type(L7price_dict))

# index = ["FUJI", "HPE", "Quantum", "IBM"]
# columns = ["FUJI", "HPE", "Quantum", "IBM"]

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
df = pd.DataFrame(L7price_list, index=["Connection"])#,columns=columns)
# df = pd.DataFrame(L7price_dict, index=index, columns=["Backup Works"])
# print(type(df))
print(df)


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