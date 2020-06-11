from selenium import webdriver
import time
# 打开浏览器，driver浏览器的实例化句柄
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("http://superf.xyz:8080/ljindex/index.html")

driver.find_element_by_xpath('//*[@id="unlogin"]/div[2]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="username"]').send_keys("e296769530")
driver.find_element_by_xpath('//*[@id="phonenum"]').send_keys("18952991115")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456aaa")
driver.find_element_by_xpath('//*[@id="confirpw"]').send_keys("123456aaa")
driver.find_element_by_xpath('//*[@id="emailnum"]').send_keys("aae@163.com")

driver.find_element_by_xpath('//*[@id="userRegist"]').click()
time.sleep(2)

alert = driver.switch_to_alert()
assert alert.text == "注册成功，请到个人中心设置密保问题，如不填写，你可能无法找回密码！"
driver.quit()