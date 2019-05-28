#imports the beautiful soup library for use, bs4 is for the beautiful soup module

#urllib request is the one that requests the data in the server
from urllib.request import urlopen as uReq

#import the bs4 and name it as a variable, use this in order to call it and simplify it
from bs4 import BeautifulSoup as soup


#save the url needed into a variable
myUrl = 'https://www.flipkart.com/search?q=iphone&marketplace=FLIPKART&otracker=start&as-show=on&as=off'

#use the uReq variable and pass through the url saved in the variable.
uClient = uReq(myUrl)

#use the method read in order to read the url and save it into a variable
page_html = uClient.read()

#use the bs4 used as a variable and save it into a variable
page_soup = soup(page_html,'html.parser')

#the containers is the variable name , the findall method means that you find all that is a div, which is a class (insert as stated)
containers = page_soup.findAll('div',{'class':'bhgxx2 col-12-12'})

#the containers are checked through inspecting the webpage in order to find the needed object to be scraped
containers = containers[4:27]
#print (soup.prettify(containers[0]))

numbers = 0
#use a variable in order to create a csv file

filename = 'apple_iphone_flipkart.csv'
#open a file and use "w" as a command to write  a file

f = open(filename,'w')
#this is the headers for the csv file, 

headers = 'Product_name,Number_of_ratings,Actual_rating,Description,Price\n'

f.write(headers)

for items in containers:
   numbers +=1
   name = items.div.img["alt"]
   
#   print ("Item ",numbers," ", name)

   ratings_and_reviews_container = items.findAll('span',{'class':'_38sUEc'})
   ratings_and_reviews = ratings_and_reviews_container[0].text
   
#   print ('Number of Ratings are: ',ratings_and_reviews)

   rating_container = items.findAll('div',{'class':'hGSR34 _2beYZw'})
   rating = rating_container[0].text
#   Had to use this block of code so that the encoder can read the and pass through symbols
   new = rating.encode('utf-8')
#   encoded it into utf-8 and decoded again to ignore unsupported symbols
   ratingz = new.decode('ascii','ignore')
   
#   print ('Actual Rating: ', rating)

   description_container = items.findAll('div', {'class':'_3ULzGw'})
   description = description_container[0].text
#   print ("Description: ", description)

   price_container = items.findAll('div', {'class':'col col-5-12 _2o7WAb'})
   price = price_container[0].text
   trim_price = ''.join(price.split(','))
   rm_rupee = trim_price.split('₹')
   final_price = rm_rupee[1]
   
#   print (final_price)

   f.write(name.replace(',','|') + ',' + ratingz + ',' + ratings_and_reviews.replace(',','|') + ',' + description.replace(',','|') + ',' + final_price.replace(',','|') + '\n')
    

f.close()