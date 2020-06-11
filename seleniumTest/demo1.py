from selenium import webdriver
import time
# 打开浏览器，driver浏览器的实例化句柄
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("http://superf.xyz:8080/ljindex/index.html")

# # id定位
# driver.find_element_by_id('kw').send_keys("哈哈哈哈")
# driver.find_element_by_id('su').click()

# xpath 位置定位
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys("111111")
# driver.find_element_by_xpath('//*[@id="su"]').click()
driver.find_element_by_xpath('//*[@id="unlogin"]/div[1]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="username"]').send_keys("qq296769530")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("199109xx")
driver.find_element_by_xpath('//*[@id="userLogin"]').click()
time.sleep(2)


