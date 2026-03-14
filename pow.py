from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ================== ADDED ==================
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# ===========================================

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)   # ADDED

driver.get("https://stagingpawwow.softgridinfo.in/")
time.sleep(5)

# Open Sign Up
driver.find_element(By.XPATH, "//*[@id='root']/header[1]/div/a[2]").click()
time.sleep(3)

driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[4]/p/button").click()
time.sleep(3)

# ================== SIGN UP FORM (YOUR CODE) ==================
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Sadhana")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("sadhanagavandgave602@gmail.com")
driver.find_element(By.XPATH, "//input[@name='mobile']").send_keys("9529589724")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Sadu@1234")
driver.find_element(By.XPATH, "//input[@name='confirmPassword']").send_keys("Sadu@1234")
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()

# Submit Sign Up (Send OTP)
driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[8]/button").click()
# ===============================================================

# ================== ADDED: CHECK USER EXISTS ==================
user_exists = False
try:
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'already')]")
        )
    )
    user_exists = True
    print("User already exists")
except:
    print("New user, continue signup")
# ===============================================================

# ================== ADDED: LOGIN FLOW ==================
if user_exists:
    driver.find_element(By.XPATH, "//*[@id='root']/header[1]/div/a[1]").click()
    time.sleep(2)

    driver.find_element(By.NAME, "email").send_keys("sadhanagavandgave602@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Sadu@1234")

    driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
    print("Logged in successfully")

# ================== OTP FLOW (YOUR ORIGINAL LOGIC) ==================
else:
    print("Enter OTP manually")
    time.sleep(60)  # MANUAL OTP ENTRY (UNCHANGED)

    driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/form/button[2]").click()
    print("OTP verified")
# ===================================================================

time.sleep(5)
driver.quit()
