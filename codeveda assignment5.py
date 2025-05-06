import requests
from bs4 import BeautifulSoup

# Function to get the webpage content
def get_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

# Function to extract headlines
def extract_headlines(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')

    # Try finding headlines with a general approach or adjust the tag/class based on inspection
    headlines = soup.find_all('h3')  # We can also try 'h2', 'span', or others
    print("\n--- Extracted Headlines ---")
    if not headlines:
        print("No headlines found.")
    for index, headline in enumerate(headlines, 1):
        print(f"{index}. {headline.text.strip()}")

# Main script to run the scraper
if __name__ == "__main__":
    # Get user input for the URL of the website
    url = input("Enter the URL of the website: ")

    page_content = get_page(url)
    
    if page_content:
        extract_headlines(page_content)
