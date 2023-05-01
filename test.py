import requests
from bs4 import BeautifulSoup
import os
import time
import json

data = []

url = "https://www.vocabulary.com/lists/156644"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

word_entries = soup.find_all("li", class_="entry learnable")

if not os.path.exists("assets"):
    os.makedirs("assets")

for entry in word_entries:
    word_link = entry.find("a", class_="word")
    if word_link:
        word_url = "https://www.vocabulary.com" + word_link["href"]
        while True:
            try:
                word_response = requests.get(word_url)
                word_soup = BeautifulSoup(word_response.content, "html.parser")
                break
            except:
                print("Retrying...")
                time.sleep(30)
        
        word = word_soup.find("h1", id="hdr-word-area").get_text().strip()
        print(word)
        meaning = entry.find("div", class_="definition").get_text().strip()
        additional_information = word_soup.find("p", class_="short").get_text().strip()
        more_information = word_soup.find("p", class_="long").get_text().strip()
        
        # Get the audio file
        audio_link = "https://s3.amazonaws.com/audio.vocabulary.com/1.0/us/" + word_soup.find("a", class_="audio")["data-audio"]+".mp3"
        while True:
            try:
                audio_data = requests.get(audio_link).content
                break
            except:
                print("Retrying...")
                time.sleep(30)
        # audio_data = requests.get(audio_link).content
        with open(os.path.join("assets", f"{word}.mp3"), "wb") as f:
            f.write(audio_data)
        
        # Get the synonyms and antonyms
        syn_url = f'https://www.merriam-webster.com/thesaurus/{word}'
        while True:
            try:
                syn_response = requests.get(syn_url)
                syn_soup = BeautifulSoup(syn_response.text, 'html.parser')
                break
            except:
                print("Retrying...")
                time.sleep(30)
        #syn_response = requests.get(syn_url)


        # get the top 5 synonyms
        try:
            synonyms_container = syn_soup.select_one('.thes-list-content.synonyms_list')
            if synonyms_container:
                synonyms = synonyms_container.find_all('a')[:5]
                top_synonyms = [syn.text.strip() for syn in synonyms]
            else:
                top_synonyms = []
        except:
            top_synonyms = []
        # get the top 5 antonyms
        try:
            antonyms_container = syn_soup.select_one('.opp-list-scored-container')
            if antonyms_container:
                antonyms = antonyms_container.find_all('a')[:5]
                top_antonyms = [ant.text.strip() for ant in antonyms]
            else:
                top_antonyms = []
        except:
            top_antonyms = []

        # Get 5 example sentences on dictionary.com

        sentence_url = f"https://www.dictionary.com/browse/{word}"
        while True:
            try:
                sentence_response = requests.get(sentence_url)
                sentence_soup = BeautifulSoup(sentence_response.text, 'html.parser')
                break
            except:
                print("Retrying...")
                time.sleep(30)
        #sentence_response = requests.get(sentence_url)
        #sentence_soup = BeautifulSoup(sentence_response.text, 'html.parser')
        
        #example_section = sentence_soup.find('div', {'class': 'default-content'})
        try:
            example_section = sentence_soup.find('div', {'id':'examples-section'})
            example_sentences = example_section.find_all('li')
            sentences = []
            for sentence in example_sentences[:5]:
                #print(sentence.find('p').text.strip())
                sentences.append(sentence.find('p').text.strip())

            if len(example_sentences) < 5:
                print('Unable to find 5 sentences')
        except:
            sentences = []

        print("Word:", word)
        # print("Meaning:", meaning)
        # print("Synonyms:", top_synonyms)
        # print("Antonyms:", top_antonyms)
        # print("Additional_Information:", additional_information)
        # print("More_Information:", more_information)
        # print("Audio:", os.path.join("assets", f"{word}.mp3"))
        # for sentence in sentences:
        #    print(f"- {sentence}")
        # print("\n")

        word_data = {
        'Word': word,
        'Meaning': meaning,
        'Synonyms': ','.join(top_synonyms),
        'Antonyms': ','.join(top_antonyms),
        'Additional_Information': additional_information,
        'More_Information': more_information,
        'Audio': os.path.join("assets", f"{word}.mp3"),
        'Example_sentences': sentences
        }
        data.append(word_data)


        # sleep for 15 seconds


        time.sleep(15)

with open('data.json', 'w') as f:
    json.dump(data, f)