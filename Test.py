#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time as t

driver=webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(30)

driver.get('http://www.baidu.com')
print u'当前URL为:',driver.current_url
t.sleep(3)

element=driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(element).perform()
t.sleep(3)

driver.find_element_by_css_selector(".setpref").click()

select=Select(driver.find_element_by_id('nr'))
select.select_by_visible_text(u'每页显示50条')

element=driver.find_element_by_id('kw')
print element.size
print element.tag_name

element.send_keys('selenium')
t.sleep(3)
element.clear()



driver.get('http://www.yahoo.co.jp')
print u'当前URL为:',driver.current_url

driver.back()
print u'当前URL为:',driver.current_url

driver.forward()
print u'当前URL为:',driver.current_url

driver.quit()
