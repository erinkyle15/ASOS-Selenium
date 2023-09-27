from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.asos.com')
time.sleep(1) 

my_account_dropdown = driver.find_element(By.CLASS_NAME, "OVxuqjQ") 
actions = ActionChains(driver)
actions.move_to_element(my_account_dropdown).perform()
time.sleep(1)

join = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Join']"))
)
join.click()

user_email_field = driver.find_element(By.ID, "Email")
actions.move_to_element(user_email_field).perform()
email = "erinkyle@email.com"  
user_email_field.send_keys(email)
time.sleep(1)

first_name_field = driver.find_element(By.ID, "FirstName")
actions.move_to_element(first_name_field).perform()
name = "erin"  
first_name_field.send_keys(name)
time.sleep(1)

last_name_field = driver.find_element(By.ID, "LastName")
actions.move_to_element(last_name_field).perform()
surname = "kyle"  
last_name_field.send_keys(surname)
time.sleep(1)

password_field = driver.find_element(By.ID, "Password")
actions.move_to_element(password_field).perform()
password = "Selenium12345"  
password_field.send_keys(password)
time.sleep(1)

# Click on the day dropdown
birth_day_dropdown = driver.find_element(By.ID, 'BirthDay') 
select_birth_day = Select(birth_day_dropdown)
select_birth_day.select_by_index(18)
time.sleep(1)

birth_month_dropdown = driver.find_element(By.ID, 'BirthMonth') 
select_birth_month = Select(birth_month_dropdown)
select_birth_month.select_by_index(5)
time.sleep(1)

birth_year_dropdown = driver.find_element(By.ID, 'BirthYear') 
select_birth_year = Select(birth_year_dropdown)
select_birth_year.select_by_index(9)
time.sleep(1)

register = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID,  'register'))
)
register.click()

time.sleep(5)

driver.quit()
