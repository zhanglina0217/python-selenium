from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print("Before search=============")

#打印当前页面title
title = driver.title
print("title:"+title)

#打印当前页面URL
now_url = driver.current_url
print('URL:'+now_url)

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)

print('After search=============')

#再次打印当前页面title
title = driver.title
print('title:'+title)

#再次打印当前页面url
now_url = driver.current_url
print('URL:'+now_url)

#获取搜索结果条数
num = driver.find_element_by_class_name('nums').text
print('result:'+num)

driver.quit()