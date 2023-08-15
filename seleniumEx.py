from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
sleep(2)
input = driver.find_element(By.NAME,"q")
input.send_keys("kodlamaio")

searchButton = driver.find_element(By.NAME, "btnK")
sleep(2)
searchButton.click()
firstResult = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/a")
firstResult.click()
# firstResult = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/a")
# firstResult.click()
# listOfCourses = driver.find_elements(By.CLASS_NAME, "course-listing")
# print(f"kodlama ioda şu anda {len(listOfCourses)} adet kurs var ")

while True:
    continue


#HTML LOCATORS
#full Xpath
#/html/body/div[6]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/a
#Xpath
#//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/a