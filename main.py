from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
import names
import time
from pyfiglet import figlet_format
import random
from termcolor import cprint

from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

cprint(figlet_format(('thebotsmith'), font='doom'), attrs=['bold'])

chromepath = "c:\chromedriver"
# set your chrome driver path here ^

with open('accounts.txt') as f:
    credentials = map(lambda r: tuple(r.split(':')), [row for row in f.read().splitlines()])
for credential in credentials:

    driver = webdriver.Chrome()
    actions = ActionChains(driver)

    username, password = credential
    url = "https://www.google.com/"
    driver.get(url)

    button1 = driver.find_element_by_xpath('//*[@id="gb_70"]')
    button1.click()
    email = "email"
   
    login = driver.find_element_by_xpath('//*[@id="identifierId"]')
    login.send_keys(username)
    next0 = driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
    next0.click()

    passw = WebDriverWait(driver, 5).until(
       EC.presence_of_element_located(('xpath','//*[@id="password"]/div[1]/div/div[1]/input')))

  
    time.sleep(1)
    passw.send_keys(password)
    time.sleep(1)
    final = driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
    final.click()
    print(" ")
    print(Fore.GREEN + ("Logged in to google!"))
    print(" ")
    time.sleep(1)
    yt = "https://www.youtube.com/watch?v=YBqDATEltNE"

    driver.get(yt)
    print(Fore.GREEN + ("started youtube video"))
    print(" ")
    time.sleep(300)
    driver.get(url)

    print(Fore.GREEN + ("starting google searches"))
    print(" ")

    search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
    search.send_keys('cook')
    actions.send_keys(Keys.ENTER)



    for i in range(10):
        random = names.get_full_name()
        searchurl = "https://www.google.com/search?source=hp&ei=IrI6W_e4EMnn5gLloKzgDQ&q={}&oq={}&gs_l=psy-ab.12..0j0i131k1j0l4j0i131k1l2j0l2.1514.155452.0.177155.20.5.15.0.0.0.110.250.4j1.5.0....0...1c.1.64.psy-ab..0.20.340...0i10k1.0.wl_aQzdHSe4".format(random,random)

        time.sleep(10)
        driver.get(searchurl)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(10)
        

    
    driver.get(url)
    print(Fore.GREEN + ("completed google searches"))
    print(" ")
    print(Fore.GREEN + ("{} Done!!").format(username))
    print(" ")
    driver.delete_all_cookies()
    driver.close()

print(Fore.GREEN + "All account done")
