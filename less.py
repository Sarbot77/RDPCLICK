from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time
import sys
from os import system, name 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
clear()
# print("\n")
# print(" [ + ] GOOGLE AUTO LESS SECURE - SELENIUM")
# print(" [ ! ] facebook.com/lav13enrose")
# listz = open(sys.argv[1],'r').readlines()
# totalemail = len(list(open(listz)))
asu = 1
list = open(sys.argv[1],'r').readlines()
for e in list:
    email=e.strip().replace(' ','').replace('\n','')
    if not email:
        break
    print(email)
    opts = Options()
    opts.add_experimental_option('excludeSwitches', ['enable-logging'])
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36")
    driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=opts)
    driver.get('https://www.gmass.co/dashboard')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierId"]'))).click()
    emailInput = driver.find_element_by_xpath('//*[@id="identifierId"]')
    emailInput.send_keys(email)
    driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button/span')))
    tmbol = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
    pw = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    pw.send_keys('cadasboy21@')
    tmbol.click()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'show-settings'))).click()
        ps = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "/html/head/title")))
        print(driver.title)
        time.sleep(10)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'settings-panel')))
        warmup = driver.find_element_by_xpath('//*[@id="settings-wrap"]/ul/li[14]/a')
        warmup.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="settings-wrap"]/ul/li[14]/form/div[1]/label'))).click()
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-confirm-warmup"]'))).click()
        # time.sleep(8)
        # try:
        #     WebDriverWait(driver, 3).until(EC.alert_is_present())
        #     alert = driver.switch_to.alert
        #     alert.accept()
        #     print("alert accepted")
        # except Exception as e:
        #     print("no alert")

    except Exception as e:
        print(e)
                # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="accept"]'))).click()
    driver.get('https://myaccount.google.com/lesssecureapps?pli=1')
    content=driver.page_source
    result = content.find('Allow less secure apps: OFF')
    if (result != -1):
            driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/c-wiz/div/div[4]/div/div/div/ul/li/div[1]/div[2]/div/button/span').click()
            print("Enabled less secure")
            driver.close()
    else:
            print('less secure already Enabled	')
            driver.close()
    # if asu == 1:
    #     break
            # driver.close()
    # content=driver.page_source
    # result = content.find('Welcome to your new account')
    # verif = content.find('Verifikasi')
    # if (verif != -1):
    #     driver.delete_all_cookies()
    #     driver.close()
    #     driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="openid-buttons"]/button[1]'))).click()
    #     emailInput = driver.find_element_by_xpath('//*[@id="identifierId"]')
    #     emailInput.send_keys(aww[0])
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/div/button'))).click()
    #     button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
    #     button.click()
    #     button.send_keys(aww[1])
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/div[2]'))).click()
    #     time.sleep(5)
    #     content=driver.page_source
    #     result = 1
    #     if (result != -1):
    #         # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="accept"]'))).click()
    #         driver.get('https://myaccount.google.com/lesssecureapps?pli=1')
    #         content=driver.page_source
    #         result = content.find('Allow less secure apps: OFF')
    #         if (result != -1):
    #             print("[ENABLING]")
    #             driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/c-wiz/div/div[3]/div[1]/div/div/div/div[2]/div').click()
    #             driver.close()
    #         else:
    #             print('Already Enabled	')
    #             driver.close()
    #     else:
    #         driver.get('https://myaccount.google.com/lesssecureapps?pli=1')
    #         content=driver.page_source
    #         result = content.find('Allow less secure apps: OFF')
    #     if (result != -1):
    #         print("[ENABLING]")
    #         driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/c-wiz/div/div[3]/div[1]/div/div/div/div[2]/div').click()
    #         driver.close()
    #     else:
    #         print('Already Enabled	')
    #         driver.close()
    # if (result != -1):
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="accept"]'))).click()
    #     driver.get('https://myaccount.google.com/lesssecureapps?pli=1')
    #     content=driver.page_source
    #     result = content.find('Allow less secure apps: OFF')
    #     if (result != -1):
    #         print("[ENABLING]")
    #         driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/c-wiz/div/div[3]/div[1]/div/div/div/div[2]/div').click()
    #         driver.close()
    #     else:
    #         print('Already Enabled	')
    #         driver.close()
    # else:
    #     driver.get('https://myaccount.google.com/lesssecureapps?pli=1')
    #     content=driver.page_source
    #     result = content.find('Allow less secure apps: OFF')
    #     if (result != -1):
    #         print("[ENABLING]")
    #         driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/c-wiz/div/div[3]/div[1]/div/div/div/div[2]/div').click()
    #         driver.close()
    #     else:
    #         print('Already Enabled	')
    #         driver.delete_all_cookies()
    #         driver.close()