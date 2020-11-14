#Title : This script scrappes products data from amazon india website where you can search for any items
#author: Arman Kazmi

'''
Note: The script return product details only for those items where all fields have values, if any of the fiels is NONE it ingnores that product.
It can be changed by using try and except for each required field.
'''

#Importing modules
from bs4 import BeautifulSoup
import requests
import json


class Amazon():
    
    
    
    '''Steps followed to scrape the data:-
          1. Amazon.Main function takes arguments search string and number of pages as integer to generates the final data.
          2. Amazon.url function returns the web addresses of the pages
          3. Amazon.html function returns the html contents of the urls
          4. Amazon India webpage lists product in two different styles:
            a. When product are listed in a horizontal list order (Sample url = https://www.amazon.in/s?k=men+shirts&ref=nb_sb_noss) Amazon.product_data1 function is used
            b. When product are listed in vertical list order (Sample url : - https://www.amazon.in/s?k=laptops&ref=nb_sb_noss) Amazon.product_data2 function is used
        
         Note: Making requests to same page multiple times can lead to blocking of your ip from amazon webpage.
           To avoid this a list of proxies can be used to make request using different ips, or there should be some time gap between making requests to same url.
           For this uncomment the function get_free_proxies()
      '''

    def __init__(self, s, p):
        self.search = s
        self.page  = p
            
    def main(self):
        urllist = self.url(self.search,self.page)
        # contents = []
        product_data ={}
        count1 = 0
        count2 = 0
        for link in urllist:
            content = self.html(link)
            product_data,count1 = self.product_data1(content,count1,product_data)
            if (not product_data) == True:
                product_data,count2 = self.product_data2(content,count2,product_data) 
            else:
                product_data,count1 = self.product_data1(content,count1,product_data)        
            if (not product_data ) == True:
                print("No information available. Try with a different search input.")
            else:
                json_object = json.dumps(product_data, indent = 5)   
                print(json_object)
   
    def url(self,search,page):
        prefi_url = "https://www.amazon.in/s?k="
        suffix_url = "&ref=nb_sb_noss"
        url_list = []
        #initial page for scrapping
        home_page = prefi_url+search.replace(' ','+')+suffix_url
        url_list.append(home_page)
        for i in range(1,int(page)+1):
            #generating url for each page numbers
            url1 = prefi_url+search.replace(' ','+')+'&page='+str(i)+suffix_url
            url_list.append(url1)
        return url_list
    
    
#     def get_free_proxies(self):
#         url = "https://free-proxy-list.net/"
#         # get the HTTP response and construct soup object
#         so = BeautifulSoup(requests.get(url).content, "html.parser")
#         proxies = []
#         for row in so.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
#             tds = row.find_all("td")
#             try:
#                 ip = tds[0].text.strip()
#                 port = tds[1].text.strip()
#                 host = f"{ip}:{port}"
#                 proxies.append(host)
#             except IndexError:
#                 continue
#         return proxies
    
    def html(self,url):
        headers = {"User-Agent":
                    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0)"
                    " Gecko/20100101 Firefox/66.0"}
      
    #         prox = self.get_free_proxies()
#         session = requests.Session()
#         proxy = random.choice(prox)
#         session.proxies = {"http": proxy, "https": proxy}
#         r = session.get(url,headers=headers)
        try:
            r = requests.get(url,headers=headers) 
            parsed = BeautifulSoup(r.content, features='lxml')
        except:
            pass
        return parsed
    
    #Type 1 of Amazon Webpage
    def product_data1(self,soup,count,product_details):
        links = soup.findAll('div',attrs={'class':'a-section a-spacing-medium a-text-center'})
        for i in range(len(links)):
            count = count+1
            try:
                l = links[i].findAll('a')[0]['href']
                #link of product
                product_link = 'https://amazon.in'+l
                #product Title
                product_title = links[i].find('span',attrs={'class':'a-size-base-plus a-color-base a-text-normal'}).get_text()
                #Product Image link
                product_image_link = links[i].find('img')['src']
                #No of stars given to product
                product_stars = links[i].find('a',attrs={'class':'a-popover-trigger a-declarative'}).get_text()
                #Price available 
                product_price = 'Rs'+links[i].find('span',attrs={'class':'a-price-whole'}).get_text()
                product_price = product_price.replace('\u20b9','Rs')
                #No. of reviews available
                review_count = links[i].find('a',attrs={'class':'a-popover-trigger a-declarative'}).findNext('span').findNext('span').findNext('span').get_text()
                #creating a dictionary for product details
                details = {'Title' : product_title,
                            'Link' : product_link,
                            'Image link' : product_image_link,
                            'Price' : product_price,
                            'Stars' : product_stars,
                            'No of reviews' : review_count
                  }
                product_details[count] = details
            except:
                count = count-1
                continue
        return product_details,count

    #Type 2 of Amazon Webpage
    def product_data2(self,soup,count,product_details):
        links = soup.findAll('div',attrs={'class':'s-main-slot s-result-list s-search-results sg-row'})
        l = links[0].findAll('div',attrs={'class':'sg-col-inner'})
        for i in range(len(l)):
            count= count+1
            try:
                #product Link
                prod_link = 'https://amazon.in'+l[i].find('span',attrs={'class':'rush-component'}).find('a')['href']
                #product Image Link
                prod_img_link = l[i].find('span',attrs={'class':'rush-component'}).find('img')['src']
                #Product title
                prod_title = l[i].find('span',attrs={'class':'a-size-medium a-color-base a-text-normal'}).get_text()
                #product stars given
                prod_stars = l[i].find('i').get_text()
                #No. of reviews
                review_count = l[i].find('span',attrs={'class':'a-size-base'}).get_text()
                #product Price
                prod_price = l[i].find('span',attrs={'class':'a-price'}).findNext('span').get_text()
                prod_price = prod_price.replace('\u20b9','Rs')
                details = {'Title' : prod_title,
                            'Link' : prod_link,
                            'Image link' : prod_img_link,
                            'Price' : prod_price,
                            'Stars' : prod_stars,
                            'No of reviews' : review_count
                        }
                product_details[count] = details
            except:
                count = count-1
                continue
        return product_details,count
    
    
#Search Input 
'''
Sample search inputs:-
    1. men  stylish shirts
    2. Laptops under 30000
    3. men sunglasses
    4. smartphones under 10000
'''

search_text = input("Enter the text to be searched : ")
no_page = input("Enter the no. of Pages to scrape (pages should be greater than 0 and less than 7 : ")

#Since for most of the product listed in horizontal view has max no. of 7 pages so providing a upper limit of 7 pages

if (int(no_page)>0 and int(no_page)<=7):
    sample = Amazon(search_text,no_page)
    sample.main()
else:
    print("Try again Page index error")
