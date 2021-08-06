from selenium import webdriver
import time
browser=webdriver.Firefox()
browser.get('https://www.walmart.com/ip/Clorox-Disinfecting-Wipes-225-Count-Value-Pack-Crisp-Lemon-and-Fresh-Scent-3-Pack-75-Count-Each/14898365')

path=browser.find_element_by_css_selector('.ReviewsHeader-heading > h2:nth-child(1)')
browser.execute_script('arguments[0].scrollIntoView()',path)
time.sleep(5)


path=browser.find_element_by_link_text('See all reviews')
path.click()
time.sleep(10)

path=browser.find_element_by_css_selector('select.field-input:nth-child(3) > option:nth-child(3)')
path.click()

time.sleep(10)


dat=[]
text=[]
rating=[]
name=[]
a=0
flag=True
while flag==True:
    hello=browser.find_elements_by_class_name("review")
    for i in hello:
        date=i.find_elements_by_class_name('review-date-submissionTime')
        title=i.find_elements_by_class_name('review-heading')
        descript=i.find_elements_by_class_name('review-text')
        ti=i.find_elements_by_class_name('review-star-rating')
        hell=i.find_elements_by_class_name('review-footer-userNickname')
        if date[0].text=='December 31, 2020':
            flag=False
            break
        dat.append(date[0].text)
        text.append(descript[0].text)
        rating.append(ti[0].text)
        name.append(hell[0].text)


    time.sleep(5)
    if a<1:
        path=browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[2]/div/div/button')
        path.click()
    else:
        path=browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[6]/div[2]/div/div/button[2]')
        path.click()
    time.sleep(5)
    print('page is done')
    a += 1

ratings=[]
for i in (rating):
    rate=i[18:21]
    ratings.append(rate)



import pandas as pd
dic={'date':dat,'desc':text,'rate':ratings,'names':name}
df=pd.DataFrame(dic)
df.to_csv('output.csv')



print(dat)
print(ratings)
print(text)
print(name)


print(len(dat))
print(len(ratings))
print(len(text))
print(len(name))
