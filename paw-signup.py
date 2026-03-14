from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://grocery.softgridinfo.in/admin/dashboard")
time.sleep(5)

# Open Sign Up form
#driver.find_element(By.XPATH, "//button[contains(text(),'Sign')]").click()
driver.find_element(By.XPATH, "//*[@id='root']/header[1]/div/a[2]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[4]/p/button").click()
time.sleep(3)
 # Fill Sign Up form
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Sadhana")
print("Sadhana")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("testdummy2320@gmail.com")
print("sadhanagavandgave602@gmail.com")
driver.find_element(By.XPATH, "//input[@name='mobile']").send_keys("9529589724")
print("9529589724")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Sadu@1234")
print("Sadu@1234")
driver.find_element(By.XPATH, "//input[@name='confirmPassword']").send_keys("Sadu@1234")
print("Sadu@1234")
driver.find_element(By.XPATH, "//input[@type='checkbox']").click() #submit Sign up form
# OTP field for OTP we use manual OTP entry
driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[8]/button").click()
time.wait(60) # for time resume

#driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/form/p[2]").send_keys("")

#driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/form/p[3]").send_keys("")
driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/form/button[2]").click() #submit both OTP
time.sleep(3)





