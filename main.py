# coding=utf-8
from bs4 import BeautifulSoup
import requests
import csv
import time
import lxml
from urllib import request

url = "https://qd.58.com/pinpaigongyu/?minprice=600_1000"
page = 0
csv_file = open("rent.csv", 'w', encoding='utf-8')
csv_writer = csv.writer(csv_file, delimiter=',')  # 写入
while True:
    page += 1
    print("fetch : ", url.format(page=page))
    time.sleep(1)
    response = requests.get(url.format(page=page))  # 抓取
    response.encoding = 'utf-8'  # 设置解码方式
    html = BeautifulSoup(response.text, features='lxml')  # 传入超文本并且声明解析器
    house_list = html.select(".list > li")
    if not house_list:
        break
    for house in house_list:
        house_title = house.select("h2")[0].string
        house_url = house.select("a")[0]["href"]
        house_info_list = house_title.split()
        if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
            house_location = house_info_list[0]
        else:
            house_location = house_info_list[1]
        house_money = house.select(".money")[0].select("b")[0].string
        csv_writer.writerow([house_title, house_location, house_money, house_url])
csv_file.close()