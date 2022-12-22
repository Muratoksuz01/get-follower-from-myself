import chromedriver_autoinstaller as chromedriver
chromedriver.install()
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
class Integram():
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.browser=webdriver.Chrome()
    def sing_in(self):
        url="https://www.instagram.com/"
        self.browser.get(url)
        sleep(1)
        self.browser.find_element("name","username").send_keys(self.username)
        self.browser.find_element("name","password").send_keys(self.password)
        sleep(1)
        self.browser.find_element("xpath","//*[@id='loginForm']/div/div[3]/button").click()
        sleep(5)
    def get_all_following(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        sleep(4)
        self.browser.find_element(By.CLASS_NAME,"_aacl._aacp._aacu._aacx._aad6._aade").click() #followers butonu
        sleep(3)
        self.scroolDown()
        takipciler=self.browser.find_elements(By.CLASS_NAME,"_ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm") 
        say=1
        for takipci in takipciler:
            name=takipci.find_element(By.CLASS_NAME,"_ab8y._ab94._ab97._ab9f._ab9k._ab9p._abcm")
            takipci_link="https://www.instagram.com/"+name.text
            print(str(say)+"-->"+name.text +"-->"+takipci_link)
            say+=1
    def scroolDown (self):
        jsKomut = """
            sayfa = document.querySelector("._aano");
            sayfa.scrollTo(0, sayfa.scrollHeight);
            var sayfaSonu = sayfa.scrollHeight;
            return sayfaSonu;"""

        sayfaSonu = self.browser.execute_script (jsKomut)
        while True:
            son=sayfaSonu
            sleep(1)
            sayfaSonu=self.browser.execute_script(jsKomut)
            if son==sayfaSonu:
                break
    def get_followers_with_number(self,number):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        sleep(4)
        self.browser.find_element(By.CLASS_NAME,"_aacl._aacp._aacu._aacx._aad6._aade").click() #followers butonu
        sleep(3)
        takipciler=self.browser.find_elements(By.CLASS_NAME,"_ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm") #users genel kutusus
        while True:
            if len(takipciler)<=number:
                self.ScrollDown_as_number()
                takipciler=self.browser.find_elements(By.CLASS_NAME,"_ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm") #users genel kutusus
            else:
                break
        say=1
        for takipci in takipciler:
            if say!=number+1:
                name=takipci.find_element(By.CLASS_NAME,"_ab8y._ab94._ab97._ab9f._ab9k._ab9p._abcm")# username
                takipci_link="https://www.instagram.com/"+name.text
                print(str(say)+"-->"+name.text +"-->"+takipci_link)
                say+=1
            else:break
    def ScrollDown_as_number(self):
        jsKomut = """
            sayfa = document.querySelector("._aano");
            sayfa.scrollTo(0, sayfa.scrollHeight);
            var sayfaSonu = sayfa.scrollHeight;
            return sayfaSonu;"""
        self.browser.execute_script(jsKomut)
    def follower_by_username(self,target_username,number):
        self.browser.get(f"https://www.instagram.com/{target_username}/")
        sleep(4)
        self.browser.find_element(By.CLASS_NAME,"_aacl._aacp._aacu._aacx._aad6._aade").click()#followers buton
        sleep(4)
        users=self.browser.find_elements(By.CLASS_NAME,"_ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm")# herbir kullanıcının genel kutusu
        while len(users)<=number:
                self.ScrollDown_as_number()
                sleep(2) 
                users=self.browser.find_elements(By.CLASS_NAME,"_ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm")# herbir kullanıcının genel kutusu
        for user in users:
            control=user.find_element(By.CLASS_NAME,"_aacl._aaco._aacw._aad6._aade").text
            control=control.lower()
            if control=="follow" or control=="takip et":
                user.find_element(By.CLASS_NAME,"_aacl._aaco._aacw._aad6._aade").click()
            else:continue







inte=Integram("your username","your password")
inte.sing_in()


#inte.get_all_following()#                        choose any function and remove '#' from it's head
#inte.get_followers_with_number(10)
#inte.follower_by_username("motivasyon.gelisim",10)






