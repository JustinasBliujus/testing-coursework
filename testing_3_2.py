from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)
time.sleep(1) 
startButton = browser.find_element(By.CLASS_NAME,"trollface")
startButton.click()
new_window = browser.window_handles[1]
first_window = browser.window_handles[0]
browser.switch_to.window(new_window)
x_element = browser.find_element(By.ID, "input_value")
x_value = float(x_element.text)  
result = math.log(abs(12 * math.sin(x_value)))
inputField = browser.find_element(By.NAME,"text")
inputField.send_keys(result)
submitButton = browser.find_element(By.CLASS_NAME,"btn-primary")
submitButton.click()
alert = browser.switch_to.alert
alert_text = alert.text
alert.accept()
print(alert_text)
