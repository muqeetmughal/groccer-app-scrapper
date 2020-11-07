from bs4 import BeautifulSoup as BS
from selenium import webdriver
from time import sleep
import requests
homeurl = "https://grocerapp.pk"
categoryurl = "https://grocerapp.pk/categories"

categoryNames = []
categoryUrls = []

# categorynamelist = ['Fruits & Vegetables', 'Fresh Meat', 'Grocery', 'Personal Care', 'Dry Fruit & Nuts', 'Home Care', 'Baby Care', 'Bakery & Dairy', 'Beverages', 'Instant Food', 'Frozen & Chilled', 'OTC & Wellness', 'Pan Shop', 'Pet Care']
# catgegoryurllist = ['https://grocerapp.pk/cn/fruits-and-vegetables/cid/1','https://grocerapp.pk/cn/fresh-meat/cid/226','https://grocerapp.pk/cn/grocery/cid/145','https://grocerapp.pk/cn/personal-care/cid/83','https://grocerapp.pk/cn/dry-fruit-and-nuts/cid/364','https://grocerapp.pk/cn/home-care/cid/10','https://grocerapp.pk/cn/baby-care/cid/99','https://grocerapp.pk/cn/bakery-and-dairy/cid/17','https://grocerapp.pk/cn/beverages/cid/15','https://grocerapp.pk/cn/instant-food/cid/16','https://grocerapp.pk/cn/frozen-and-chilled/cid/212','https://grocerapp.pk/cn/otc-and-wellness/cid/218','https://grocerapp.pk/cn/pan-shop/cid/12','https://grocerapp.pk/cn/pet-care/cid/224']

class groccerapp():

    def __init__(self):
        self.driver =  webdriver.Chrome('C:\webdriver/chromedriver.exe')
        sleep(1)
        self.categories()
        
    #--------------------------------------------------------------------------------------
#------------Uncomment the Below Code for Generating categories Names and Links--------
    def categories(self):
        self.driver.get(categoryurl)
        sleep(3)
        page_source = self.driver.page_source
        soup = BS(page_source,'html.parser')
        categoryTable = soup.find('div', attrs={'class':'jss214'})

        for a in categoryTable.find_all("a"):
            categoryNames.append(a['aria-label'])
            
        for a in categoryTable.find_all('a', href=True):
            categoryUrls.append(homeurl+a['href'])
        print(categoryNames)
        print(categoryUrls)
#---------------------------------------------------------------------------------------
    # def categoryPage(self):
    #     # for x in range(len(categorynamelist)):
    #         self.driver.get(catgegoryurllist[0])
    #         sleep(3)
    #         page_source = self.driver.page_source
    #         categorySoup = BS(page_source, 'html.parser')


            # print("Name: "+categorynamelist[x]+"    Link: "+catgegoryurllist[x])




    # def site(self):
    #     self.driver.get(categoryurl)
    #     sleep(3)



m = groccerapp()




# self.driver =  webdriver.Chrome('C:\webdriver/chromedriver.exe')
#         sleep(1)


# categoryNames = []
# categoryUrls = []

#--------------------------------------------------------------------------------------
#------------Uncomment the Below Code for Generating categories Names and Links--------
    # def categories(self):
    #     page_source = self.driver.page_source
    #     soup = BS(page_source,'html.parser')
    #     categoryTable = soup.find('div', attrs={'class':'jss214'})

    #     for a in categoryTable.find_all("a"):
    #         categoryNames.append(a['aria-label'])
            
    #     for a in categoryTable.find_all('a', href=True):
    #         categoryUrls.append(homeurl+a['href'])
    #     print(categoryNames)
    #     print(categoryUrls)
#---------------------------------------------------------------------------------------