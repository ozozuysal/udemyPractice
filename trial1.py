from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/training-ground")
browser.maximize_window()
assert "Training Ground" in browser.title

browser.find_element(By.ID, 'ipt1').click()
browser.find_element(By.ID, 'ipt1').send_keys("ozgur ozuysal")
browser.find_element(By.ID, 'b1').click()

wait = WebDriverWait(browser, 5)
wait.until(EC.alert_is_present())

print("Popup message")

alert = browser.switch_to.alert
assert "You clickedButton1." in alert.text
alert.accept()

print("Completed")



browser.close()
