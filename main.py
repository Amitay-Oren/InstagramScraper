import json
from instagram_scraper import login
from instagram_scraper import scrape_hashtag_posts
from selenium import webdriver

# Target Instagram hashtag
hashtag = "freepalestine"

# Main script
def main():
    try:
        # Load credentials from credential.json
        with open('credentials.json') as f:
            credentials = json.load(f)

        # Extract username and password
        username = credentials['username']
        password = credentials['password']

        login(username, password)
        scrape_hashtag_posts(hashtag, num_posts=10)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    driver = webdriver.Chrome()  # Define the driver variable
    main()