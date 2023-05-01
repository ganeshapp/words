import requests
from bs4 import BeautifulSoup

url = 'https://www.merriam-webster.com/thesaurus/wheedle'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# get the top 5 synonyms
synonyms_container = soup.select_one('.thes-list-content.synonyms_list')
if synonyms_container:
    synonyms = synonyms_container.find_all('a')[:5]
    top_synonyms = [syn.text.strip() for syn in synonyms]
else:
    top_synonyms = []

# get the top 5 antonyms
antonyms_container = soup.select_one('.opp-list-scored-container')
if antonyms_container:
    antonyms = antonyms_container.find_all('a')[:5]
    top_antonyms = [ant.text.strip() for ant in antonyms]
else:
    top_antonyms = []

print("Top 5 synonyms for 'zenith':", top_synonyms)
print("Top 5 antonyms for 'zenith':", top_antonyms)