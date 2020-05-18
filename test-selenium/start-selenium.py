from selenium import webdriver
driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
'''
print("设置浏览器宽480、高800显示")
driver.set_window_size(480,800)
driver.quit()
'''
#浏览器全屏模式
driver.maximize_window()
#访问百度首页
first_url = 'http://www.baidu.com'
print('now access %s'%(first_url))
driver.get(first_url)

#访问新闻页
second_url='http://news.baidu.com'
print("now access %s"%(second_url))
driver.get(second_url)

#返回（后退）到百度首页
print('back to %s'%(first_url))
driver.back()

#前进到新闻页
print('foward to %s'%(second_url))
driver.forward()

driver.quit()