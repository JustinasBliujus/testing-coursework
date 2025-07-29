# Testing - coursework

This repository contains a few testing assignments using **Python**, with tools such as `unittest`, `pytest`, and `selenium`.

---

## Repository Structure

- `testing_1.py` → Unit tests on personal code from another subject `AI1.py`(Task 1)  
- `testing_2.py` → Selenium script to fill out a web form (Task 2)  
- `testing_3_1.py` → Test for JS alert acceptance and CAPTCHA (Task 3.1)  
- `testing_3_2.py` → Test for redirect and CAPTCHA on new tab (Task 3.2)  
- `testing_4.py` → Test for two registration forms with `unittest` (Task 4)  
- `testing_5.py` → Pytest version of Task 4 using fixtures and class-based tests (Task 5)
- `fuma_free_test_plan.pdf` → Making a testplan for a fictional project (Task 6)
---

## Task Overview

### Task 1 – Unit Testing (20–30 Tests)
- **Tool:** `unittest`
- **Goal:** Create 20–30 meaningful unit tests on your own Python codebase.
- **Focus:** Test logic, edge cases, exceptions, and data handling.

### Task 2 – Web Form Automation
- **Tool:** `selenium`
- **Goal:** Automate filling out a form on any publicly available website.
- **Skills:** Element selection, interaction, and submission.

### Task 3.1 – JavaScript Alert + CAPTCHA
- **Site:** [suninjuly.github.io/alert_accept.html](http://suninjuly.github.io/alert_accept.html)
- **Steps:**  
  1. Click the button  
  2. Accept JavaScript confirm  
  3. Solve CAPTCHA challenge  
  4. Submit the answer

### Task 3.2 – Redirect & New Tab Handling
- **Site:** [suninjuly.github.io/redirect_accept.html](http://suninjuly.github.io/redirect_accept.html)
- **Steps:**  
  1. Click the button to open a new tab  
  2. Switch to the new tab  
  3. Solve CAPTCHA  
  4. Submit the answer

### Task 4 – Positive and Negative Form Test with `unittest`
- **Sites:**
  - [registration1.html](http://suninjuly.github.io/registration1.html) – Should **pass**
  - [registration2.html](http://suninjuly.github.io/registration2.html) – Should **fail**
- **Tool:** `unittest`
- **Approach:** Use `TestCase` class, assertions, and test structure.

### Task 5 – Pytest Version of Task 4
- **Tool:** `pytest`
- **Features:**
  - Use of fixtures to manage browser instance.
  - Separate browser session for each test.
  - Tests implemented as class methods.

### Task 6 - Brief testplan for a fictional project
- **Features:**
  - Following IEEE 829 standard.
  - The project is about a mobile app for quiting smoking.
---



