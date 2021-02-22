from selenium import webdriver
from time import sleep
from tkinter import *
import tkinter.messagebox
from PIL import Image,ImageTk
from pynput.keyboard import *


k=Controller()
username=int(input('Enter your registered phone number'))


url=input('Enter the product link\n')

headline=input('Enter the headlinee\n')

review1=input('Enter your review\n')


Rname=''
AbsName=''

d=webdriver.Chrome("/Users/PrakashC/Desktop/chromedriver")

d.get(url)
sleep(3)
name=d.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div[5]/div[4]/div[1]/div/h1/span').text

for i in name:
    if(i!=' '):
        AbsName=AbsName+i

d.find_element_by_xpath('/html/body/div[2]/header/div/div[1]/div[2]/div/a[2]').click()
sleep(3)
d.find_element_by_id('ap_email').send_keys(username)
d.find_element_by_class_name('a-button-inner').click()
sleep(3)
d.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div[3]/form/span/span/input').click()
sleep(15)

d.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[1]/form/div[4]/span/span/input').click()

sleep(3)
d.find_element_by_partial_link_text('Write a product review').click()
sleep(3)
d.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/button[5]/img').click()
sleep(3)
d.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/form/div[5]/div[2]/div/div/input').send_keys(headline)
sleep(3)
d.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/form/div[6]/div[2]/div/div/div/textarea').send_keys(review1)
sleep(3)
#press submit
d.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[3]/div[1]/input').send_keys('seller feedback')
k.press(Key.enter)
k.release(Key.enter)
sleep(5)
d.find_element_by_link_text("Leave Seller feedback").click()


for i in range(2,7):
    a=d.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div/div/div['+str(i)+']/form/div[1]/div/div/div/div[2]/div[2]/div[2]/ul/li[1]/span/h4/a').text
    for v in a:
        if(v!=' '):
           Rname=Rname+v


    if(AbsName==name):
      print('abd')

else:
    d.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div/div/div[7]/ul/li[5]/a').click()


















"""
d.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/form/div[7]/span/span/button').click()
#create gui
g = Tk()

urls=""
review=""


g.title('Amazon-Ekaro')
g.geometry('1300x500')
l1 = Label(g, text="Enter the product link below", relief="solid",
           font=("arial", 20, "italic"), width=30).place(x=100,y=200)
e1 = Entry(g, textvar=urls, font=("arial", 16, "italic"), width=50)
e1.place(x=600, y=200)

l2 = Label(g, text="Enter the review", relief="solid",
           font=("arial", 20, "italic"), width=30).place(x=100,y=300)
e2 = Entry(g, textvar=review, font=("arial", 16, "italic"), width=50)
e2.place(x=600, y=300)

bSubmit = Button(g, text='Submit', font=("arial", 16, "italic"), width=10, command = lambda :submit(urls,review))
bSubmit.place(x=600, y=400)
g.mainloop()

"""

"""
    
    Sanitizer:While everyone is is in panic to whether buy online or not.
Well I was in need of a sanitizer with perfect quality and pricing as in the market they have tiny bottles with such little quantity and damn expensive.
This one seems to be the perfect choice. Was so nicely packed that one could ensure hygiene and in a perfect condition.
A new bottle arrived on time .
I really like the smeel.of the sanitizer to definitely a reliable product.

 
"""#sample Reviews


