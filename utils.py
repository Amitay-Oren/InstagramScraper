from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import json

import datetime
from datetime import date
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
    time.sleep(1)
    password_field.send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(5)

#-----------------Scrape by user----------------------


# Function to scrape all post links from a user's profile
def scrape_user_posts(user_profile, num_posts):
    
    try:
        driver.get(f"https://www.instagram.com/{user_profile}/")
        # Wait until the first post link is visible
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/p/')]")))
    except Exception as err:
        print(f"Error accessing user profile: {user_profile}. The error: {err}")

    time.sleep(3)
    start_date = date(2023, 10, 26)
    start_datetime = datetime.datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0)

    post_links = set()

    while len(post_links) < num_posts and len(post_links) < 90:
        
        post_elements = driver.find_elements(By.XPATH, "//a[contains(@href,'/p/')]")
        time.sleep(2)
        for post_element in post_elements:
            
            try:
                time.sleep(2)
                post_date = get_post_date(post_element.get_attribute("href"))
                time.sleep(2)
            except Exception as e:
                print(f"Error getting post date. The error: {e}")
                continue

            if start_datetime <= post_date:
                post_links.add(post_element.get_attribute("href"))

        # Scroll down to load more posts
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # Save post links to CSV file
    with open('instagram_post_links_user.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Post Link'])
        writer.writerows([[post_link] for post_link in post_links])


def scrape_users_posts_from_file(users, num_posts):

    for user in users:
        scrape_user_posts(user, num_posts)


#-----------------Scrape by hashtag--------------------
def scrape_hashtag_posts(hashtag, num_posts=10):

    print("===============" + hashtag + "===============")
    try:
        driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
        # Wait until the first post link is visible
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/p/')]")))
    except Exception as e:
        print(f"Error accessing hashtag: {hashtag}. The error: {e}")
        return
    time.sleep(5)

    post_links = set()
    start_date = date(2023, 10, 7)
    end_date = date(2023,10, 27)
    start_datetime = datetime.datetime(start_date.year, start_date.month, start_date.day, 0, 0, 0)
    end_datetime = datetime.datetime(end_date.year, end_date.month, end_date.day, 0, 0, 0)

    print(len(post_links))
    
    links = driver.find_elements(By.XPATH, "//a[contains(@href,'/p/')]")
    for link in links:
        try:
            post_date = get_post_date(link.get_attribute("href"))

        except Exception as e:
            print(f"Error getting post date. The error: {e}")
            continue

        if start_datetime <= post_date <= end_datetime:
            post_links.add(link.get_attribute("href"))
            print(post_links)
            
        print(len(post_links))
            
        if len(post_links) >= num_posts:
            print(post_links)
            break
            
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    save_post_links_to_csv_file(post_links, hashtag)



def scrape_hashtags_posts_from_file(hashtags, num_posts):

    for hashtag in hashtags:  
        scrape_hashtag_posts(hashtag, num_posts)





# -----------------helper functions------------

def get_post_date(post_link):
    driver_post_date = webdriver.Chrome()
    # time.sleep(10)
    # Navigate to the post link using the driver
    driver_post_date.get(post_link)
    time.sleep(10)

    # Find the time element using its class
    time_element = driver_post_date.find_element(By.CLASS_NAME, "_aaqe")
    print(time_element)
    datetime_value = time_element.get_attribute("datetime")
    print(datetime_value)
    # Convert the date text to a datetime object
    datetime_obj = datetime.datetime.fromisoformat(datetime_value[:-14])

    # date_time_obj_1 = convert_string_to_datetime(datetime_value)
    print(datetime_obj)


    #return datetime_obj
    return datetime_obj

def save_post_links_to_csv_file(post_links, hashtag):
    # Save post links to CSV file
    with open('instagram_post_links.csv', mode='a', encoding='utf-8', newline='') as file:
        try:
            writer = csv.writer(file)
            writer.writerow(['========' + hashtag + '========'])
            writer.writerows([[post_link] for post_link in post_links])
        except Exception as e:
            print(f"Error saving post links to CSV file. The error: {e}")

def get_hashtags():
    with open('against_hashtags.txt', 'r', encoding='utf-8') as f:
        hashtags = f.readlines()
    hashtags = [hashtag.strip() for hashtag in hashtags]

    return hashtags

def get_users():
    with open('users.txt', 'r', encoding='utf-8') as f:
        users = f.readlines()
    users = [user.strip() for user in users]

    return users

def get_username():
    try:
        # Load credentials from credential.json
        with open('credentials.json') as f:
            credentials = json.load(f)

        # Extract username and password
        username = credentials['username']
    except Exception as e:
        print("An error occurred while trying the username from credentials.json:", e)

    return username

def get_password():
    try:
        # Load credentials from credential.json
        with open('credentials.json') as f:
            credentials = json.load(f)

        # Extract username and password
        password = credentials['password']
    except Exception as e:
        print("An error occurred while trying the username from credentials.json:", e)
        
    return password


