from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_Kodlama:
    def test_invalid_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)
        #en fazla 5 saniye olacak şekilde user-name id'li elementin görünmesini bekle
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"test sonucu: {testResult}")
        sleep(100)
testClass = Test_Kodlama()
testClass.test_invalid_login()
while True:
    continue