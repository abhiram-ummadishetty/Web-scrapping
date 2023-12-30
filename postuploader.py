from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


# def croping_image():
#     driver.find_element(By.XPATH, "//*[@aria-label='Select crop']").click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, "//*[@aria-label='Photo outline icon']").click()
#     time.sleep(2)
#     # driver.find_element(By.XPATH, "//*[@aria-label='Open media gallery']").click()
#     # time.sleep(2)

def connecion_est():
    upload_files = os.path.join(os.path.abspath(__file__ + "/../"), "images")
    print(os.listdir(upload_files))

    images = []

    for ul in os.listdir(upload_files):
        images.append(ul)
        print(f'{upload_files}\{ul}')
    length = len(images)
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    url = "https://www.instagram.com/"
    driver.get(url)
    return driver,length,upload_files

def login(Username,Password,driver):
    username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='username']")))
    password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='password']")))
    username.clear()
    username.send_keys(Username)
    password.clear()
    password.send_keys(Password)
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@tabindex=0]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Not Now')]").click()
    time.sleep(2)

def post(driver,upload_files,length):
    driver.find_element(By.XPATH, "//*[@aria-label='New post']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'Select from computer')]").click()

    count = 1
    for ul in os.listdir(upload_files):
        time.sleep(2)
        pyautogui.typewrite(f"{upload_files}\{ul}")
        pyautogui.press('enter')
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@aria-label='Select crop']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@aria-label='Photo outline icon']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@aria-label='Open media gallery']").click()
        time.sleep(2)
        if count!=length:
            driver.find_element(By.XPATH, "//*[@aria-label='Plus icon']").click()
            time.sleep(2)
        count = count+1

    driver.find_element(By.XPATH, "//div[contains(text(),'Next')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[contains(text(),'Next')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[contains(text(),'Share')]").click()
    time.sleep(5)





