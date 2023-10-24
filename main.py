import json
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Target Instagram hashtag
hashtag = "freepalestine"

# Target Instagram user
user_profile = "mdfighters"  # Replace with the user's profile you want to scrape

# Set up the Chrome webdriver
driver = webdriver.Chrome()

# Function to login to Instagram
def login(username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys(username)
    password_field.send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(5)


# Main script
def main():
    from ScrapeByHashtag import scrape_hashtag_posts
    from ScrapeByUser import scrape_user_posts

    try:
        # Load credentials from credential.json
        with open('credentials.json') as f:
            credentials = json.load(f)

        # Extract username and password
        username = credentials['username']
        password = credentials['password']

        
        global driver
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
