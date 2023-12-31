import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.com/biz/stanford-shopping-center-palo-alto"
response = requests.get(url)

# Check for a successful request
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 4: Extract the Links
    links = []
    for link in soup.find_all('a', class_='biz-name'):
        restaurant_link = link.get('href')
        links.append(restaurant_link)

    # Step 5: Construct Full URLs
    base_url = "https://www.yelp.com"
    full_links = [base_url + link for link in links]

    # Step 6: Iterate Over the Restaurant Pages
    for restaurant_url in full_links:
        restaurant_response = requests.get(restaurant_url)
        if restaurant_response.status_code == 200:
            restaurant_soup = BeautifulSoup(restaurant_response.text, 'html.parser')
