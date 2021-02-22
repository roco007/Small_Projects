from selenium import webdriver
from time import sleep
from tkinter import *
import tkinter.messagebox
from PIL import Image,ImageTk

username='9673179079'
password='Ilike2$ing'

url1='https://www.amazon.in/ap/signin?_encoding=UTF8&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_youraccount_signout%26signIn%3D1%26useRedirectOnSuccess%3D1/'
url2='https://earnkaro.com/'





def submit():
    print('1')
    global name
    driver = webdriver.Chrome("/Users/PrakashC/Desktop/chromedriver")
    driver.get(url1)
    driver.find_element_by_id('ap_email').send_keys(username)
    driver.find_element_by_class_name('a-button-inner').click()

    driver.find_element_by_id('ap_password').send_keys(password)
    driver.find_element_by_id('signInSubmit').click()
    sleep(5)
    driver.find_element_by_id('twotabsearchtextbox').send_keys('BoroPlus Advanced Anti-Germ Hand Sanitizer, 200ml')
    driver.find_element_by_class_name('nav-input').click()
    lnk=driver.find_element_by_partial_link_text('BoroPlus Advanced Anti-Germ Hand Sanitizer, 200ml').get_attribute("href")

    driver.get(url2)
    driver.find_element_by_id('link_signin').click()
    sleep(3)
    driver.find_element_by_id('uname').send_keys('raj45colaco@gmail.com')
    driver.find_element_by_id('pwd').send_keys(password)
    sleep(3)
    driver.find_element_by_id('btnLayoutSignIn').click()
    sleep(3)
    driver.find_element_by_xpath('/html/body/div[12]/div[1]/div[2]/div[2]/div[1]/div/div[2]/form/div[2]/div[4]/button').click()
    sleep(10)
    driver.find_element_by_id('wzrk-cancel').click()
    sleep(3)
    driver.find_element_by_id('link_makeprofit').click()
    sleep(3)
    driver.find_element_by_xpath('/html/body/div[5]/section/div/section/form/div/div/div/input[1]').send_keys(lnk)
    sleep(3)
    driver.find_element_by_xpath('/html/body/div[5]/section/div/section/form/div/div/button').click()
    prLink=driver.find_elements_by_tag_name('a')
    no=prLink.__len__()
    profit=prLink[no-1].get_attribute("href")
    c='https://ekaro.in/'+profit[67:]

    driver.get(c)




#create gui
g = Tk()

name = ""

g.title('Amazon-Ekaro')
g.geometry('1300x500')
l1 = Label(g, text="Enter the name of the product as of in the Amazon App/Website", relief="solid",
           font=("arial", 26, "italic"), width=300).pack()
e1 = Entry(g, textvar=name, font=("arial", 16, "italic"), width=80)
e1.place(x=200, y=200)

bSubmit = Button(g, text='Submit', font=("arial", 16, "italic"), width=10, command=submit)
bSubmit.place(x=600, y=300)
g.mainloop()









"""
#Method using whatsapp
driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[2]/div[2]/div[1]/div/div[2]/a').click()
sleep(45)
driver.find_element_by_class_name('_2S1VP copyable-text selectable-text').send_keys('9673179079')
driver.find_element_by_class_name('_2EXPL aZ91u').click()
driver.find_element_by_class_name('eTCKi').click()
driver.find_element_by_class_name('weEq5').click()
driver.find_element_by_class_name('_3BCzw').click()
#Get profit link



driver.find_element_by_

#Enter details
#signin
driver.find_element_by_id('ap_email').send_keys(username)
driver.find_element_by_class_name('a-button-inner').click()
#driver.find_element_by_id('ap_password').send_keys(password)
driver.find_element_by_id('auth-login-via-otp-btn').click()
sleep(20)
driver.find_element_by_id('a-autoid-0').click()

link=driver.find_element_by_link_text('').get_attribute()
"""
