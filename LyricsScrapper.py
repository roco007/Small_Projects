from selenium import webdriver
from time import sleep
from pynput.keyboard import *

url='https://www.google.com/'
k=Controller()
search=input('Enter the song name\n')

driver =  webdriver.Chrome("/Users/PrakashC/Desktop/chromedriver")

driver.get(url)
driver.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(search+' song lyrics')
k.press(Key.enter)
k.release(Key.enter)
f=open('C:/Users/PrakashC/Desktop/SongLyrics007/'+search+'.txt','wt',encoding="utf-8")
try:
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div').click()

except Exception:
    pass


lyr=driver.find_elements_by_tag_name('span')

for l in lyr:
    if(l.get_attribute('jsname')=='YS01Ge'):
        f.write(l.text+'\n')
f.close()
