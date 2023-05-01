import requests
from bs4 import BeautifulSoup

url = 'https://www.dictionary.com/browse/adulate'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#example_section = soup.find_all('div', {'class': 'default-content'})
example_section = soup.find('div', {'id':'examples-section'})
example_sentences = example_section.find_all('li')

for sentence in example_sentences[:5]:
    print(sentence.find('p').text.strip())

if len(example_sentences) < 5:
    print('Unable to find 5 sentences')
