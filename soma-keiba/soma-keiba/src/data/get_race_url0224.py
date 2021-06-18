import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

import shutil
import os

options = Options()
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver,10)



URL = "https://db.netkeiba.com/?pid=race_search_detail"
driver.get(URL)
time.sleep(1)
wait.until(EC.presence_of_all_elements_located)

# 検索オプション(競争種別:芝、期間:2015年1月~現在、馬場:中山、距離:2000m以上)


# 芝を選択
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/form/table/tbody/tr[2]/td/input[1]").click()

# 期間を選択
year = 2015
month = 1

start_year_element = driver.find_element_by_name('start_year')
start_year_select = Select(start_year_element)
start_year_select.select_by_value(str(year))
start_mon_element = driver.find_element_by_name('start_mon')
start_mon_select = Select(start_mon_element)
start_mon_select.select_by_value(str(month))
# end_year_element = driver.find_element_by_name('end_year')
# end_year_select = Select(end_year_element)
# end_year_select.select_by_value(str(year))
# end_mon_element = driver.find_element_by_name('end_mon')
# end_mon_select = Select(end_mon_element)
# end_mon_select.select_by_value(str(month))

# 中央競馬場をチェック
# for i in range(1,11):
#     terms = driver.find_element_by_id("check_Jyo_"+ str(i).zfill(2))
#     terms.click()


# 中山競馬場をチェック
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/form/table/tbody/tr[4]/td/input[6]").click()

# レース距離を2000m以上に
distance = 2000

texts = driver.find_element_by_name("kyori_min")
texts.send_keys(distance)

# 表示件数を選択(20,50,100の中から最大の100へ)
list_element = driver.find_element_by_name('list')
list_select = Select(list_element)
list_select.select_by_value("100")

# フォームを送信
# time.sleep(100)
frm = driver.find_element_by_css_selector("#db_search_detail_form > form")
frm.submit()
time.sleep(5)
wait.until(EC.presence_of_all_elements_located)



with open(str(year)+"-"+str(month)+".txt", mode='w') as f:
    while True:
        time.sleep(5)
        wait.until(EC.presence_of_all_elements_located)
        all_rows = driver.find_element_by_class_name('race_table_01').find_elements_by_tag_name("tr")
        for row in range(1, len(all_rows)):
            race_href=all_rows[row].find_elements_by_tag_name("td")[4].find_element_by_tag_name("a").get_attribute("href")
            f.write(race_href+"\n")
        try:
            target = driver.find_elements_by_link_text("次")[0]
            driver.execute_script("arguments[0].click();", target) #javascriptでクリック処理
        except IndexError:
            break


shutil.move('./2015-1.txt', './urls/')
