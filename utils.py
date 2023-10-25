from selenium.webdriver.common.by import By
from selenium import webdriver
import csv
import time



# Set up the Chrome webdriver
driver = webdriver.Chrome()



#-----------------login----------------------

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

#-----------------Scrape by user----------------------

def scrape_users_from_file(file_path, num_posts=10):
    with open(file_path, 'r') as file:
        usernames = file.read().splitlines()

    for username in usernames:
        print(f"Scraping posts from user: {username}")
        scrape_user_posts(username, num_posts)


# Function to scrape all post links from a user's profile
def scrape_user_posts(user_profile, num_posts=10):
    

    driver.get(f"https://www.instagram.com/{user_profile}/")
    time.sleep(2)

    # Scroll down to load more posts
    post_links = set()
    while len(post_links) < num_posts:
        post_elements = driver.find_elements(By.XPATH, "//a[contains(@href,'/p/')]")
        for post_element in post_elements:
            post_links.add(post_element.get_attribute("href"))

        # Scroll down to load more posts
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # Save post links to CSV file
    with open(r"C:\Users\amita\InstagramScraper\instaenv\instagram_user_posts.csv", mode='a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([[post_link] for post_link in list(post_links)[:num_posts]])


#-----------------Scrape by hashtag--------------------


# Function to scrape posts with a specific hashtag and save post links to CSV
def scrape_hashtag_posts(hashtag, num_posts=10):
   

    driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
    time.sleep(2)

    post_links = set()
    while len(post_links) < num_posts:
        links = driver.find_elements(By.XPATH, "//a[contains(@href,'/p/')]")
        for link in links:
            post_links.add(link.get_attribute("href"))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # Save post links to CSV file
    with open('instagram_post_links.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Post Link'])
        writer.writerows([[post_link] for post_link in post_links])