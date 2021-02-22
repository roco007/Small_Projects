from selenium import webdriver
from time import sleep
from pynput.keyboard import *

url='https://www.instagram.com/'

links=[]

k=Controller()


d =  webdriver.Chrome("/Users/PrakashC/Desktop/chromedriver")
d.get(url+'nunescalvin/')
sleep(5)


a=d.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[1]/a').text

no=a[0:len(a)-6]

