from selenium import webdriver
from time import sleep
from pynput.keyboard import *

url='https://www.youtube.com/'

k=Controller()
search=input('Enter the song name\n')

driver =  webdriver.Chrome("/Users/PrakashC/Desktop/chromedriver")

driver.get(url)
driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input').send_keys(search+' song')
driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button').click()
sleep(10)
a=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a').get_attribute('href')
driver.get('https://ytmp3.cc/en13/')
sleep(10)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/form/input[1]').send_keys(a)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/form/input[2]').click()
sleep(5)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[1]').click()

