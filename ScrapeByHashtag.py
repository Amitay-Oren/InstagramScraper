from selenium.webdriver.common.by import By
import csv
import time
from main import driver






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

# # Main script
# try:
#     login(username, password)
#     scrape_hashtag_posts(hashtag, num_posts=10)
# except Exception as e:
#     print("An error occurred:", e)
# finally:
#     driver.quit()
