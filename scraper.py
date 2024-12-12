import requests
from bs4 import BeautifulSoup
import json
# pip install requests
# pip install beautifulsoup4


results_in_dict_list = []

for page in range(1, 101):
    url = f'https://www.jamesbeard.org/awards/search?keyword=&year=&categories%5BRestaurant+%26+Chef%5D=1&page={page}'
    r = requests.get(url)
    r.raise_for_status()

    soup = BeautifulSoup(r.content, 'html.parser')

    results = soup.find('div', class_="c-results c-results--awards")
    if not results:
        break

    result_list = results.find_all("div", class_="c-award-recipient")

    for result_item in result_list:
        nominee = {}
        name = result_item.find(
            "p", class_="c-award-recipient__name").text.strip()
        award_details = result_item.find_all(
            "p", class_="c-award-recipient__text")

        award = award_details[0]
        if len(award_details) == 5:
            nominee["name"] = name
            nominee["location"] = award_details[1].text.strip()
            nominee["category"] = award_details[2].text.strip()
            nominee["level"] = award_details[3].text.strip()
            nominee["year"] = award_details[4].text.strip()
        elif len(award_details) == 6:
            nominee["name"] = name
            nominee["restaurant"] = award_details[1].text.strip()
            nominee["location"] = award_details[2].text.strip()
            nominee["category"] = award_details[3].text.strip()
            nominee["level"] = award_details[4].text.strip()
            nominee["year"] = award_details[5].text.strip()

        results_in_dict_list.append(nominee)
        # This only saves results where chefs won for a particular restaurant or a
        # restaurant won for a particular category

with open('jb-restaurants-&-chefs.json', 'w') as file:
    json.dump(results_in_dict_list, file, indent=4)

print(f"Total results scraped: {len(results_in_dict_list)}")
