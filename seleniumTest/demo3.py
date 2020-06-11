from selenium import webdriver
import time
# 打开浏览器，driver浏览器的实例化句柄
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("http://132.232.44.158:9999/shopxo/admin.php")
time.sleep(2)

driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[1]/input').send_keys("admin")
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[2]/input').send_keys("shopxo")
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[3]/button').click()

time.sleep(2)
# 切换元素

iframe = driver.find_element_by_id('ifcontent')
driver.switch_to_frame(iframe)

e = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[1]/div/p[2]')
print(e.text)

driver.switch_to_default_content()
e = driver.find_element_by_xpath('//*[@id="admin-offcanvas"]/div/ul/li[1]/a/span[2]')
print(e.text)