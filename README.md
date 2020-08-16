# Amazon-product-details-scrapper

To scrape the details from [Amazon India](Amazon.in/) follow the steps:

**1. open the terminal in the file location and ```run pip3 install -r requirements.txt```

**2. Run ```python amazon_scrap.py```

##Note: Amazon keep changing its HTML layout so it is possible that some product details won't be accessible using this script.
**One can use the [Amazon-simple-product-api](https://pypi.org/project/python-amazon-simple-product-api/) but one should have valid aws account and amazon associate key to access the product details.

##**Sample

**Search :- 'Men stylish shirts'

**Number of pages to scrape :- 4

**Json object desplaying first 5 product details
```{
     "1": {
          "Title": "Men's Slim Fit Shirt",
          "Link": "https://amazon.in/gp/bestsellers/apparel/1968094031/ref=sr_bs_0_1968094031_1",
          "Image link": "https://m.media-amazon.com/images/I/718rD4AqFJL._AC_UL320_.jpg",
          "Price": "Rs397",
          "Stars": "3.2 out of 5 stars",
          "No of reviews": "554"
     },
     "2": {
          "Title": "Cotton Polka Print Dotted Shirts for Men for Formal Use,100% Cotton Shirts,Office Wear Shirts, M=38,L=40,XL=42",
          "Link": "https://amazon.in/Super-weston-Cotton-Dotted-Shirts/dp/B084L8T75F/ref=sr_1_2?dchild=1&keywords=men+stylish+shirts&qid=1597561195&sr=8-2",
          "Image link": "https://m.media-amazon.com/images/I/81q1-5edHwL._AC_UL320_.jpg",
          "Price": "Rs399",
          "Stars": "2.9 out of 5 stars",
          "No of reviews": "55"
     },
     "3": {
          "Title": "Men's Solid Slim Fit Casual Shirt",
          "Link": "https://amazon.in/Dennis-Lingo-Casual-C501_Light-Blue_Medium/dp/B06XR3XD6L/ref=sr_1_3?dchild=1&keywords=men+stylish+shirts&qid=1597561195&sr=8-3",
          "Image link": "https://m.media-amazon.com/images/I/61XA8LSTF1L._AC_UL320_.jpg",
          "Price": "Rs749",
          "Stars": "3.8 out of 5 stars",
          "No of reviews": "566"
     },
     "4": {
          "Title": "Men's Casual Shirt",
          "Link": "https://amazon.in/Dennis-Lingo-Solid-Casual-CC201_Dustypink_M_Dustypink_M/dp/B07HK6NT81/ref=sr_1_4?dchild=1&keywords=men+stylish+shirts&qid=1597561195&sr=8-4",
          "Image link": "https://m.media-amazon.com/images/I/61YQd1wdQBL._AC_UL320_.jpg",
          "Price": "Rs549",
          "Stars": "3.8 out of 5 stars",
          "No of reviews": "3,035"
     },
     "5": {
          "Title": "Men's Slim Fit T-Shirt",
          "Link": "https://amazon.in/Blisstone-Cotton-Hooded-T-Shirt-Large/dp/B07M85JLCR/ref=sr_1_5?dchild=1&keywords=men+stylish+shirts&qid=1597561195&sr=8-5",
          "Image link": "https://m.media-amazon.com/images/I/71sE+WiLKjL._AC_UL320_.jpg",
          "Price": "Rs258",
          "Stars": "3.6 out of 5 stars",
          "No of reviews": "384"
     }
     ```
    
