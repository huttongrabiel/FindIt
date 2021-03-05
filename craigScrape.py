from requests import get
from time import sleep
from random import randint
from bs4 import BeautifulSoup

link = input("Enter the link to your local craigslist: ")
stolen_good = input("Enter the name of your stolen good: ").lower().split()

response = get(link)
souper = BeautifulSoup(response.text, 'html.parser')

posts = souper.find_all('li', class_='result-row')

post_titles = []

#Begin to loop through each page and access the title
#Every title will be added to the post_titles[] list and then compared to the given item

for post in posts: # Looping through each post on a page
  post_title = post.find('a', class_='result-title hdrlnk')
  post_text = post_title.text
  
  post_titles.append(post_text.lower())

sleep(randint(1,8)) #Random sleep to be gentle to server

item_count = 120

while item_count <= 2880: #Stops the program on the last page of the for sale section
  page_link = link + '?s=' + str(item_count) #Updating link
  
  response_two = get(page_link)
  html_soup = BeautifulSoup(response_two.text, 'html.parser')

  post_set = html_soup.find_all('li', class_='result-row')
  
  for item in post_set: #Adds the title of each item to one list
    post_set_title = item.find('a', class_='result-title hdrlnk')
    post_title_text = post_set_title.text

    post_titles.append(post_title_text)

  item_count += 120  #Increment by 120 to go to next page 

print("DISCLAIMER: You may need to try multiple phrases to find a matching answer, if"
      "the first does not return any solid results, change your word order and/or words")

print("Try searching for these items: ") 

title_words = []

for title in post_titles: #Checking if any item matches the given description
  for word in stolen_good:
    if word in title:
      match = title
      print(match)
# To continue we need to find which item matches and then return that to the user
# Ideally we would like to pull the exact link for the item and display it
