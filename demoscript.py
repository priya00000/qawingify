from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_page(driver):
   
    driver.get("https://sakshingp.github.io/assignment/login.html")

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("validUsername")
    password_input.send_keys("validPassword")
    login_button.click()
    
    
    assert "Welcome" in driver.page_source, "login failed

    
    username_input.clear()
    password_input.clear()
    login_button.click()

 
    assert "username must be present" in driver.page_source, "Empty username validation failed"
    assert "password must be present" in driver.page_source, "Empty password validation failed"



def test_home_page(driver):

    amount_header = driver.find_element(By.XPATH, "//th[text()='AMOUNT']")
    amount_header.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@data-title='Amount']")))

    amount_values = driver.find_elements(By.XPATH, "//td[@data-title='Amount']")

  
    assert is_sorted(amount_values), "AMOUNT column is not sorted"

def is_sorted(elements):

    element_texts = [element.text for element in elements]
    numeric_values = [float(text.replace(',', '')) for text in element_texts]
    return numeric_values == sorted(numeric_values)

driver = webdriver.Firefox()
driver_path = '/path/to/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)


try:
    test_login_page(driver)
    test_home_page(driver)

finally:
    driver.quit()
