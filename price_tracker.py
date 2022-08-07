
#1 Extract data from internet (URL, API setup)

## https://www.amazon.com/
## https://www.backupworks.com/
## https://www.connection.com/
## https://www.tape4backup.com/
## https://tapeandmedia.com/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('C:/Users/kai.fukasawa/Documents/GitHub/chromedriver')
driver = webdriver.Chrome(service=s)

#2 Access to website
driver.get("https://www.google.com/")
print(driver.title) #> Google
driver.save_screenshot("search_page.png")


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