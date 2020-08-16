#Importing modules
from bs4 import BeautifulSoup
import requests
import json

#creating url for search index
def url(search,page):
    prefi_url = "https://www.amazon.in/s?k="
    suffix_url = "&ref=nb_sb_noss"
    url_list = []
    home_page = prefi_url+search.replace(' ','+')+suffix_url
    url_list.append(home_page)
    for i in range(1,int(page)+1):
        url1 = prefi_url+search.replace(' ','+')+'&page='+str(i)+suffix_url
        url_list.append(url1)
    return url_list

#Making requests
def html(url):
    headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0)"
               " Gecko/20100101 Firefox/66.0"}
    try:
        r = requests.get(url,headers=headers) 
        soup = BeautifulSoup(r.content, features='lxml')
    except:
        pass
    return soup

#Type - 1 of amazon page style (when products are listed horizontal wise)
def product_data1(soup,count,product_details):
    links = soup.findAll('div',attrs={'class':'a-section a-spacing-medium a-text-center'})
    for i in range(len(links)):
        count = count+1
        try:
            l = links[i].findAll('a')[0]['href']
            product_link = 'https://amazon.in'+l
            product_title = links[i].find('span',attrs={'class':'a-size-base-plus a-color-base a-text-normal'}).get_text()
            product_image_link = links[i].find('img')['src']
            product_stars = links[i].find('a',attrs={'class':'a-popover-trigger a-declarative'}).get_text()
            product_price = 'Rs'+links[i].find('span',attrs={'class':'a-price-whole'}).get_text()
            product_price = product_price.replace('\u20b9','Rs')
            review_count = links[i].find('a',attrs={'class':'a-popover-trigger a-declarative'}).findNext('span').findNext('span').findNext('span').get_text()
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
            prod_link = 'https://amazon.in'+l[i].find('span',attrs={'class':'rush-component'}).find('a')['href']
            prod_img_link = l[i].find('span',attrs={'class':'rush-component'}).find('img')['src']
            prod_title = l[i].find('span',attrs={'class':'a-size-medium a-color-base a-text-normal'}).get_text()
            prod_stars = l[i].find('i').get_text()
            review_count = l[i].find('span',attrs={'class':'a-size-base'}).get_text()
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



#Main
search = input("Enter the text to be searched : ")
no_page = input("Enter the no. of Pages to scrape : ")


#Passing no.of pages and search index to be searched on amazon.in search box
url_list = url(search,no_page)

#Fetching the html content of these urls
contents = []
for url in url_list:
    contents.append(html(url))

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
    


