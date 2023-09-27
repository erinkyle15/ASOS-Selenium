from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.asos.com')
time.sleep(1)

my_account_dropdown = driver.find_element(By.CLASS_NAME, "OVxuqjQ") 
actions = ActionChains(driver)
actions.move_to_element(my_account_dropdown).perform()
time.sleep(1)

sign_in = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Sign In']"))
)

sign_in.click()

user_login_field = driver.find_element(By.ID, "EmailAddress")
actions.move_to_element(user_login_field).perform()
username = "erinkyle@email.com"  
user_login_field.send_keys(username)
time.sleep(2)

user_password_field = driver.find_element(By.ID, "Password")
actions.move_to_element(user_password_field).perform()
password = "Selenium12345"
user_password_field.send_keys(password)
time.sleep(2)

user_sign_in = driver.find_element(By.ID, "signin")
actions.move_to_element(user_sign_in).perform()
user_sign_in.click()

time.sleep(5)

driver.quit()









