import json
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from utils import scrape_hashtag_posts, scrape_user_posts, login

# Target Instagram hashtag
hashtag = "freepalestine"

# Target Instagram user
user_profile = "mdfighters"  # Replace with the user's profile you want to scrape






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
        scrape_user_posts(user_profile, num_posts=10)

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    driver = webdriver.Chrome()  # Define the driver variable
    main()
