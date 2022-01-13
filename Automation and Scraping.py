from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec

driver=webdriver.Firefox()
#automate google search to search for the cats image
def automation():
    driver.get('https:/www.google.com/')
    search=WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.CSS_SELECTOR,'.gLFyf')))
    search.send_keys('cats')
    click_ele=driver.find_element_by_css_selector('.FPdoLc > center:nth-child(1) > input:nth-child(1)')
    click_ele.click()
    image=driver.find_element_by_css_selector('div.hdtb-mitem:nth-child(2) > a:nth-child(1)')
    image.click()

#scraping the images and storing it to the specified path
def scraping():
    automation()
    path='/home/himanshu/Desktop/downloaded_image/'#write your directory to save the image
    for j in range(1,50):
        try:
            img = driver.find_element_by_xpath(f'/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{str(j)}]/a[1]/div[1]/img')
            img.screenshot(path + str(j) +'.png')
        except:
            continue



scraping()