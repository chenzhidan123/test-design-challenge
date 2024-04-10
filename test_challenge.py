from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pdb
import re

class TestAutomationChallenge:
    #Initialze the webdriver
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.EXPECTED_FOLLOWER = 5
        self.driver.get("https://onskeskyen.dk/")
        
    #Click the "ACCEPTER ALLE" bottom
    def click_accpect(self):
       accept_bottom = self.driver.find_element(By.CLASS_NAME,'coi-banner__accept')
       accept_bottom.click()


    # Click on the "Inspiration" 
    def click_inspiration(self):
        inspiration_menu = self.driver.find_element(By.CSS_SELECTOR,"button.ant-btn.css-120k5fe.ant-btn-round.ant-btn-text.ant-btn-lg.PublicMenu__Button-sc-1c794c8-9.cmtACl")
        inspiration_menu.click()

    # Click on the "Brands" 
    def click_brands(self):
        brands_submenu = self.driver.find_element(By.LINK_TEXT,"Brands")
        brands_submenu.click()

    #Selects the Børn & Baby category
    def click_born(self):
        baby_category = self.driver.find_element(By.CSS_SELECTOR,"#__next > div.MainContainer__Container-sc-6fe7f2f9-0.dDXZTf > div > div > div.brands__CategoriesContainer-sc-61b5e112-2.ebcMuA > div > button:nth-child(8)")
        baby_category.click()
    #Load more brands    
    def load_more_brands(self):
        view_more = self.driver.find_element(By.CSS_SELECTOR,'.CarouselViewAllButton__BtnText-sc-1a7e4de1-0')
        view_more.click()
    # Click on the "Brands" 
    def click_plysdyr(self):
        plysdyr_pic = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div/div[4]/div[2]/div[59]/div/div/div/span/img')
        plysdyr_pic.click()

    # Opens the De største bamser trending list
    def click_trending_list(self):
        trending_list = self.driver.find_element(By.CSS_SELECTOR,'#__next > div.MainContainer__Container-sc-6fe7f2f9-0.fjwrOO > div > div > div.BubbleContainer__Container-sc-286d7772-0.jjujcf > div > div.BrandPageContent__Container-sc-3d77230c-0.ctYqFq > div.CarouselContainer__MyContainer-sc-ae5c0300-0.bvjkri > div.slick-slider.CarouselTrendingLists__MySlider-sc-86a9c3ae-0.fnYPNt.slick-initialized > div > div > div.slick-slide.slick-active.slick-current > div > div > div > div > div.TrendingListCard__CardBottomContainer-sc-8d8a5b12-2.kjjvZm > div > div > div.TrendingListCard__TrendListTitle-sc-8d8a5b12-4.cEnsit')
        trending_list.click()

    #Obtain the follower number
    def get_follower_num(self):
        follower = self.driver.find_element(By.CSS_SELECTOR,'.Followers__FollowersCount-sc-b7d8d0bc-0.dlJBA-d').text
        follower_num = re.search(r'\d+',follower).group(0)
        return follower_num
    
    # Asserts on the number of trending list followers
    def assert_follower_num(self,follower_num):
        try:
            assert int(follower_num) == self.EXPECTED_FOLLOWER
            print ('CASE PASS')
        except:
            print("CASE FAIL->Expect follower is {}, Actual follower is {}".format(self.EXPECTED_FOLLOWER,follower_num))
        
    def main(self):
        self.click_accpect()
        self.click_inspiration()
        self.click_brands()
        self.click_born()
        self.load_more_brands()
        time.sleep(2)
        self.load_more_brands()
        time.sleep(2)
        self.click_plysdyr()
        self.click_trending_list()
        follower_num = self.get_follower_num()
        self.assert_follower_num(follower_num)
        self.driver.quit()
        
if __name__ == "__main__":
    case1 = TestAutomationChallenge()
    case1.main()
    
 
