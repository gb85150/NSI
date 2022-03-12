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


class ChromeDriver:
    def __init__(self):
            """
            Initializes the driver
            :return: None
            """
            options = webdriver.ChromeOptions()
            self.chrome = webdriver.Chrome(executable_path=r'F:\NSI\NSI\HomeworkSync\res\chromedriver.exe', options=options)
            self.chrome.get("https://www.ecoledirecte.com/")
            self.__connect()
    
    
    def __connect(self):
        """
        Find the username and password fields.
        Enter the username and password.
        Check information provided.
        :return: None
        """
        # Find the username and password fields
        self.__username = self.chrome.find_element(by=By.ID, value="username")
        self.__password = self.chrome.find_element(by=By.ID, value="password")

        # Enter the username and password

        self.__username.send_keys(input("Email : "))
        self.__password.send_keys(gp.getpass("Password : "))

        # Check information provided
        # showpass = chrome.find_element_by_id("show-password")
        # showpass.click()


        login = self.chrome.find_element(by=By.ID, value="connexion")
        login.click()


    # Getters and Setters
    def get_driver(self) -> webdriver:
        return self.chrome
    
    def get_username(self) -> str:
        return self.__username
    
    def get_password(self) -> str:
        return self.__password
    
    def set_username(self, username:str):
        self.__username = username
    
    def set_password(self, password:str):
        self.__password = password