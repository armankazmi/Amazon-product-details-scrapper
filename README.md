# Amazon-product-details-scrapper

To scrape the details from [Amazon India](Amazon.in/) follow the steps:

**1. open the terminal in the file location and ```run pip3 install -r requirements.txt```**

**2. Run ```python amazon_scrap.py```**

**Note: Amazon keep changing its HTML layout so it is possible that some product details won't be accessible using this script. Also, making simulatneous requests to same page using same ip might lead to blocking of your ip. To avoid this free proxy servers can be used to make requests. For more refer to the comments in script amazon_scrap.py**

**One can use the [Amazon-simple-product-api](https://pypi.org/project/python-amazon-simple-product-api/) but one should have valid aws account and amazon associate key to access the product details.**

## **Sample**

**Input 1 :-**

Search :- 'Men stylish shirts'

Number of pages to scrape :- 4

**Json object desplaying first 5 product details out of 500+ product details**
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
     .......
```
     
**Input 2 :-**

Search :- 'Best smartphones under 15000'

Number of pages to scrape :- 3

**Json object desplaying first 5 product details**
```
{
     "1": {
          "Title": "Redmi 8A Dual (Sea Blue, 3GB RAM, 32GB Storage) \u2013 Dual Cameras & 5,000 mAH Battery",
          "Link": "https://amazon.in/Redmi-8A-Dual-Blue-Storage/dp/B07WPVLKPW/ref=sr_1_1?dchild=1&keywords=best+smartphones+under+15000&qid=1597561872&sr=8-1",
          "Image link": "https://m.media-amazon.com/images/I/71yXShgxvpL._AC_UY218_.jpg",
          "Price": "Rs8,299",
          "Stars": "4.0 out of 5 stars",
          "No of reviews": "10,621"
     },
     "2": {
          "Title": "Vivo U20 (Blazing Blue, Snapdragon 675 AIE, 4GB RAM, 64GB Storage)",
          "Link": "https://amazon.in/Vivo-Blazing-Blue-Snapdragon-Storage/dp/B081RTYX3M/ref=sr_1_3?dchild=1&keywords=best+smartphones+under+15000&qid=1597561872&sr=8-3",
          "Image link": "https://m.media-amazon.com/images/I/5146hJBeZqL._AC_UY218_.jpg",
          "Price": "Rs12,990",
          "Stars": "4.4 out of 5 stars",
          "No of reviews": "14,813"
     },
     "3": {
          "Title": "Redmi 8A Dual (Sky White, 2GB RAM, 32GB Storage) \u2013 Dual Cameras & 5,000 mAH Battery",
          "Link": "https://amazon.in/Redmi-8A-Dual-White-Storage/dp/B07X1KSWZ3/ref=sr_1_4?dchild=1&keywords=best+smartphones+under+15000&qid=1597561872&sr=8-4",
          "Image link": "https://m.media-amazon.com/images/I/710p2f-zAdL._AC_UY218_.jpg",
          "Price": "Rs7,499",
          "Stars": "4.0 out of 5 stars",
          "No of reviews": "10,621"
     },
     "4": {
          "Title": "Redmi Note 9 Pro (Interstellar Black, 4GB RAM, 64GB Storage) - Latest 8nm Snapdragon 720G & Gorilla Glass 5 Protection",
          "Link": "https://amazon.in/Test-Exclusive-549/dp/B077PWBC78/ref=sr_1_7?dchild=1&keywords=best+smartphones+under+15000&qid=1597561872&sr=8-7",
          "Image link": "https://m.media-amazon.com/images/I/91Lr-OxVKjL._AC_UY218_.jpg",
          "Price": "Rs13,999",
          "Stars": "4.2 out of 5 stars",
          "No of reviews": "2,443"
     },
     "5": {
          "Title": "Vivo Y15 (Aqua Blue, 4GB RAM, 64GB Storage) with No Cost EMI/Additional Exchange",
          "Link": "https://amazon.in/Vivo-Aqua-Storage-Additional-Exchange/dp/B07S6BGL1K/ref=sr_1_8?dchild=1&keywords=best+smartphones+under+15000&qid=1597561872&sr=8-8",
          "Image link": "https://m.media-amazon.com/images/I/61d5kbgcBxL._AC_UY218_.jpg",
          "Price": "Rs12,990",
          "Stars": "4.2 out of 5 stars",
          "No of reviews": "2,914"
     },
     .....
```
