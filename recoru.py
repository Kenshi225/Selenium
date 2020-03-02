import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

# 操作するブラウザを開く
driver = webdriver.Chrome()
driver.get('https://www.google.com/')

# 操作するページを開く
driver.get('https://app.recoru.in/ap/')
wait = 1
time.sleep(wait)

# RecoRuにログイン
driver.find_element_by_id('contractId').send_keys("id")
driver.find_element_by_id('authId').send_keys("address")
driver.find_element_by_id('password').send_keys("password")
driver.find_element_by_class_name('ow').click()
time.sleep(wait)
# 勤務表画面へ遷移
driver.find_element_by_id('m1').click()
time.sleep(wait)
# 前月へ
driver.find_element_by_xpath("//*[@id='PM']/div[2]/a[1]").click()
time.sleep(wait)
# 日数分だけ繰り返し勤怠入力
table = driver.find_elements_by_xpath("//*[@class='item-day']")
tr_count = len(table) + 1
for i in range(1, tr_count) :
    # 平日のみ処理実行
    week = driver.find_element_by_xpath("//*[@id='attendanceChartForm']/table/tbody/tr["+str(i)+"]/td[1]/a[1]/label").text[-2:-1]
    if week == '土' or week == '日' :
        i += 1
    else :
        element = driver.find_element_by_xpath("//*[@id='attendanceChartForm']/table/tbody/tr["+str(i)+"]/td[2]/select[1]")
        select_element = Select(element)
        select_element.select_by_value('1')
        driver.find_element_by_xpath("//*[@id='attendanceChartForm']/table/tbody/tr["+str(i)+"]/td[3]/input[1]").send_keys("8:50")
        driver.find_element_by_xpath("//*[@id='attendanceChartForm']/table/tbody/tr["+str(i)+"]/td[4]/input[1]").send_keys("18:00")
        txt = driver.find_element_by_xpath("//*[@id='attendanceChartForm']/table/tbody/tr["+str(i)+"]/td[5]/a/img").get_attribute('onclick')
        driver.execute_script(txt)
        time.sleep(wait)
        driver.find_element_by_xpath("//*[@id='SCROLL-BREAKTIME']/table[2]/tbody/tr[1]/td[1]/input[1]").send_keys("12:00")
        driver.find_element_by_xpath("//*[@id='SCROLL-BREAKTIME']/table[2]/tbody/tr[1]/td[3]/input[1]").send_keys("13:00", Keys.TAB, Keys.ENTER)
        time.sleep(wait)
        Alert(driver).accept()
        time.sleep(wait)
        i += 1

# ウィンドウを閉じる
#time.sleep(wait)
#driver.quit()
