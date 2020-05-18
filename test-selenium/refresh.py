from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
print("刷新页面")
driver.refresh()
driver.quit()