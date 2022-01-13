from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import json
import sqlite3

#creating sqlite connection
connection=sqlite3.connect('city_temp.db')
cursor=connection.cursor()

#to scrap the city name from the github
def scraping():
    driver=webdriver.Firefox()
    driver.get('https://github.com/nshntarora/Indian-Cities-JSON/blob/master/cities.json')
    ele=driver.find_element_by_css_selector('#raw-url')
    ele.click()
    body=driver.find_element_by_xpath('/html/body/pre')
    lis=json.loads(body.text)
    city_name=[]
    for i in range(len(lis)):
        city_name.append(lis[i]['name'])
    return city_name

#scraping and inserting temperature with the city name in sqlite database
def creating_table():
    city_name=scraping()
    cursor.execute('drop table temp')
    cursor.execute('''CREATE TABLE temp(CITY TEXT,TEMPERATURE TEXT)''')
    driver = webdriver.Firefox()
    for j in range(len(city_name)):
        driver.get(f'https://www.google.com/search?channel=fs&client=ubuntu&q={city_name[j]}+temperature')
        ele=driver.find_element_by_id('wob_tm')
        cursor.execute(f'''INSERT INTO temp VALUES('{city_name[j]}','{ele.text}')''')
        connection.commit()


creating_table() #function to run
#to view the table
'''cursor.execute('select * from temp')
result = cursor.fetchall()
print(result)'''
