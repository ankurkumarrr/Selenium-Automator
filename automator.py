from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import os
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLUE)
print(style.RESET)

data = {}

orderno = []
f = open("orderno.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		orderno.append(line.strip())
f.close()

customerid = []
f = open("customerid.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		customerid.append(line.strip())
f.close()

customername = []
f = open("customer_name.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		customername.append(line.strip())
f.close()

total_number_orderno=len(orderno)
total_number_customerid=len(customerid)
total_number_customername=len(customername)
print(style.RED + 'We found ' + str(total_number_orderno) + ' orders in the file' + style.RESET)
print(style.RED + 'We found ' + str(total_number_customerid) + ' customers in the file' + style.RESET)
print(style.RED + 'We found ' + str(total_number_customername) + ' customer names in the file' + style.RESET)
delay = 30

orderid = orderno[0]

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
wait = WebDriverWait(driver, 10)

# Smartmetr Fetch values

# driver.get('https:\\portal.smartmeterrpm.com\\orders\\{orderid}\\C8ABFCF8-377E-4821-89D6-432912C59C1A-1621626168\\'.format(orderid = orderid))
# input(style.MAGENTA + "Once your browser opens up sign in to smartmeter and then press ENTER..." + style.RESET)

# try:

#     c = 0

#     for i in orderno:
#         url = 'https:\\portal.smartmeterrpm.com\\orders\\{orderid}\\C8ABFCF8-377E-4821-89D6-432912C59C1A-1621626168\\'.format(orderid = i)
#         driver.get(url)
#         sleep(2)
#         try:
#             rpmid = wait.until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="line-items-table"]/table[2]/tbody/tr/td[4]'''))).text
#             trackingno = wait.until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="shipping-info"]/tr/td[1]'''))).text
#             data[customerid[c]] = [rpmid,trackingno]
#             f = open("smartmetr_outputlog.txt", "a+")
#             f.write(str([i,customername[c],customerid[c],rpmid,trackingno])+"\n")
#             f.flush()
#             f.close()
            
#             f = open("rpmids.txt", "a+")
#             f.write(rpmid+"\n")
#             f.flush()
#             f.close()

#             f = open("trackingno.txt", "a+")
#             f.write(trackingno+"\n")
#             f.flush()
#             f.close()



#         except:
#             f = open("smartmetr_outputlog.txt", "a+")
#             f.write(str([i,"Error"])+"\n")
#             f.flush()
#             f.close()
#             print("Loading Error")
#             pass
#         c+=1

# except:
#     print(Exception)
    

# SalesForce Block

rpmids = []
f = open("rpmids.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		rpmids.append(line.strip())
f.close()


trackingno = []
f = open("trackingno.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		rpmids.append(line.strip())
f.close()


driver.get('https:\\sciometrix.lightning.force.com\\lightning\\o\\Patient__c\\list?filterName=Recent')
input(style.MAGENTA + "Once your browser opens up sign in to salesforce and then press ENTER..." + style.RESET)

try:

    url = 'https:\\sciometrix.lightning.force.com\\lightning\\o\\Patient__c\\list?filterName=Recent'
    driver.get(url)

    c1 = 0

    for j in customerid:

        #search
        searchbar = wait.until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="oneHeader"]/div[2]/div[2]/div/button''')))
        sleep(3)
        searchbar.click()
        searchbar2 = wait.until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="input-185"]''')))
        sleep(3)
        searchbar2.send_keys(j)
        sleep(3)
        searchbar2.send_keys(Keys.ENTER)
        sleep(3)

        #select patient 
        patient = wait.until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="brandBand_2"]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/table/tbody/tr/th/span/a''')))
        sleep(3)
        patient.click()
        sleep(3)
        input(style.MAGENTA + orderno[c1] + "   " + rpmids[c1] + "   " + trackingno[c1] + style.RESET)
        c1+=1

    # #update front rpmID
    # # rpm1_button = wait.until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="sectionContent-2174"]/div/slot/records-record-layout-row[6]/slot/records-record-layout-item[1]/div/div/div[2]/button''')))
    # rpm1_button = wait.until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="input-1298"]''')))
    # sleep(2)
    # rpm1_button.send_keys("12345")
    # sleep(6)
    
except:
    print(Exception)   


driver.close()