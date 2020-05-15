from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver import ActionChains
import xlwt
import xlrd
import openpyxl
browser = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
import re
path="C:/Users/admin/PycharmProjects/untitled2/test.xlsx"
col_name="品牌"
df=pd.read_excel(path)
name=df[col_name]
n=df.shape[0]
df['可疑度'] = 0
for idx, key_word in name.items():
    browser.get('http://www.baidu.com')
    assert "百度" in browser.title
    search_text_blank = browser.find_element_by_id("kw")
    search_text_blank.send_keys(key_word )
    search_text_blank.send_keys(Keys.ENTER)
    time.sleep(1)
    page = browser.page_source
    num = len(re.findall(r'加盟',page))
    df['可疑度'].loc[idx] = num
    d =  {'品牌':key_word,'可疑度':num}
    #pd.DataFrame(d,index=[0])
    df.to_excel('excel_output.xls', sheet_name='biubiu')
    #print (d)