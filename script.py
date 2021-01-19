#!/usr/bin/python3
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
import platform

login_email = "censored"
login_passwd = "censored"
post_url = "https://www.facebook.com/MBStoreMongolia/posts/3764409580288912"
group_list = ["ҮНЭГҮЙ ШУУРХАЙ ЗАР МЭДЭЭ","МОНГОЛЫН ХАМГИЙН ТОМ ЗАРЫН ГРУПП", "Хэрэгтэй мэдээллийг эндээс"]

def main():
    path = path_identify()
    driver = init_driver(path)
    driver.get("https://facebook.com/")

    if is_logged_in(driver):
        share(driver, post_url, group_list)  
    else:
        login(driver, login_email, login_passwd)
        share(driver, post_url, group_list) 

def path_identify():
    if platform.system() == "Linux":
        path = "~/.config/google-chrome/Default"
    elif platform.system() == "Darwin":
        path = "~/Library/Application\ Support/Google/Chrome/Default"
    else:
        path = "%HOMEDIR%%HOMEPATH%%\AppData\Local\Google\Chrome\User Data\Default"
    return path

def init_driver(path):
    profile = Options()
    profile.add_argument(f"user-data-dir='{path}'")
    preferences = {"profile.default_content_setting_values.notifications" : 2}
    profile.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=profile)
    return driver

def is_logged_in(driver):
    if "Facebook - Log In or Sign Up" == driver.title:
        return False
    else:
        return True

def login(driver, login_email, login_passwd):
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    email.send_keys(login_email)
    password.send_keys(login_passwd)
    driver.find_element_by_id("u_0_b").click()

def share(driver, post_url, group_list):

    time.sleep(2)
    driver.get(post_url)
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div[3]/div/div[1]/div[2]/span").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div/div/span/span").click()
    time.sleep(4)
    for group in group_list:
        textarea = driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[3]/div/div[1]/div/label/input")
        textarea.click()
        textarea.send_keys(group)
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div/span/span").click()
        time.sleep(2)
        textarea.send_keys(Keys.CONTROL + "a")
        textarea.send_keys(Keys.DELETE)
        

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
