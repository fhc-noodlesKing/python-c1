from selenium import webdriver
import time
# 打开浏览器，driver浏览器的实例化句柄
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("http://132.232.44.158:9999/shopxo")
time.sleep(2)

driver.find_element_by_partial_link_text('斜挎风琴包').click()
print(driver.title)

driver.switch_to_window(driver.window_handles[-1])
print(driver.title)