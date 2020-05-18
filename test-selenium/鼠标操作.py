from selenium import webdriver

#引入actionchains类
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()

#定位到要悬停的元素
above = driver.find_element_by_id('s-usersetting-top')
#对定位到的元素执行鼠标悬停工作
ActionChains(driver).move_to_element(above).perform()