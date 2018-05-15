#***************************************************
#              Author='swaraj singh'               *                            
#              Date=15/05/2018                     *                           
#              Time=9:35 AM                        *
#***************************************************

import os
from selenium import webdriver #import selenium.webdriver
from bs4 import BeautifulSoup
import time

print "Note : Prefix your URL with 'http' or 'https://' ..."
url = str(raw_input("Enter a Website Url :"))
driver = webdriver.PhantomJS()
driver.set_window_size(1600, 900)
print "Opening The Url ..."
driver.get(url)

print '*'*77
print "[*] Url loaded - " + url
print '*'*77

action = []
form_name = []
inpu = []
change = 0
html = driver.page_source
soup = BeautifulSoup(html,'lxml')

def get_num_forms():
    q=0
    forms=driver.find_elements_by_tag_name('form')
    for form in forms:
        q+=1
    print "[1.] Number of Forms Found :{}".format(q)

'''def getting_forms():
    q=0
    forms=driver.find_elements_by_tag_name('form')
    for form in forms:
        q+=1
        action.append(form.get_attribute('action'))
        form_name.append(form.get_attribute('name'))
        print ('[{}]').format(q),'.',action[q-1],"-->",form_name[q-1]
    ins = str(raw_input("Enter Your Input :"))
    request_form(ins)'''
    
def request_form():
    q = 0
    b = 0
    z = 0
    #action = []
    #form_name = []
    success = 0
    input_name = []
    input_id = []
    button_name = []
    button_click = []
    sq = 0
    print 1
    forms = driver.find_elements_by_tag_name('form')
    for form in forms:
        q+=1
        action.append(form.get_attribute('action'))
        form_name.append(form.get_attribute('name'))
        change = 1
        print ('[{}]').format(q),'.',action[q-1],"-->",form_name[q-1]
    var = str(raw_input("Enter Your Input :"))
    q=0
    for form in forms:
        q=q+1
        if var==str(q):
            success=1
            print "You Have Requested for {} Name :{}".format(action[q-1],form_name[q-1])
            insi = form.find_elements_by_tag_name('input')
            for t in insi:
                if t.get_attribute('type')!='button':
                    if t.get_attribute('type')!='hidden' and t.get_attribute('type')!='submit':
                        b=b+1
                        input_name.append(t.get_attribute('name'))
                        input_id.append(t.get_attribute('id'))
                        print "Enter Input for :",input_name[b-1],":"
                        v=raw_input()
                        t.send_keys(v)
                if t.get_attribute('type')=='submit':
                    button_name.append(t.get_attribute('name'))
                    button_click.append(t)
            butto = form.find_elements_by_tag_name('button')
            for sw in butto:
                button_name.append(sw.get_attribute('name'))
                button_click.append(sw)
            for bn in button_name:
                z=z+1
                y='y'
                print ("[{}] Enter 'y' to Submit :{}").format(z,button_name[z-1])
                click=str(input(""))
                if click=='y':
                    button_click[z-1].click()
                    time.sleep(5)
                    html=driver.page_source
                    #print html
                    soup = BeautifulSoup(html, "lxml")
                    driver.save_screenshot("swarajsingh.png")
                    titles=soup.find('title')
                    print titles
                else:
                    print "Sorry Try Again Later ..."
                    #for hj in titles:        
                break
        #if success!=1:
            #print "You Have not Entered Desried Input Kindly Check your Input.\nPlease Try Again Later ..."

if change == 1:
    action = []
    form_name = []
    change = 0
            
def get_num_images():
    q=0
    imgs = driver.find_elements_by_tag_name('img')
    for img in imgs:
        q=q+1
    print "[2.]Number of Images Loaded: {}".format(q)
    
def get_detail_img():
    q=0
    src = []
    img_name = []
    imgs = driver.find_elements_by_tag_name('img')
    for img in imgs:
        q=q+1
        src.append(img.get_attribute('src'))
        img_name.append((img.get_attribute('name')))
        print q,'.',src[q-1],"-->",img_name[-1]

def get_all_links():
    q=0
    links = []
    linki=driver.find_elements_by_tag_name('a')
    for l in linki:
        q=q+1
        links.append((l.get_attribute('href')))
    print "[*]Total No. of links Found: ",q
    q=0
    for wrt in links:
        q+=1
        print "[{}] {}".format(q,wrt)    
    it = int(raw_input("[*] Enter the link number to open it :"))
    q=0
    for g in links:
        q+=1
        if it==q:
            driver.get(g[q-1])
            
def choices():
    y='y'
    n='n'
    while(y=='y' or y=='Y'):
        
    	get_num_forms();
    	get_num_images();
    	print "[3.] GetallLinks within the Page"
    	print "[4.] Take ScreenShot"
        print "[5.] Clear The Screen ..."

    	print '*'*44
    	ins=int(input("Enter Your Input what you want to do: "))
    	if ins==1:
        	request_form() 
    	elif ins==2:
        	get_detail_img()
    	elif ins==3:
        	get_all_links()
    	elif ins==4:
        	print "Taking ScreenShot ..."
        	driver.save_screenshot("swarajsingh.png")
        elif ins==5:
            os.system('cls')
    	else:
        	print "error"
        y=str(input("Is you want to do more :"))
        if y=='n':
            break
            
        action = []
        form_name = []
        src = []
        img_name = []
        links = []
        inpu = []

choices();
    
driver.quit()             
