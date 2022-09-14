from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
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

chrome_options = webdriver.ChromeOptions();
chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)



ans = 'nishinotakao9687@ni-rakutenjp.info'
print(ans)
driver.get("https://gmail.com")
inpt=driver.find_element(By.XPATH,'//*[@id="identifierId"]')
submit=driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/div[3]')
inpt.send_keys(ans)
submit.click()
passx = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
inpt.send_keys('cadasboy21@')
sbmt = driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/div[3]')
sbmt.click()
