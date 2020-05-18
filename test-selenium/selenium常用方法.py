from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

'''
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
'''

'''
search_text = driver.find_element_by_id("kw")
search_text.send_keys('selenium')
search_text.submit()
sleep(5)
'''

#获得输入框尺寸
size = driver.find_element_by_id("kw").size
print(size)


#返回百度页面底部备案信息
text = driver.find_element_by_id("s-bottom-layer-right").text
print(text)


#返回元素的属性值，可以是id、name、type或其他任意属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
print(attribute)

#返回元素的结果是否可见，返回结果为true或者false
result = driver.find_element_by_id("kw").is_displayed()
print(result)

driver.quit()