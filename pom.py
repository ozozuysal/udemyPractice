from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground/'

    def go(self):
        self.driver.get(self.url)

    def type_into_input_field(self, text):
        inpt =  self.driver.find_element(By.ID, 'ipt1')
        inpt.clear()
        inpt.send_keys(text)
        return None


    def get_input_text(self):
        inpt = self.driver.find_element(By.ID, 'ipt1')
        elem_text = input.get_attribute('value')
        return elem_text

    def click_button_1(self):
        button = self.driver.find_element(By.ID, 'ipt1')
        button.click()
        return None


#Test

browser = webdriver.Chrome()
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
trng_page.type_into_input_field('Thats Ok')
trng_page.click_button_1()

