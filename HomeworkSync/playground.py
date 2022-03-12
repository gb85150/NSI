from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import getpass as gp
import json


"""Help :
# Setup instructions :
# 1. Install selenium (pip install selenium)
# 2. Set chrome driver to path (modify environment variable) (Optional)
# 3. Set executable path to chromedriver executable (Do this if you did not set the environment variable). See line 70.
# 4. Run the script
"""


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


def get_homework_list() -> dict:
    """
    Gets the list of homework by webscraping the ecoledirecte.com website
    :return: None
    """
    homework = chrome.find_element(by=By.XPATH, value='//*[@id="container-menu"]/ed-menu/div/div/div/ul/li[7]/ed-menu-block-item/div/a')
    homework.click()
    time.sleep(1.5)
    hwcalendar = chrome.find_elements(by=By.CLASS_NAME, value="date")
    dico_devoirs = {}

    # Boucle sur les dates
    for i in range(len(hwcalendar)):
        print(hwcalendar[i].text)
        print("\n")
        dico_devoirs[hwcalendar[i].text] = {}
        current_date = hwcalendar[i].text
        hwcalendar[i].click()
        time.sleep(1)
        back=chrome.find_element(by=By.XPATH, value='/html/body/app-root/div/ed-authenticated-layout/div[2]/div[2]/ed-cdt/ed-cdt-eleve/div/div/div[2]/div[2]/ed-cdt-eleve-onglets/ul/li[9]/a')
        
        print("Check ({}/{})".format(i+1, len(hwcalendar)))
        
        # Get all the homework
        tmphw_title=chrome.find_elements(by=By.XPATH, value='/html/body/app-root/div/ed-authenticated-layout/div[2]/div[2]/ed-cdt/ed-cdt-eleve/div/div/div[2]/div[1]/div/ed-cdt-eleve-view-day/div/div[2]/div/ed-cdt-eleve-taf-seance/div[1]/h3')
        tmphw_content=chrome.find_elements(by=By.XPATH, value='/html/body/app-root/div/ed-authenticated-layout/div[2]/div[2]/ed-cdt/ed-cdt-eleve/div/div/div[2]/div[1]/div/ed-cdt-eleve-view-day/div/div[2]/div/ed-cdt-eleve-taf-seance/div[2]/div/div[1]/p/p')
        
        # Print the homework
        for i in range(len(tmphw_title)):
            print("Matière : {}".format(tmphw_title[i].text))
            print("==========================================================")
            print("Tâche : \n{}".format(tmphw_content[i].text))
            print("==========================================================")

            # Add the homework to the dictionary
            tmphw_title=chrome.find_elements(by=By.XPATH, value='/html/body/app-root/div/ed-authenticated-layout/div[2]/div[2]/ed-cdt/ed-cdt-eleve/div/div/div[2]/div[1]/div/ed-cdt-eleve-view-day/div/div[2]/div/ed-cdt-eleve-taf-seance/div[1]/h3')
            tmphw_content=chrome.find_elements(by=By.XPATH, value='/html/body/app-root/div/ed-authenticated-layout/div[2]/div[2]/ed-cdt/ed-cdt-eleve/div/div/div[2]/div[1]/div/ed-cdt-eleve-view-day/div/div[2]/div/ed-cdt-eleve-taf-seance/div[2]/div/div[1]/p/p')
            tmphw_isDone=chrome.find_elements(by=By.XPATH, value='/html/body/app-root/div/ed-authenticated-layout/div[2]/div[2]/ed-cdt/ed-cdt-eleve/div/div/div[2]/div[1]/div/ed-cdt-eleve-view-day/div/div[2]/div/ed-cdt-eleve-taf-seance/div[1]/p/label/input')
            swap = {}
            swap[tmphw_title[i].text] = {
                "Travail" : tmphw_content[i].text,
                "IsDone" : tmphw_isDone[i].is_selected()}
            dico_devoirs[current_date] = swap
        
        # Go back to the summery
        back.click()
        time.sleep(1)
        hwcalendar = chrome.find_elements(by=By.CLASS_NAME, value="date")
    return dico_devoirs


def save_homework_list(dico: dict):
    """
    Saves the homework list to a JSON file with json.dump()
    :param dico: The homework
    :return: None
    """
    with open("HomeworkSync/homework.json", "w") as f:
        json.dump(dico, f, indent=4)


def init_driver() -> None:
    """
    Initializes the driver
    :return: None
    """
    global switch
    global chrome
    switch = True
    options = webdriver.ChromeOptions()
    chrome = webdriver.Chrome(executable_path=r'F:\NSI\NSI\HomeworkSync\res\chromedriver.exe', options=options)
    chrome.get("https://www.ecoledirecte.com/")
    return None


if __name__ == "__main__":
    print("\nStarting... Please prepare your logins\n \n \n")
    init_driver()	
    connect()
    time.sleep(3)
    save_homework_list(get_homework_list())
    print("\n \n \n finished...\n \n \n")
    time.sleep(3)
    chrome.quit() if switch == True else None
