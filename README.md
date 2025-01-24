# James Beard Award Winners & Nominees Scraper

This Python app scrapes the list of James Beard Award Winners & Nominees from the offical James Beard website. Using it you can collect data on restaurants & chefs from their website as a JSON file.

### Features
- Scrapes the James Beard Awards website for nominees and winners in the "Restaurant & Chef" category.
- Extracts key details such as the nominee's name, restaurant, location, award category, level, and year.
- Saves the scraped data in a JSON file for further use.

### Prerequisits 
- Python 3.x
- Required Python libraries:
    - requests: to send HTTP requests
    - beautfulsoup4: for parsing HTML and extracting information

Install the required libraries using:
```pip install requests beautifulsoup4```

### How to Use
1. Clone or download this repository.
2. Ensure Python and the required libraries are installed.
3. Run the script: ```python scraper.py```
4. The script will generate a JSON file named jb-restaurants-&-chefs.json containing the scraped data.

### Scraped Data Structure
The JSON output is a list of dictionaries, where each dictionary contains the following keys:

- name: Name of the nominee or winner.
- restaurant (if given): Name of the associated restaurant.
- location: Location of the nominee or restaurant.
- category: Award category.
- level: Award level (e.g., finalist or winner).
- year: Year of the award.

Example entry:
```
    {
        "name": "Kristina Liedags Compton",
        "restaurant": "Hilda and Jesse",
        "location": "San Francisco, California",
        "category": "Restaurant & Chef",
        "level": "Semifinalist",
        "year": "2024"
    },
```

### Notes
- The script scrapes publicly available information from the James Beard Awards website.
- Use the scraper responsibly and in accordance with the website's terms of use.
- If the website structure changes, the script may require updates.
