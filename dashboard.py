from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://stagingpawwow.softgridinfo.in/")
wait = WebDriverWait(driver, 10)

# Login button (Home page)
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Login')]"))).click()


# Email
wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys("testdummy2320@gmail.com")

# Password
wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("Sadu@123")

# Submit button
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

# Profile icon
profile_icon = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "svg.lucide-user"))
)
profile_icon.click()


# Use JS click (safe for SVG)
#driver.execute_script("arguments[0].click();", profile_icon)

# -----------------------------
# Step 2: Click Logout
# -----------------------------
logout = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//p[text()='Log Out']"))
)

logout.click()

# -----------------------------
# Step 3: Handle Confirmation Popup
# -----------------------------

# OPTION 1 → Click OK (Confirm Logout)
ok_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='OK']]"))
)
ok_button.click()
# OPTION 2 → Click Cancel (if needed)
# cancel_button = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//button[text()='Cancel']"))
# )
# cancel_button.click()

# -----------------------------
# Step 4: Verification (Optional but IMPORTANT)
# -----------------------------
# Example: check login page visible after logout
wait.until(EC.url_contains("login"))
print("Logout successful")
assert "login" in driver.current_url
# Close browser
driver.quit()



