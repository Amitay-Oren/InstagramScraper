from utils import scrape_hashtags_posts_from_file, scrape_users_posts_from_file, login, get_hashtags, get_username, get_password







# Main script
def main():
    
    hashtags = get_hashtags()
    print(hashtags)
    
    username = get_username()
    password = get_password()

        
    login(username, password)

    scrape_hashtags_posts_from_file(hashtags, num_posts=10)
    # scrape_user_posts(user_profile, num_posts=10)

   


if __name__ == "__main__":
    main()
