from requests import get
from bs4 import BeautifulSoup
import pandas as pd

url=input("Enter the URL: ")
N=int(input("Enter the maximum number of reviews you need: "))
base_url =url
base_response = get(base_url)
html_soup = BeautifulSoup(base_response.text, 'html.parser')

#movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')

result_df = pd.DataFrame()


num_reviews = N
# Searching all reviews
reviews_containers = html_soup.find_all('div', class_ = 'imdb-user-review')
# Check if actual number of reviews is less than target one
if len(reviews_containers) < num_reviews:
    num_reviews = len(reviews_containers)
# Looping through each review and extracting title and body
reviews_titles = []
reviews_bodies = []
for review_index in range(num_reviews):
    review_container = reviews_containers[review_index]
    review_title = review_container.find('a', class_ = 'title').text.strip()
    review_body = review_container.find('div', class_ = 'text').text.strip()
    reviews_titles.append(review_title)
    reviews_bodies.append(review_body)

L=len(reviews_titles)

for i in range(L):
    print(str(i+1)+"."+reviews_titles[i])
    print(" "+reviews_bodies[i])
    print("")
