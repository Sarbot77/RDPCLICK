from itertools import count
import re
import pickle
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
# options.add_argument("--incognito")
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

def name(email):
  driver.get('https://script.google.com')
  print('goto script google')
  # time.sleep(5)
  try:
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="'+email+'"]'))).click()
    print('waiting for next action')
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]'))).send_keys('cadasboy21@')
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/span'))).click()
    print('trying input account')
  except Exception as e:
    print('skip choosing account')
  try:
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="View Dashboard"]'))).click()
    # comment: 
  except Exception as e:
    print('66:view dashboard already clicked')
  # end try
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="New project"]'))).click()
  time.sleep(5)
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz[3]/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/ul/li')))
  box = driver.switch_to.active_element
  box.send_keys(Keys.CONTROL,'a')
  box.send_keys(Keys.DELETE)
  print('bikin function')
  script = 'function doGet(e){'+'return'+'ContentService.createTextOutput(''"Method GET not allowed");}'+' function doPost(e){'+'var send = GsenderV2.sendGmail(e);'+'return ContentService.createTextOutput(send);}'
  box.send_keys(script)
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz[3]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div/div/span/span/i'))).click()
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder=" Script ID "]'))).send_keys('1EK9uTQN4ChzH2KoHJ16yvDz9fTw4HkLJVEExM-P7-SCwdm_wpf1KCMjH')
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Look up"]'))).click()
  print('add script')
  time.sleep(3)
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Add"]'))).click()
  time.sleep(3)
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Deploy"]'))).click()
  time.sleep(2)
  print('klik deploy')
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="New deployment"]'))).click()
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="Lw7GHd snByac"]//i[@aria-hidden="true"][@class="google-material-icons jkk8t"][text()="settings"]'))).click()
  time.sleep(2)
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="jO7h3c"][text()="Web app"]'))).click()
  print('klik web app')
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="text"][@class="VfPpkd-fmcmS-wGMbrd "]'))).send_keys(email)
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[4]/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[4]/div/div'))).click()
  print('mengisi descripsi')
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Anyone"]'))).click()
  
  try:
      WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Deploy"]'))).click()
      
  except Exception as e:
      time.sleep(10)
      print('gagal mencari si anjing iframe')
      # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//iframe[@title="Google Survey"]')))
      driver.switch_to.frame(driver.find_element_by_name('google-hats-survey'))
      driver.find_element(By.XPATH,'//span[text()="No thanks"]').click()
      time.sleep(2)
      driver.switch_to.default_content()
      WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Deploy"]'))).click()
    
  # end try
  print('success deploy..')
  time.sleep(2)
  print('success deploy....')
  window_before = driver.window_handles[0]
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Authorize access"]'))).click()
  window_after = driver.window_handles[1]
  print('switch window')
  driver.switch_to.window(window_after)
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="pQ0lne"]//ul[1]/li[1]/div[1]'))).click()
  # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-identifier="'+email+'"]'))).click()
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Allow"]'))).click()
  print('success authorize')
  driver.switch_to.window(window_before)
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-new-deployment="true"]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[2]/div[1]')))
  webApps = driver.find_element(By.XPATH,'//div[@data-new-deployment="true"]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]/div[1]/a[1]')
  try:
    webApps = webApps.get_attribute('href')
    print('grab webhook :',Back.CYAN+webApps)
    open('WEBHOOK_FRESH.txt','a').write(webApps+"|"+email+"\n")
  except Exception as e:    
        print(e)
  print('----------------FINISH -----------------------')
  driver.delete_all_cookies()
  driver.get('chrome://settings/clearBrowserData')
  time.sleep(5)
  actions = ActionChains(driver) 
  actions.send_keys(Keys.TAB * 7 + Keys.ENTER) # confirm
  actions.perform()
  time.sleep(5)
  # driver.get('chrome://settings/clearBrowserData')
  # time.sleep(2)
  # actions.send_keys(Keys.TAB * 9 + Keys.ENTER) # confirm
  # actions.perform()
  # time.sleep(5)
  # time.sleep(60)
  # driver.quit()
  # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div[3]/div/div/div[1]/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div[4]/div[2]/span/span'))).send_keys('ini functionnya')
# end def

def login(a):
  driver.get('https://accounts.google.com')
  ans = a
  pw = 'cadasboy21@'
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierId"]'))).send_keys(ans)
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/div/button/span'))).click()
  print('trying to login....')
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys(pw)
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button/span'))).click()
  time.sleep(3)
  print('trying to login......')
# end def
for e in open(sys.argv[1],'r').readlines():
  link=e.strip().replace(' ','').replace('\n','')
  if not link:
        break
  url = link
  driver.get(url)
  print('get url from: ',Fore.YELLOW +url)
  pw = 'cadasboy21@'
  try:
    emil = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//form[@id="tos_form"]/span[1]/p[1]')))
    emil = emil.text
    x = re.search(r'Welcome\sto\syour\snew\saccount:\s([^"]+)\.\s', emil)
    email = x.group(1)
    print('trying login with: ',Fore.MAGENTA +email)
    # comment: 
  except Exception as e:
    print(Fore.RED+'The URL you tried to use is either incorrect or no longer valid.')
    break
  # end try

  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="confirm"]'))).click()
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Password"]'))).send_keys(pw)
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ConfirmPassword"]'))).send_keys(pw)
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit"]'))).click()
  WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sdgBod"]/span')))
  print('succesful login')
  name(email)
    
Done = input("Proccess done quit?: ")
if (Done == 'y'):
  driver.quit()


# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierNext"]/div/button/span'))).click()
# print('mengisi login')
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))).send_keys('cadasboy21@')
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button/span'))).click()
# print('login. . . .')
# time.sleep(5)
# i = 1
# while i < 3:
#   driver.get('https://admin.google.com/ac/users?hl=en&authuser=0')
#   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/span/span'))).click()
#   WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[1]/span/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/input')))
#   fName = driver.find_element(By.XPATH, value='//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[1]/span/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/input')
#   lName = driver.find_element(By.XPATH, value='//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[1]/span/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/input')
#   eMail = driver.find_element(By.XPATH, value='//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[1]/span/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div[1]/input')
#   fName.send_keys('Halo')
#   lName.send_keys('Yamada')
#   eMail.clear()
#   iD = 'services-annamzon.co.jp-'+random_string(7, 5)
#   eMail.send_keys(iD)
#   Confirm = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[2]/div[2]/span/span'))).click()
#   print('succesful create')
#   previewSend = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[5]/div/div[2]/span/div/span/div/div[2]/div[1]/div[3]/div/span/span'))).click()
#   print('preview send clicked')
#   sentLogin = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/div[6]/div/div[2]/span/div/span/div/div[1]/span/div/div/div/div/div[1]/div/div[1]/input')))
#   sentLogin.send_keys('satu@bikebaikjon.org')
#   copyMyself = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/div[6]/div/div[2]/span/div/span/div/label/span'))).click()
#   print('mengisi email kirm ke dan click sent copy')
#   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[6]/div/div[2]/span/div/div[2]/div[2]/span/span'))).click()
#   print('sukses membuat akun: ', iD+domen )
#   time.sleep(3)
#   i += 1
# # end while
# ans = input("Quit ?: ")
# if (ans == "y"):
#  driver.quit()