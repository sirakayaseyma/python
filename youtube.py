from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.youtube.com/")
sleep(2)
input = driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
input.send_keys("osman")
sleep(2)
butonClc = driver.find_element(By.XPATH, "//*[@id='search-icon-legacy']/yt-icon/yt-icon-shape/icon-shape/div")
butonClc.click()
sleep(6)

while True:
    continue