from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://stagingpawwow.softgridinfo.in/")

time.sleep(3)

