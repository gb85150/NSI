from multiprocessing.sharedctypes import Value
from types import MethodType
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
    username = chrome.find_element(by=By.ID, value="username")
    password = chrome.find_element(by=By.ID, value="password")

    # Enter the username and password

    username.send_keys("geoffrey.bousseau@gmail.com")
    password.send_keys("01099011109gb")

    # Check information provided
    # showpass = chrome.find_element_by_id("show-password")
    # showpass.click()


    login = chrome.find_element(by=By.ID, value="connexion")
    login.click()


# Initialize the driver
chrome = webdriver.Chrome(executable_path=r'E:\NSI\NSI\HomeworkSync\res\chromedriver.exe')
chrome.get("https://www.ecoledirecte.com/")


if __name__ == "__main__":
    print("\n \n \n starting...\n \n \n")	
    connect()
    time.sleep(3)
    homework = chrome.find_element(by=By.XPATH, value='//*[@id="container-menu"]/ed-menu/div/div/div/ul/li[7]/ed-menu-block-item/div/a')
    homework.click()
    time.sleep(1.5)
    hwcalendar = chrome.find_elements(by=By.CLASS_NAME, value="date")
    for i in range(len(hwcalendar)):
        print(hwcalendar[i].text)
        hwcalendar[i].click()
        time.sleep(1)
        back=chrome.find_element(by=By.XPATH, value='/html/body/app-root/div/ed-authenticated-layout/div[2]/div[2]/ed-cdt/ed-cdt-eleve/div/div/div[2]/div[2]/ed-cdt-eleve-onglets/ul/li[9]/a')
        print("Check ({}/{})".format(i+1, len(hwcalendar)))
        back.click()
        time.sleep(1)
        hwcalendar = chrome.find_elements(by=By.CLASS_NAME, value="date")
    # daytab = chrome.find_element(by=By.XPATH, value='/html/body/app-root/div/ed-authenticated-layout/div[2]/div[2]/ed-cdt/ed-cdt-eleve/div/div/div[2]/div[2]/ed-cdt-eleve-onglets/ul/li[2]/a')
    # daytab.click()
    print("\n \n \n finished...\n \n \n")

# NB : 0.7s serait peut etre bien pour le sleep