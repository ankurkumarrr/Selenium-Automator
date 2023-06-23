
# rpmids = []
# f = open("rpmids.txt", "r")
# for line in f.read().splitlines():
# 	if line.strip() != "":
# 		rpmids.append(line.strip())
# f.close()


# driver.get('https:\\sciometrix.lightning.force.com\\lightning\\o\\Patient__c\\list?filterName=Recent')
# input(style.MAGENTA + "Once your browser opens up sign in to salesforce and then press ENTER..." + style.RESET)

# try:

#     url = 'https:\\sciometrix.lightning.force.com\\lightning\\o\\Patient__c\\list?filterName=Recent'
#     driver.get(url)

#     c1 = 0

#     for j in customerid:

#         #search
#         searchbar = wait.until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="oneHeader"]/div[2]/div[2]/div/button''')))
#         sleep(1)
#         searchbar.click()
#         searchbar2 = wait.until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="input-185"]''')))
#         sleep(1)
#         searchbar2.send_keys(j)
#         sleep(1)
#         searchbar2.send_keys(Keys.ENTER)
#         sleep(1)

#         #select patient 
#         patient = wait.until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="brandBand_2"]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/table/tbody/tr/th/span/a''')))
#         sleep(1)
#         patient.click()
#         sleep(1)
#         input(style.MAGENTA + orderno[c1] + "   " + rpmids[c1] + style.RESET)
#         c1+=1

#     # #update front rpmID
#     # # rpm1_button = wait.until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="sectionContent-2174"]/div/slot/records-record-layout-row[6]/slot/records-record-layout-item[1]/div/div/div[2]/button''')))
#     # rpm1_button = wait.until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="input-1298"]''')))
#     # sleep(2)
#     # rpm1_button.send_keys("12345")
#     # sleep(6)
    
# except:
#     print(Exception)   
