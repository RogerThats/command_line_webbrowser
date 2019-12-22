import os
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#binary = FirefoxBinary('/media/root/F2CC8EAFCC8E6E23/firefox-68.0.1/firefox/firefox')
binary = FirefoxBinary('/usr/lib/firefox-esr/firefox-esr')

old = False

class MyBrowser:
    def __init__(self):
        self.old = False
        options = Options()
        options.add_argument('-headless')
        #fp = webdriver.FirefoxProfile()
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        self.driver = webdriver.Firefox(firefox_binary=binary, capabilities=cap, options=options)
        self.driver.set_window_size(1600, 900)
    
    def openUrl(self, url):
        self.url = url
        print("Openning Url ...")
        self.driver.get(self.url)
        print('*'*77)
        print("[*] Url Loaded - " + self.url)
        print('*'*77)
        self.action = []
        self.form_name = []
        self.inpu = []
        self.change = 0
        self.html = self.driver.page_source
        self.soup = BeautifulSoup(self.html, 'lxml')
        self.forms = self.driver.find_elements_by_tag_name('form')
        
    def onChange(self):
        self.html = self.driver.page_source
        self.soup = BeautifulSoup(self.html, 'lxml')
        self.forms = self.driver.find_elements_by_tag_name('form')
        self.action = []
        self.form_name = []
        self.inpu = []
        self.change = False
    
    def getNumForms(self):
        count = 0
        for form in self.forms:
            count += 1
        return count
    
    def changes(self):
        self.action = []
        self.form_name = []
        self.change = False
        
    def getNumImages(self):
        q = 0
        imgs = self.driver.find_elements_by_tag_name('img')
        for img in imgs:
            q += 1
        return q
    
    def getDetailImg(self):
        q = 0
        self.src = []
        self.img_name = []
        imgs = self.driver.find_elements_by_tag_name('img')
        for img in imgs:
            q += 1
            self.src.append(img.get_attribute('src'))
            self.img_name.append((img.get_attribute('name')))
            print(q, '.', self.src[q-1], "-->", self.img_name[q-1])
    
    def getAllLinks(self):
        q = 0
        self.links = []
        linki = self.driver.find_elements_by_tag_name('a')
        for l in linki:
            q += 1
            self.links.append(l.get_attribute('href'))
        print("[*] Total Number of Links Found : ", q)
        q = 0
        for wrt in self.links:
            q += 1
            print("[{}] {}".format(q, wrt))
        it = int(input("[*] Enter the link Number to Open it : "))
        q = 0
        for g in self.links:
            q += 1
            if it == q:
                self.openUrl(self.links[q-1])
                self.old = True
                self.onChange()
    
    def userChoices(self):
        user_input = 'y'
        while 'y' in user_input or 'Y' in user_input:
            if self.old == False:
                print("Note : Prefix Url with http:// or https://")
                url = str(input("Enter Url : "))
                self.openUrl(url)
                self.old = True
            
            print("[1.] Number of Forms Found :{}".format(self.getNumForms()))
            print("[2.] Number of Images Found :{}".format(self.getNumImages()))
            print("[3.] Get All Links Within the Page")
            print("[4.] Take ScreenShot")
            print("[5.] Clear the Screen")
            print("[6.] Open a Url")
            
            print('*'*44)
            ins = int(input("Enter Your Input( Above List) : "))
            if ins == 1:
                self.requestForm()
            elif ins == 2:
                self.getDetailImg()
            elif ins == 3:
                self.getAllLinks()
            elif ins == 4:
                print("Taking Screen Shot ...")
                self.driver.save_screenshot("swarajsingh.png")
            elif ins == 5:
                os.system('cls')
            elif ins == 6:
                print("Note : Prefix Url with http:// or https://")
                url = str(input("Enter Url : "))
                self.openUrl(url)
                self.old = True
            user_input = str(input("Is You Want to Do More : "))
            if 'n' in user_input or 'N' in user_input:
                break
            
            self.action = []
            self.form_name = []
            self.src = []
            self.img_name = []
            self.links = []
            self.inpu = []
            
    
    def requestForm(self):
        q = 0
        b = 0
        z = 0
        success = False
        input_name = []
        input_id = []
        button_name = []
        button_click = []
        sq = 0
        #print(self.forms)
        for form in self.forms:
            q += 1
            self.action.append(form.get_attribute('action'))
            self.form_name.append(form.get_attribute('name'))
            change = True
            print('[{}]'.format(q),'.',self.action[q-1],"-->",self.form_name[q-1])
        var = int(input("Enter Your Input : "))
        q = 0
        for form in self.forms:
            q += 1
            if var == q:
                success = True
                print("You Had Requested For {} Name : {}".format(self.action[q-1], self.form_name[q-1]))
                insi = form.find_elements_by_tag_name('input')
                for t in insi:
                    if t.get_attribute('type') != 'button':
                        if t.get_attribute('type') != 'hidden' and t.get_attribute('type') != 'submit':
                            b += 1
                            input_name.append(t.get_attribute('name'))
                            input_id.append(t.get_attribute('id'))
                            print("Enter Input for : ", input_name[b-1], ":")
                            user_input = input()
                            t.send_keys(user_input)
                        if t.get_attribute('type') == 'submit':
                            button_name.append(t.get_attribute('name'))
                            button_click.append(t)
                butto = form.find_elements_by_tag_name('button')
                for sw in butto:
                    button_name.append(sw.get_attribute('name'))
                    button_click.append(sw)
                for bn in button_name :
                    z += 1
                    print("[{}] Enter 'y' to Submit : {}".format(z, button_name[z-1]))
                    click = str(input(""))
                    if click == 'y':
                        button_click[z-1].click()
                        time.sleep(5)
                        self.onChange()
                        self.driver.save_screenshot("swarajsingh.png")
                        titles = self.soup.find('title')
                        print(titles)
                    else:
                        print("Sorry Try Again Later ...")
                    break
                    
                    
browse = MyBrowser()
browse.userChoices()
browse.driver.quit()
