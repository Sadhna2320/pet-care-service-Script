from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.support.ui import webDriverWait   # used for wait as a place of time
#from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://stagingpawwow.softgridinfo.in/")
time.sleep(3)

# Login button
driver.find_element(By.XPATH,"//*[@id='root']/header/div/a[2]").click()
time.sleep(2)

# Create account
driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div/form/div[4]/p/button").click()
time.sleep(2)

# Name
driver.find_element(By.NAME,"name").send_keys("Sadhana")

# Email
driver.find_element(By.NAME,"email").send_keys("testdummy2320@gmail.com")

# Mobile
driver.find_element(By.NAME,"mobile").send_keys("1234567895")

# Password
driver.find_element(By.NAME,"password").send_keys("Sadu@123")

# Confirm Password
driver.find_element(By.NAME,"confirmPassword").send_keys("Sadu@123")

# Checkbox
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()

# Submit
driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(3)

# Check if user already exists
page_text = driver.page_source

if "already exists" in page_text:

    print("User already exists → go to login")

    driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div/form/div[8]/p/button").click()

    driver.find_element(By.NAME,"email").send_keys("testdummy2320@gmail.com")
    driver.find_element(By.NAME,"password").send_keys("Sadu@123")

    driver.find_element(By.XPATH,"//button[@type='submit']").click()

else:

    print("Signup successful → OTP verification")

    input("Enter OTP manually then press ENTER...")

    driver.find_element(By.XPATH,"//button[contains(text(),'Verify')]").click()

time.sleep(5)
#display dashboard now click on profile icon
driver.find_element(By.XPATH,"//*[@id='root']/header[2]/div[2]/div[3]/svg").click()
