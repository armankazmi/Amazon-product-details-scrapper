#Title : This script scrappes products data from amazon india website where you can search for any items
#author: Arman Kazmi

#Importing modules
from bs4 import BeautifulSoup
import requests
import json


#creating url for search inputs with uls upto specified page numbers
def url(search,page):
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

'''
    Note: making requests to same page multiple times can lead to blocking of your ip from amazon webpage.
    To avoid this a list of proxies can be used to make request using different ips, or there should be some time gap between making requests to same url.
    
'''
#Listing all  free proxies from https://free-proxy-list.net/. Uncomment below function to use proxies
'''
def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies
'''
#Making requests
def html(url):
    headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0)"
               " Gecko/20100101 Firefox/66.0"}
    try:
        #uncomment to use proxy ip for scraping
        #proxies = get_free_proxies()
        #proxy = random.choice(proxies)
        #r = requests.get(url,proxies=proxies,headers=headers)
        r = requests.get(url,headers=headers) 
        soup = BeautifulSoup(r.content, features='lxml')
    except:
        pass
    return soup


#Type - 1 of amazon page style (when products are listed horizontal wise)
#Sample url = https://www.amazon.in/s?k=men+shirts&ref=nb_sb_noss

def product_data1(soup,count,product_details):
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


#Type - 2 of amazon page style (when products are listed vertical wise)
def product_data2(soup,count,product_details):
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

def main(search,no_page):
    #Passing no.of pages and search index to be searched on amazon.in search box
    ulist = url(search,no_page)

    #Fetching the html content of these urls
    contents = []
    for link in ulist:
        contents.append(html(link))

    final_data = {}  #creating dictionary of product details where key will be index
    c = 0
    c1 = 0
    for soup in contents:
        final_data,c = product_data1(soup,c,final_data)
        if (not final_data) == True:                                           #checking if products in page are listed horizontal or vertical wise
            final_data,c1 = product_data2(soup,c1,final_data)                  #products listing in vertical wise
        else:
            final_data,c = product_data1(soup,c,final_data)


    #To convert in Json Format
    # Serializing json with indent = 5
    json_object = json.dumps(final_data, indent = 5)   
    print(json_object)

    
    
#Main
search = input("Enter the text to be searched : ")
no_page = input("Enter the no. of Pages to scrape (pages should be greater than 0 and less than 7 : ")
if (int(no_page)>0 and int(no_page)<=7):
    main(search,no_page)
else:
    print("Try again Page index error")
