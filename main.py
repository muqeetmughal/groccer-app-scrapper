from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
from time import sleep
import requests
import httplib2
import os
import json
import urllib.request
import random
timer = 60
homeurl = "https://grocerapp.pk"


categorynamelist = ['Fruits & Vegetables', 'Fresh Meat', 'Grocery', 'Personal Care', 'Dry Fruit & Nuts', 'Home Care', 'Baby Care', 'Bakery & Dairy', 'Beverages', 'Instant Food', 'Frozen & Chilled', 'OTC & Wellness', 'Pan Shop', 'Pet Care']
categoryurllist = ['https://grocerapp.pk/cn/fruits-and-vegetables/cid/1','https://grocerapp.pk/cn/fresh-meat/cid/226','https://grocerapp.pk/cn/grocery/cid/145','https://grocerapp.pk/cn/personal-care/cid/83','https://grocerapp.pk/cn/dry-fruit-and-nuts/cid/364','https://grocerapp.pk/cn/home-care/cid/10','https://grocerapp.pk/cn/baby-care/cid/99','https://grocerapp.pk/cn/bakery-and-dairy/cid/17','https://grocerapp.pk/cn/beverages/cid/15','https://grocerapp.pk/cn/instant-food/cid/16','https://grocerapp.pk/cn/frozen-and-chilled/cid/212','https://grocerapp.pk/cn/otc-and-wellness/cid/218','https://grocerapp.pk/cn/pan-shop/cid/12','https://grocerapp.pk/cn/pet-care/cid/224']
productlinks = []
allproductlink = []
class groccerapp():


    def __init__(self):
        self.driver = webdriver.Chrome('C:/webdriver/chromedriver.exe')
        # self.linkgenerator()
        self.productscrape()

    def createFolder(self, name):
        try:
            os.mkdir(name)
            print("\n Directory " , name ,  " Created ") 
        except FileExistsError:
            print("\n Directory " , name ,  " already exists")

    def linkgenerator(self):
        for x in range(len(categoryurllist)):
            self.driver.get(categoryurllist[x])
            sleep(3)
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(timer)
            page_sauce = self.driver.page_source
            for link in BeautifulSoup(page_sauce, features='html.parser', parse_only=SoupStrainer('a')):
                if link.has_attr('href'):
                    productlinks.append(homeurl + link['href'])
            generatedproductlink = [ link for link in productlinks if "prn" in link ]
        
            allproductlink.extend(generatedproductlink)

            with open('productUrlsList.txt', 'w') as filehandle:
                json.dump(allproductlink, filehandle)
            print("\n"+categorynamelist[x]+"=> Completed Successfully")

    def productscrape(self):
        with open('productUrlsList.txt', 'r') as filehandle:
                restoredUrlList = json.load(filehandle)
        for product_link_loop in range(len(restoredUrlList)):
            self.driver.get(random.choice(restoredUrlList))
            try:
                sleep(1)
                self.driver.find_element_by_xpath('//span[@jsselect="heading" and @jsvalues=".innerHTML:msg"]')
                print('No Internet connection, aborted!')
            except:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                sleep(5)
                product_source = self.driver.page_source
                product_soup = BeautifulSoup(product_source,features='html.parser')

                if not product_soup.find_all("body", string="found"):
                    mainTag = product_soup.find('main')
                    three_divs_in_main_Tag = mainTag.find_all('div')
                    four_divs_inside_1st_div_of_Main = three_divs_in_main_Tag[0].find_all('div',recursive=False, limit=4)
                    
                    folder_name = four_divs_inside_1st_div_of_Main[1].find('img', alt=True)
                    image_url = four_divs_inside_1st_div_of_Main[1].find('img', src=True)

                    folderName = folder_name['alt']
                    imageNameFull = folderName + ".jpeg"
                    imagePath = folderName + "/" +imageNameFull

                    if os.path.exists(folderName):
                        print("Skipped Because Already Exists: "+folderName)
                        continue
                    else:
                        self.createFolder(folderName)
                        sleep(0.5)
                        self.downloadImage(image_url['src'], imagePath)
                        self.description(folderName,four_divs_inside_1st_div_of_Main)
                        
    def downloadImage(self, imageUrl ,image_Path):
        response = requests.get(imageUrl)
        file = open(image_Path, "wb")
        file.write(response.content)
        file.close()
        print(image_Path+" ===> Saved")

    def description(self,folderName,four_divs):
        section1 = open(folderName+'/'+ folderName +'.txt','w+', encoding="utf-8")
        section1.write(four_divs[0].text)
        section1.write("\n")
        section1.close()

        section2 = open(folderName+'/'+ folderName +'.txt','a', encoding="utf-8")
        section2.write(four_divs[1].text)
        section2.write("\n")
        section2.close()

        section3 = open(folderName+'/'+ folderName +'.txt','a', encoding="utf-8")
        section3.write(four_divs[2].text)
        section3.write("\n")
        section3.close()

        section4 = open(folderName+'/'+ folderName +'.txt','a', encoding="utf-8")
        section4.write(four_divs[3].text)
        section4.write("\n")
        section4.close()
        print("\nDescription Added")

m = groccerapp()