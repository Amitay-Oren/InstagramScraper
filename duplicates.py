import csv
from collections import Counter

# Function to check for duplicate post links in a CSV file
def check_duplicate_links(file_path):
    post_links = []
    with open(file_path, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            post_links.extend(row)

    # Count the occurrences of each post link
    link_counts = Counter(post_links)

    # Find and print duplicate post links
    duplicates = {link: count for link, count in link_counts.items() if count > 1}
    if duplicates:
        print(f"Duplicate post links found in {file_path}:")
        for link, count in duplicates.items():
            print(f"Link: {link}, Occurrences: {count}")
    else:
        print(f"No duplicate post links found in {file_path}")

# List of CSV files to check for duplicates
csv_files = [
    r'C:\Users\amita\InstagramScraper\instaenv\instagram_user_posts.csv',
]
# Check for duplicate post links in each CSV file
for file_path in csv_files:
    check_duplicate_links(file_path)
