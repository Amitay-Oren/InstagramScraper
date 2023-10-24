from selenium.webdriver.common.by import By
import csv
import time
from main import driver








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

# # Main script
# try:
#     login(username, password)
#     file_path = r"C:\Users\amita\InstagramScraper\users.txt"  # Specify the file path to the usernames list
#     scrape_users_from_file(file_path, num_posts=10)
# except Exception as e:
#     print("An error occurred:", e)
# finally:
#     driver.quit()