from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup
#browser = webdriver.Chrome(executable_path="C:\Selenium_Driver\chromedriver")
browser = webdriver.Firefox(executable_path="C:\Selenium_Driver\geckodriver")
browser.get("https://weather.com/pt-BR/clima/10dias/l/BRMG0645:1:BR")

lista = ["Lencois Paulista","Bauru"]

for i in lista:
    
    print(i)
    field_input = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[8]/div[2]/div/div/div/div[1]/div/div[1]/div/input")
    field_input.send_keys(i)

    time.sleep(2)

    search = BeautifulSoup(browser.page_source, 'html.parser')
    list_find = search.find("div", {'class':'styles__inner__3moHD'})
    search_url = list_find.find("ul").find_all("li")

#    print(search_url[0].find('a')['href'])

    link = 'https://weather.com/' + search_url[0].find('a')['href']

    browser.get(link)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    table = soup.find('table', attrs={'class':'twc-table'})

    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    
    for row in rows:
        dia_sem = row.find(class_="date-time").get_text()
        dia = row.find(class_="day-detail clearfix").get_text()
        descricao = row.find(class_="description").get_text()
        temp = row.find(class_="temp").get_text()
        precip = row.find(class_="precip").get_text()
        wind = row.find(class_="wind").get_text()
        humidity = row.find(class_="humidity").get_text()
        print(dia_sem,dia, descricao,temp,precip, wind, humidity)
