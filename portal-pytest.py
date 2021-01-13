from selenium import webdriver
import time
import allure
import pytest
import os
@allure.feature("登录")
def test_denglu():
    driver = webdriver.Chrome()
    driver.get("https://angelapi.bluemoon.com.cn/portal-admin/login.html")
    driver.find_element_by_id("username").send_keys("80474765")
    time.sleep(3)
    driver.find_element_by_id("password").send_keys("qq123123")
    time.sleep(3)
    driver.find_element_by_id("rand").send_keys("8888")
    driver.find_element_by_id("onLogin").click()
    time.sleep(10)
    assert driver.title == "蓝月亮-门户网站"
    print("success")
    driver.quit()
#
if __name__=='__main__':
    pytest.main(['-s', '-q','--alluredir','../result', 'portal-pytest.py'])
    os.system('allure generate  -c ../result/  -o ../report/ --clean')
#     #/home/appadm/result