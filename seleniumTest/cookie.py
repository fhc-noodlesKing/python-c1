from selenium import webdriver
import time

def get_page(url):
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.maximize_window()
    driver.get(url)
    cookie = {'domain': '132.232.44.158', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'dq7ld0oqsg6c5kk239llpeosv7'}
    driver.add_cookie(cookie)
    driver.refresh()
    return driver

driver = get_page("http://132.232.44.158:9999/shopxo/")


# driver = webdriver.Chrome(executable_path='chromedriver.exe')
# driver.get("http://132.232.44.158:9999/shopxo/")

# cookie = {'domain': '132.232.44.158', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'dq7ld0oqsg6c5kk239llpeosv7'}
# driver.add_cookie(cookie)


# driver.refresh()


