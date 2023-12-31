
import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage you want to scrape
url = "https://www.tripadvisor.com/Restaurant_Review-g186319-d1209702-Reviews-The_Old_Stamp_House_Restaurant-Ambleside_Lake_District_Cumbria_England.html#REVIEWS"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Identify the HTML structure that contains reviews
    review_elements = soup.find_all('div', class_='review')

    # Loop through each review element and extract data
    for review in review_elements:
        # Extract restaurant name
        restaurant_name = review.find('h2', class_='restaurant-name').text.strip()

        # Extract review content
        review_content = review.find('p', class_='review-content').text.strip()

        # Extract review rating
        review_rating = review.find('span', class_='rating').text.strip()

        # Extract date of review
        date_of_review = review.find('span', class_='review-date').text.strip()

        # Extract type of cuisine
        type_of_cuisine = review.find('span', class_='cuisine-type').text.strip()

        # Print or store the collected data
        print("Restaurant Name:", restaurant_name)
        print("Review Content:", review_content)
        print("Review Rating:", review_rating)
        print("Date of Review:", date_of_review)
        print("Type of Cuisine:", type_of_cuisine)
        print("\n")
else:
    print("Failed to retrieve the webpage.")

