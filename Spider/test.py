from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# print(driver.title)
#
# driver.quit()

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chromedriver = "/usr/bin/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromedriver)
usr = "1103291"
pwd = "0625"
url = "http://hlcrm.hlmc.cn:8881/Login"
# driver.get(url)
# print(driver.title)

###########################
# 建立一个browser对象
# 定义登陆的网址
# 获取变量

driver.get(url)
print(driver.title)

# 找到对应的输入框和登陆按钮
driver.find_element(By.ID,"txtLoginID").send_keys("1103291")
driver.find_element(By.ID,"txtPassword").send_keys("0625")

# 进行提交-登陆
driver.find_element(By.CSS_SELECTOR,"button").click()
print(driver)
time.sleep(5)
#
driver.switch_to.window(driver.window_handles[0])

# 填写表单
driver.find_element(By.XPATH,"//*[@id='rd_heat_y']").click() # 体温
time.sleep(1)
driver.find_element(By.ID,"rd_contact_n").click()  # 是否与确诊病例有关联
time.sleep(1)
driver.find_element(By.ID,"rd_Travelbeijinn").click()  # 14天内途径高风险地区
time.sleep(1)
driver.find_element(By.ID,"rd_TravelOutFn").click()  # 14天内境外旅居史
time.sleep(1)
driver.find_element(By.ID,"rd_s_no").click() # 隔离状况 "无需隔离"
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='fm']/div[30]/input[2]").click() # 被隔离
time.sleep(1)
driver.find_element(By.ID,"ckPromise").click()  # 承诺
time.sleep(1)

# 进行提交-登陆
driver.find_element(By.ID,"btnSave").click()
print(driver.title)
print("done")
###########################
time.sleep(5)
driver.quit()

#
# if __name__ == '__main__':
#     ClockIn()
