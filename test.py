from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import os


def running():
    opt = Options()
    #opt.headless = True
    driver1 = webdriver.Chrome(options=opt)
    driver1.set_window_size(800, 600)
    driver1.get("https://aviso.bz/login")
    print("please wait...")
    # load cookies
    with open('./cookies/account_1.json', 'r') as f:
        cookies = json.load(f)
    time.sleep(2)
    for cookie in cookies:
        driver1.add_cookie(cookie)
    time.sleep(2)
    driver1.refresh()
    window_before = driver1.window_handles[0]
    driver1.get("https://aviso.bz/work-youtube")
    time.sleep(2)
    coin = WebDriverWait(driver1, 60).until(
    EC.presence_of_element_located((By.ID,"new-money-ballans"))).text
    print(coin)
    time.sleep(2)
    text = WebDriverWait(driver1, 60).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/table/tbody/tr[3]/td[2]/div[2]/table/tbody/tr/td[3]/div/span[1]"))).text
    wait = text[0:2]
    print(wait)
    time.sleep(2)
    WebDriverWait(driver1, 60).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/table/tbody/tr[3]/td[2]/div[2]/table/tbody/tr/td[2]/div[1]/span[1]"))).click()
    time.sleep(3)
    WebDriverWait(driver1, 60).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/table/tbody/tr[3]/td[2]/div[2]/table/tbody/tr/td[2]/div[1]/div/div/span[1]"))).click()
    
    window_after = driver1.window_handles[1]
    driver1.switch_to.window(window_after)
    time.sleep(2)
    driver1.switch_to.frame(WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.XPATH,'//iframe[starts-with(@src, "https://www.youtube.com/embed")]'))))

    WebDriverWait(driver1, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()
    new_wait = int(wait) + 9
    time.sleep(new_wait)
    time.sleep(0.5)
    driver1.get("https://aviso.bz/")
    file_path = "./cookies/account_1.json"
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} delete successfully..")
    cookies = driver1.get_cookies()
    for cookie in cookies:
        if 'expiry' in cookie:
            del cookie['expiry']
    new = "./cookies/account_1.json"
    with open(new, 'w') as f:
        json.dump(cookies, f)
    print("cookies copied done..")
    driver1.quit()



while True:
    try:
      running()
      time.sleep(5)
    except:
        continue
