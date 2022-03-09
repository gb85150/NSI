from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import getpass as gp


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

    username.send_keys(input("Email : "))
    password.send_keys(gp.getpass("Password : "))

    # Check information provided
    # showpass = chrome.find_element_by_id("show-password")
    # showpass.click()


    login = chrome.find_element(by=By.ID, value="connexion")
    login.click()


def print_homework_list() -> None:
    """
    Prints the list of homework by webscraping the ecoledirecte.com website
    :return: None
    """
    homework = chrome.find_element(by=By.XPATH, value='//*[@id="container-menu"]/ed-menu/div/div/div/ul/li[7]/ed-menu-block-item/div/a')
    homework.click()
    time.sleep(1.5)
    hwcalendar = chrome.find_elements(by=By.CLASS_NAME, value="date")
    for i in range(len(hwcalendar)):
        print(hwcalendar[i].text)
        print("\n")
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
        
        # Go back to the summery
        back.click()
        time.sleep(1)
        hwcalendar = chrome.find_elements(by=By.CLASS_NAME, value="date")
    return None


# Initialize the driver
switch = False
options = webdriver.ChromeOptions()
chrome = webdriver.Chrome(executable_path=r'E:\NSI\NSI\HomeworkSync\res\chromedriver.exe', options=options)
chrome.get("https://www.ecoledirecte.com/")


if __name__ == "__main__":
    print("\nStarting... Please prepare your logins\n \n \n")	
    connect()
    time.sleep(3)
    print_homework_list()
    print("\n \n \n finished...\n \n \n")
    time.sleep(3)
    chrome.quit() if switch == True else None

# NB : 0.7s serait peut etre bien pour le sleep
# test = chrome.find_element(by=By.ID, value="test")
# print(test.is_selected())














dico = {
    "Day" : {
        "Subject" : {
            "Task" : "Content",
            "IsDone" : False
        },
        "AnotherSubject" : {
            "Task" : "Content",
            "IsDone" : True
        }
    },
    "AnotherDay" : {
        "Subject" : {
            "Task" : "Content",
            "IsDone" : False
        }
    }
}
with open("test.txt", "w") as f:
    f.write(dico)