import requests
from bs4 import BeautifulSoup
import re
from email_validator import validate_email, EmailNotValidError
from pymongo import MongoClient

def scrape_emails(url):
    """Scrape emails from a given webpage URL."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        with requests.Session() as session:
            response = session.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        emails = set(re.findall(r'[\w\.-]+@[\w\.-]+', soup.text))
        return emails
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return set()

def validate_emails(emails):
    """Validate and filter out invalid emails."""
    valid_emails = set()
    for email in emails:
        try:
            valid = validate_email(email, check_deliverability=False)
            valid_emails.add(valid.email)
        except EmailNotValidError:
            continue
    return valid_emails

def save_to_mongodb(emails):
    """Store valid emails in MongoDB."""
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["LeadGeneration"]
        collection = db["Emails"]
        
        for email in emails:
            if not collection.find_one({"email": email}):  # Avoid duplicates
                collection.insert_one({"email": email})
        print("Emails successfully saved to MongoDB.")
    except Exception as e:
        print(f"MongoDB Error: {e}")

def main():
    urls = [
        "https://example.com",  # Replace with real business directory URLs
    ]
    
    all_emails = set()
    for url in urls:
        scraped_emails = scrape_emails(url)
        all_emails.update(scraped_emails)
    
    valid_emails = validate_emails(all_emails)
    print(f"Valid emails found: {valid_emails}")
    save_to_mongodb(valid_emails)

if __name__ == "__main__":
    main()
