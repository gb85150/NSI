from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Setup instructions :
# 1. Install selenium (pip install selenium)
# 2. Set chrome driver to path (modify environment variable)
# 3. Set executable path to chromedriver executable
# 4. Run the script


def connect():
    # Find the username and password fields
    username = chrome.find_element_by_id("username")
    password = chrome.find_element_by_id("password")

    # Enter the username and password

    username.send_keys("geoffrey.bousseau@gmail.com")
    password.send_keys("01099011109gb")

    # Check information provided
    showpass = chrome.find_element_by_id("show-password")
    showpass.click()


    login = chrome.find_element_by_id("connexion")
    login.click()


# Initialize the driver
chrome = webdriver.Chrome(executable_path=r'F:\NSI\NSI\HomeworkSync\res\chromedriver.exe')
chrome.get("https://www.ecoledirecte.com/")


if __name__ == "__main__":
    connect()
    time.sleep(3)
    homework = chrome.find_element(by=By.XPATH, value='//*[@id="container-menu"]/ed-menu/div/div/div/ul/li[7]/ed-menu-block-item/div/a')
    homework.click()
    hwcalendar = chrome.find_elements(by=By.CSS_SELECTOR, value=".date")
    for i in hwcalendar:
        print(i.text)
        i.click()
        time.sleep(3)
        chrome.back()
        time.sleep(3)