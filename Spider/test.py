from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)
#driver.get("https://www.baidu.com")
driver.get("http://hlcrm.hlcm.cn:8881")
print(driver.title)

###########################
usr = "1103291"
pwd = "0625"
url = "http://hlcrm.hlcm.cn:8881"

# 建立一个browser对象
# 定义登陆的网址
# 获取变量

browser = driver.get(url)

# 找到对应的输入框和登陆按钮
browser.find_element_by_id("txtLoginID").send_keys("1103291")
browser.find_element_by_id("txtPassword").send_keys("0625")

# 进行提交-登陆
browser.find_element_by_class_name("btn btn-primary form-control").click()
browser = driver.get(url)
# 填写表单
browser.find_element_by_id("rd_heat_y").send_keys("正常")  # 体温
browser.find_element_by_id("rd_contact_n").send_keys("无")  # 是否与确诊病例有关联
browser.find_element_by_id("rd_Travelbeijinn").send_keys("否")  # 14天内
browser.find_element_by_id("rd_s_no").send_keys("无需隔离")  # 隔离状况
browser.find_element_by_id("Is_BeGeLi").send_keys("否")  # 被隔离
browser.find_element_by_id("ckPromise").send_keys("Y")  # 承诺

# 进行提交-登陆
browser.find_element_by_id("btnSave").click()
print(driver.title)
print("done")
###########################

driver.quit()
