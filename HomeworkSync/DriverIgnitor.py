from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import getpass as gp


def init_driver():
    """
    Initializes the driver
    :return: None
    """
    global chrome
    options = webdriver.ChromeOptions()
    chrome = webdriver.Chrome(executable_path=r'F:\NSI\NSI\HomeworkSync\res\chromedriver.exe', options=options)
    chrome.get("https://www.ecoledirecte.com/")
    return chrome


def connect():
    # Find the username and password fields
    username = chrome.find_element(by=By.ID, value="username")
    password = chrome.find_element(by=By.ID, value="password")

    # Enter the username and password

    username.send_keys(input("Email : "))
    password.send_keys(gp.getpass("Password : "))

    # Check information provided
    # showpass = chrome.find_element_by_id("show-password")
    # showpass.click()


    login = chrome.find_element(by=By.ID, value="connexion")
    login.click()