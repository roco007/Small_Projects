from selenium import webdriver
from time import sleep
from pynput.keyboard import *
from pynput.mouse import *
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.options import Options


chOpt=Options()
chOpt.add_experimental_option('pref',{'download.default_directory': 'C:\Desktop'})# download to desired location

url='https://www.amazon.in/'
k=Controller()
d =  webdriver.Chrome("/Users/PrakashC/Desktop/chromedriver", chrome_options=chOpt) # (chrome_options=chOpt) is for chrome settings
d.get(url)
#print(d.title)  #gives the title of the web page

#d.minimize_window() #minimize the window

#d.fullscreen_window()# fullscreen mode

#d.maximize_window()#maximize the window

#print(d.current_url) #returns url of current webpage

#print(d.page_source)#returns html data


#d.close()#closes the tab which was auto-generated tab

#d.quit()# closes all tabs

"""
             <Navigation Commands>

d.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input').send_keys('Arijit singh')

k.press(Key.enter)
k.release(Key.enter)
sleep(2)
d.back()# goes to previous webpage
sleep(2)
d.forward()# goes to next webpage
sleep(2)
d.refresh()# refreshes the current webpage

"""  # navigation commands

"""
        <Conditional Commands>

a=d.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div[1]/div[3]/center/input[1]')# 'Google search' button

#print(a.is_displayed()) # returns true if it is displayed

#print(a.is_enabled())   # returns true if it is enabled

#a.is_selected()        # is used while working with radio buttons and returns true if the button is selected

"""  # conditional commands


"""

                     <----------LINKS----------->


links=d.find_elements_by_tag_name('a')# it will return all the elements with the specified tag

for i in links:
    print(i.text +" - "+i.get_attribute('href'))# '.text' will return the text present in the tag and '.get_attribute( 'attribute' )' will return value of specified attribute

print(len(links))

d.find_element_by_link_text('Register').click() # this will find the element by the text within the specified tag and .click() will click on that link element  

"""  # Link commands


"""


                         <----Working with Alerts---->

d.switch_to_alert().dismiss()
d.switch_to_alert().accept()
"""  # Alert commands

"""

           <------Working with frames--------->
#d.switch_to_frame('')..here we can use name or id as identifier

d.switch_to_frame()                # switch from main content to a particular frame to work in that frame

d.switch_to_default_content()      # switch back to main frame

d.switch_to_frame()                # switch to another frame to work in that frame

"""  # Frame commands


"""
            <-----Working with Browser Windows------->

b=d.current_window_handle     # this will give the window_handle of the main page
print(b)
d.find_element_by_xpath('/html/body/div[1]/div[2]/div/main/article/div/div[1]/section/div/div/div[2]/a[1]/span').click()
sleep(5)
a=d.window_handles             #  this will return the list of all the window handle in the order of their activation
print(a[1])
sleep(5)
d.switch_to.window(b)           # this will switch to respective window with handle 'b'
sleep(5)

d.switch_to.window(a[1])        #  'a' has list of all thr window_handles in order that they were activated


"""  # Browser window commands

"""
                                  <-------Working with Table tag------->

    #for website='https://trends.builtwith.com/websitelist/Responsive-Tables'

# len() will return the number of rows present in table tag

rows=len(d.find_elements_by_xpath('/html/body/form/div[2]/div[2]/div/table/tbody/tr'))

columns=len(d.find_elements_by_xpath('/html/body/form/div[2]/div[2]/div/table/tbody/tr[1]/td'))

print(str(rows)+'x'+str(columns))



for r in range(2,rows+1):   # generally row-count should start from 2 as first row is always heading
    for c in range(2,6): # avoid columns with img data
         if(c!=3):

          value = d.find_elements_by_xpath("/html/body/form/div[2]/div[2]/div/table/tbody/tr["+str(r)+"]/td["+str(c)+"]")

          for i in value:
              print(i.text)

"""# Table commands


"""
                <-------Scroll Commands-------->
                

d.execute_script("window.scrollBy(0,700)","")# scrolls downto 700 pixels

f=driver.find.....................
d.execute_script("arguements[0].scrollIntoView();",f)# scrolls downto element 'f'


d.execute_script("window.scrollBy(0,document.body.scrollHeight)") # scrolls till the end

"""# Scroll Commands



"""
# url=amazon.in


sleep(5)



(  nav=d.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/a[2]/span[1]')
 accnt=d.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[4]/div[3]/div[2]/div/div[3]/a[1]/span')
 action.move_to_element(nav).move_to_element(accnt).click().perform()   )  Hover action


(       element=d.find......(.....)
        action.double_click(element).perform()        )Double click


(  element=d.find......(.....)
        action.context_click(element).perform()         
    ) Right click

(      action=ActionChains(d)
#nav=d.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/a[2]/span[1]')
#accnt=d.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[4]/div[3]/div[2]/div/div[3]/a[1]/span')
#action.move_to_element(nav).move_to_element(accnt).click().perform()

src=d.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/a/div[1]/img')
dest=d.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[3]/div[1]/input')
action.drag_and_drop(src,dest).perform() 
        ) Drag and Drop

"""# Mouse actions

"""
d.find_element_by_xpath(".....").send_keys(' address of file ')


"""#uploading files

"""
"""#








