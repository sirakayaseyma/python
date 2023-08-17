from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class Test_Kodlama:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")


    def test_invalid_login(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        passwordInput = self.driver.find_element(By.ID, "password")
        #en fazla 5 saniye olacak şekilde user-name id'li elementin görünmesini bekle
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"test sonucu: {testResult}")

    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID, "password")
        

        #en fazla 5 saniye olacak şekilde user-name id'li elementin görünmesini bekle
        #action Chains
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput, "standard_user")
        actions.send_keys_to_element(passwordInput, "secret_sauce")
        actions.perform()
        # usernameInput.send_keys("standard_user")
        # passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(20)

      


testClass = Test_Kodlama()
testClass.test_invalid_login()
testClass.test_valid_login()
while True:
    continue