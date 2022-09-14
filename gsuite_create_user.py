import pickle
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time
import sys
import random  
import string 
from os import system, name 
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("--headless")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")

stealth(driver,
        languages=["ja-JP", "ja"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

def random_string(letter_count, digit_count):  
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))  
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
  
    sam_list = list(str1) # it converts the string to list.  
    random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
    final_string = ''.join(sam_list)  
    return final_string  

user = 'admin@re-transfer.com'
domen = '@re-transfer.com'
url = "https://admin.google.com"
j = int(input("bikin berapa ?: ")) 
driver.get(url)
print('get url')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierId"]'))).send_keys(user)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierNext"]/div/button/span'))).click()
print('mengisi login')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys('cadasboy21@')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button/span'))).click()
print('login. . . .')
time.sleep(5)
i = 1
while i < j:
  driver.get('https://admin.google.com/ac/users?hl=en&authuser=0')
  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/span/span'))).click()
  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[1]/span/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/input')))
  fName = driver.find_element(By.XPATH, value='//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[1]/span/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/input')
  lName = driver.find_element(By.XPATH, value='//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[1]/span/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/input')
  eMail = driver.find_element(By.XPATH, value='//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[1]/span/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div[1]/input')
  fName.send_keys('Halo')
  lName.send_keys('Yamada')
  iD = 'services-annamzon.co.jp-'+random_string(7, 5)
  time.sleep(2)
  eMail.clear()
  eMail.send_keys(iD)
  Confirm = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[2]/div[2]/span/span'))).click()
  print('succesful create')
  previewSend = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[5]/div/div[2]/span/div/span/div/div[2]/div[1]/div[3]/div/span/span'))).click()
  print('preview send clicked')
  sentLogin = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/div[6]/div/div[2]/span/div/span/div/div[1]/span/div/div/div/div/div[1]/div/div[1]/input')))
  sentLogin.send_keys('satu@bikebaikjon.org')
  copyMyself = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/div[6]/div/div[2]/span/div/span/div/label/span'))).click()
  print('mengisi email kirm ke dan click sent copy')
  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[6]/div/div[2]/span/div/div[2]/div[2]/span/span'))).click()
  print('sukses membuat akun: ', Fore.MAGENTA +iD+domen )
  time.sleep(3)
  i += 1
# end while
ans = input("Quit ?: ")
if (ans == "y"):
 driver.quit()