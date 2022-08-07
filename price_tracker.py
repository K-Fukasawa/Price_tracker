
#1 Extract data from internet (URL, API setup)

## https://www.amazon.com/
## https://www.backupworks.com/
## https://www.connection.com/
## https://www.tape4backup.com/
## https://tapeandmedia.com/

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# s = Service('C:/Users/kai.fukasawa/Documents/GitHub/chromedriver')  #< Print your filepath to Chromedriver here.
# driver = webdriver.Chrome(service=s)

import requests
from bs4 import BeautifulSoup

URL = "https://www.backupworks.com/FujiFilm-LTO-9-Tape-Media-16659047.aspx"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

price1 = soup.find_all("span", class_="prod-detail-cost-value")
# results = soup.find(id="prod-detail-cost-value")
print(price1)
print(type(price1))

#2 


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