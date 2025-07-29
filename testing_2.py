from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://www.facebook.com/r.php?entry_point=login&locale=lt_LT"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(1) 

try:
    cookie_button = browser.find_element(By.XPATH, "//span[contains(text(), 'Atmesti nebūtinus slapukus')]")
    print("Cookie popup found.")
    cookie_button.click()
    print("Cookies rejected!")
except Exception as e:
    print("No cookie popup found or error:", str(e))

time.sleep(1) 
nameInput = browser.find_element(By.NAME, "firstname")
nameInput.send_keys("Juozukas")
surnameInput = browser.find_element(By.NAME, "lastname")
surnameInput.send_keys("Juozukopavarde")
year = Select(browser.find_element(By.NAME, "birthday_year"))
year.select_by_value("1995")
month = Select(browser.find_element(By.NAME, "birthday_month"))
month.select_by_value("6") 
day = Select(browser.find_element(By.NAME, "birthday_day"))
day.select_by_value("15") 
gender = browser.find_element(By.XPATH, "//input[@value='2']")  
gender.click()
email = browser.find_element(By.NAME, "reg_email__")
email.send_keys("juozukas96254245@gmail.com")
password = browser.find_element(By.NAME, "reg_passwd__")
password.send_keys("saugusslaptazodis4352354#$")
button = browser.find_element(By.NAME, "websubmit")
button.click()

time.sleep(40)
