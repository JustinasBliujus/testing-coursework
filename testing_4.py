import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestFormFilling(unittest.TestCase): #testas tikrina kad butu suvesta visa informacija, t.y. iesko 5 input field. Jeigu taip yra tada iesko success zinutes.
    
    def setUp(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.driver = webdriver.Chrome()
        self.driver.get(link)
    
    def test_fill_form(self):
        dataset = {
            "name": "Juozas",
            "surname": "Juozopavarde",
            "email": "Juozopavarde@example.com",
            "phone": "+1234567890",
            "address": "123 Vilniaus g."
        }
        
        input_fields = self.driver.find_elements(By.TAG_NAME, 'input')
        
        data_keys = list(dataset.keys())

        for i, input_field in enumerate(input_fields):
            if i < len(data_keys):  
                field_name = data_keys[i]
                input_field.send_keys(dataset[field_name])
                
        unused_data = [value for i, value in enumerate(dataset.values()) if i >= len(input_fields)]
        self.assertEqual(len(unused_data), 0, f"Unused data: {unused_data}")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button.btn") 
        submit_button.click()
        self.driver.implicitly_wait(5)  
        success_message = self.driver.find_element(By.XPATH, "//h1[text()='Congratulations! You have successfully registered!']")
        self.assertTrue(success_message.is_displayed(), "Success message not displayed")

if __name__ == "__main__":
    unittest.main()
