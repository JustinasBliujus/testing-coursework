import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

class TestRegistrationForms:
    
    def fill_form(self, driver, link, dataset):
        driver.get(link)
        input_fields = driver.find_elements(By.TAG_NAME, 'input')
        data_keys = list(dataset.keys())
        
        for i, input_field in enumerate(input_fields):
            if i < len(data_keys): 
                field_name = data_keys[i]
                input_field.send_keys(dataset[field_name])

        unused_data = [value for i, value in enumerate(dataset.values()) if i >= len(input_fields)]
        
        assert len(unused_data) == 0, f"Unused data: {unused_data}"
        
        submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        submit_button.click()
        driver.implicitly_wait(5) 
        success_message = driver.find_element(By.XPATH, "//h1[text()='Congratulations! You have successfully registered!']")
        assert success_message.is_displayed(), "Success message not displayed"
    
    def test_registration_form_1(self, driver):
        dataset = {
            "name": "Juozas",
            "surname": "Juozopavarde",
            "email": "Juozopavarde@example.com",
            "phone": "+1234567890",
            "address": "123 Vilniaus g."
        }
        link = "http://suninjuly.github.io/registration1.html"
        self.fill_form(driver, link, dataset)

    def test_registration_form_2(self, driver):
        dataset = {
            "name": "Jonas",
            "surname": "Jonaitis",
            "email": "Jonaitis@example.com",
            "phone": "+9876543210",
            "address": "456 Kauno g."
        }
        link = "http://suninjuly.github.io/registration2.html"
        self.fill_form(driver, link, dataset)
