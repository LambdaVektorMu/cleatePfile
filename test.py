#!/Users/vektormac/work/3.8venv/bin/python
# coding: utf-8

from pprint import pprint
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

driver_path = '/Users/vektormac/work/chromedriver'
options = Options()
options.add_argument('--incognito')
driver = webdriver.Chrome(executable_path=driver_path, options=options)

url = 'https://www.foodpanda.co.jp/restaurant/l0pj/sutekikare-gurirurou-zhu'
driver.get(url)
sleep(2)

# 最初のポップアップを閉じる
buttons = driver.find_elements_by_tag_name('button')
for b in buttons:
    if b.get_attribute('aria-label') == 'close':
        b.click()
        break
sleep(2)

# レストラン情報を表示する
svgs = driver.find_elements_by_tag_name('svg')
for s in svgs:
    if s.get_attribute('class') == 'fl-brand-primary':
        s.click()
        break
sleep(2)

# レストランの住所を取得する
p_tags = driver.find_elements_by_tag_name('p')
for p in p_tags:
    print(p.get_attribute('class'))
    if p.get_attribute('class') == 'cl-neutral-secondary f-14 fw-light lh-regular':
        print(p.text)
        break

# 口コミ点数情報を表示する
buttons = driver.find_elements_by_tag_name('button')
for b in buttons:
    if b.get_attribute('data-title') == '口コミ':
        b.click()
        break
sleep(2)

# 口コミ点数を取得する
h2_tags = driver.find_elements_by_tag_name('h2')
for h2 in h2_tags:
    print(h2.get_attribute('class'))
    if h2.get_attribute('class') == 'f-18 fw-light mb-sm':
        print(h2.text)
        break

sleep(3)
driver.quit()
