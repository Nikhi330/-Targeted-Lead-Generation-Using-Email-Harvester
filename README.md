# -Targeted-Lead-Generation-Using-Email-Harvester


## Overview
This Python script scrapes emails from business directories, validates them, and stores valid emails in MongoDB. It is designed for targeted lead generation.

## Features
- Extracts emails from webpages using web scraping.
- Validates emails using `email-validator`.
- Stores unique, valid emails in MongoDB.

## Prerequisites
Ensure you have the following installed:

### Install Required Dependencies
Run the following command:
```bash
pip install requests beautifulsoup4 email-validator pymongo
```

### Install & Start MongoDB
#### Windows:
1. If MongoDB is installed as a service, start it using:
   ```bash
   net start MongoDB
   ```
2. Or run:
   ```bash
   mongod
   ```

#### Linux/macOS:
1. Start MongoDB with:
   ```bash
   sudo systemctl start mongod
   ```

## Running the Script
1. Save the script as `email_scraper.py`.
2. Run it using:
   ```bash
   python email_scraper.py
   ```

## Checking Stored Emails in MongoDB
Once the script runs successfully, open the MongoDB shell and use the following commands:
```bash
mongo
use LeadGeneration
db.Emails.find().pretty()
```
This will display the stored valid emails.

## Customizing the Script
- Replace `https://example.com` in the script with real business directory URLs.
- Modify MongoDB collection names as needed.

## Troubleshooting
### 1. `ModuleNotFoundError`
If any module is missing, install it using:
```bash
pip install <module_name>
```

### 2. `requests.exceptions.RequestException`
- Ensure the target website is accessible.
- Add headers in `requests.get()` to mimic a browser.

### 3. `MongoDB connection errors`
- Ensure MongoDB is running (`mongod` command).
- Verify the connection string in the script.

## License
This project is open-source and can be modified as needed.

---
Developed by Nikhil Pathak 🚀

