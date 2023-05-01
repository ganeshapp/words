# A python program to download the lsit of words from vocabulary.com list available at https://www.vocabulary.com/lists/156644 and save it in a file

import requests
from bs4 import BeautifulSoup

# The url of the list
url = "https://www.vocabulary.com/lists/156644"

# The file to save the list
file = "list.txt"

# The request
r = requests.get(url)

# The soup
soup = BeautifulSoup(r.text, "html.parser")
print("hi")
# The list of words

words = soup.find_all("a", {"class": "word dynamictext"})
print(words)
words = [word.text for word in words]
print(words)

# The list of definitions
definitions = soup.find_all("div", {"class": "definition"})
definitions = [definition.text for definition in definitions]

# The list of examples
examples = soup.find_all("div", {"class": "example"})
examples = [example.text for example in examples]

# The list of synonyms
synonyms = soup.find_all("div", {"class": "synonyms"})
synonyms = [synonym.text for synonym in synonyms]

# The list of antonyms
antonyms = soup.find_all("div", {"class": "antonyms"})
antonyms = [antonym.text for antonym in antonyms]

# The list of word types
word_types = soup.find_all("span", {"class": "partofspeech"})
word_types = [word_type.text for word_type in word_types]
for i in range(len(words)):
    print(words[i] + " - " + word_types[i] + definitions[i] + examples[i] + synonyms[i] + antonyms[i])

# Save the list in a file
'''
with open(file, "w") as f:
    for i in range(len(words)):
        f.write(words[i] + " - " + word_types[i] + definitions[i] + examples[i] + synonyms[i] + antonyms[i])
'''
