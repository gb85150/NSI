from selenium.webdriver.common.by import By
from DriverIgnitor import ChromeDriver
from LoginPrompt import login
import time
import json


"""Help :
# Setup instructions :
# 1. Install selenium (pip install selenium)
# 2. Set chrome driver to path (modify environment variable) (Optional)
# 3. Set executable path to chromedriver executable (Do this if you did not set the environment variable). See line 70.
# 4. Run the script
"""


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
        tmphw_content=chrome.find_elements(by=By.CLASS_NAME, value='contenu-non-maitrise')
        
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
            tmphw_sumup = ''
            for j in range(len(tmphw_content)):
                tmphw_sumup += tmphw_content[j].text
                tmphw_sumup += "\n"
            swap = {}
            swap[tmphw_title[i].text] = {
                "Travail" : tmphw_sumup.text,
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


if __name__ == "__main__":
    switch = True
    print("\nStarting... Please prepare your logins\n \n \n")
    email, password = login()
    chromeobject = ChromeDriver(email, password)
    chrome = chromeobject.get_driver()
    time.sleep(3)
    save_homework_list(get_homework_list())
    print("\n \n \n finished...\n \n \n")
    time.sleep(3)
    chrome.quit() if switch == True else None
