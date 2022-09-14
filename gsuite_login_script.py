from itertools import count
import pyperclip
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
saveAs = input("Please enter output name: ")

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
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[4]/div/div[2]/span/div/div[2]/span/span'))).click()
  except Exception as e:
    print('error: view dashboard already clicked')
  
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div[1]/button/span[3]'))).click()
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz[3]/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/ul/li')))
  box = driver.switch_to.active_element
  box.send_keys(Keys.CONTROL,'a')
  box.send_keys(Keys.DELETE)
  print('bikin function')
  script = """ 
function doPost(e) {
  var email = e.parameter["email"];
  var name = e.parameter["name"];
  var subject = e.parameter["subject"];
  var body = e.parameter["body"];
  var isHtml = e.parameter["isHtml"];
  var replyTo = e.parameter["replyTo"];

  function formatAMPM() {
    var d = new Date(),
      minutes = d.getMinutes().toString().length == 1 ? '0' + d.getMinutes() : d.getMinutes(),
      hours = d.getHours().toString().length == 1 ? '0' + d.getHours() : d.getHours(),
      ampm = d.getHours() >= 12 ? 'pm' : 'am',
      months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    return days[d.getDay()] + ' ' + months[d.getMonth()] + ' ' + d.getDate() + ' ' + d.getFullYear() + ' ' + hours + ':' + minutes + ampm;
  }

  var message = GmailApp.getInboxThreads(0, 1)[0].getMessages()[0];
  var froms = message.getFrom();
  var userx = Session.getActiveUser().getEmail();
  var userg = "mailer-daemon@googlemail.com";
  var emailX = "null";
  var statusInfo = "null";

  if (froms.includes(userg)) {
    var body = message.getBody();
    var bodyText = body.replace(/[\\r\\n]/g, "");

    var regExp = new RegExp('weight:bold;margin:0\\">(.*)<\\/h2>', "gm"); // "i" is for case insensitive
    var statusInfo = regExp.exec(bodyText)[1];

    if (statusInfo == "Address not found") {
      var regExps = new RegExp("text-decoration\\:none'\\>\\<b\\>(.*)\\<\\/b>", "gm"); // "i" is for case insensitive
      var emailX = regExps.exec(bodyText)[1];
    }
  } else if (froms.includes(userx)) {
    try {
      var body = GmailApp.getInboxThreads(0, 1)[0].getMessages()[1].getBody();
      var bodyText = body.replace(/[\\r\\n]/g, "");
      try {
        var regExp = new RegExp('weight:bold;margin:0\\">(.*)<\\/h2>', "gm"); // "i" is for case insensitive
        var statusInfo = regExp.exec(bodyText)[1];
      } catch (e) {
        var statusInfo = bodyText
      }

      if (statusInfo == "Address not found") {
        var regExps = new RegExp("text-decoration\\:none'\\>\\<b\\>(.*)\\<\\/b>", "gm"); // "i" is for case insensitive
        var emailX = regExps.exec(bodyText)[1];
      }
    }
    catch (error) {
    }

  }

  try {
    GmailApp.sendEmail(email, subject, body, {
      name: name,
      htmlBody: isHtml,
      replyTo: replyTo
    });
    var result = "{\\"status\\":\\"Success\\",\\"mailStatus\\":\\"" + statusInfo + "\\",\\"mailPalsu\\":\\"" + emailX + "\\",\\"to\\":\\"" + email + "\\",\\"date\\":\\"" + formatAMPM() + "\\"}";
  } catch (error) {
    var result = "{\\"status\\":\\"Failed\\",\\"mailStatus\\":\\"" + statusInfo + "\\",\\"error\\":\\"" + error + "\\",\\"date\\":\\"" + formatAMPM() + "\\"}";
  }
  return ContentService.createTextOutput(result).setMimeType(ContentService.MimeType.JSON);
}
  """
  pyperclip.copy(script)
  box.send_keys(Keys.CONTROL + "v")
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
      iframe = driver.find_element(By.XPATH,'//iframe[@name="google-hats-survey"]')
      # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//iframe[@title="Google Survey"]')))
      driver.switch_to.frame(iframe)
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
    open('WEBHOOK-'+saveAs+'.txt','a').write(webApps+"|"+email+"\n")
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
  email=e.strip().replace(' ','').replace('\n','')
  if not email:
        break
  print('Email : ',Back.GREEN +email)
  pw = 'cadasboy21@'
  login(email)
  name(email)
    
Done = input("Proccess done quit?: ")
if (Done == 'y'):
  driver.quit()