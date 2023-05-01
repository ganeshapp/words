// Function to play the audio file
function playAudio(audioPath) {
    const audio = new Audio(audioPath);
    audio.play();
  }
  
  // Select the word list element
  const wordList = document.querySelector('.word-list');
  
  // Load the JSON data
  fetch('data.json')
    .then(response => response.json())
    .then(data => {
      // Shuffle the array of words
      const shuffledWords = data.sort(() => Math.random() - 0.5);
  
      // Take the first 10 words
      const selectedWords = shuffledWords.slice(0, 10);
      // Loop through each selected word
      selectedWords.forEach(word => {
        // Create a new list item for the word
        const wordItem = document.createElement('li');
  
        wordItem.classList.add('word-card');
        // Create the word text with audio icon
        const wordText = document.createElement('span');
        wordText.classList.add('word-text');
        //alert(word.Additional_Information)
       
  
        // Add the word text
        const wordSpan = document.createElement('span');
        wordSpan.textContent = ` ${word.Word}`;
        wordText.appendChild(wordSpan);

         // Create the audio icon
         const audioIcon = document.createElement('i');
         audioIcon.classList.add('fa', 'fa-volume-up', 'audio-icon');
         audioIcon.addEventListener('click', () => playAudio(word.Audio));
         wordText.appendChild(audioIcon);
  
        // Add the word text to the list item
        wordItem.appendChild(wordText);
  
        // Add the meaning
        const meaning = document.createElement('p');
        meaning.textContent = `${word.Meaning}`;
        wordItem.appendChild(meaning);
  
        // Add the synonyms (if any)
        if (word.Synonyms) {
        // create an element for the synonyms and add it to the word item. The header synonyms must be bold

        const synonyms = document.createElement('p');
        synonyms.innerHTML = `<strong>Synonyms:</strong>  ${word.Synonyms.replaceAll(',', ', ')}`;
        wordItem.appendChild(synonyms);
        }
  
        // Add the antonyms (if any)
        if (word.Antonyms) {
          const antonyms = document.createElement('p');
          antonyms.innerHTML = `<strong>Antonyms:</strong> ${word.Antonyms.replaceAll(',', ', ')}`;
          wordItem.appendChild(antonyms);
        }
  
        // Add the example sentences (if any)
        if (word.Example_sentences) {
        
          const examples = document.createElement('p');
          examples.innerHTML = '<strong>Example Sentences:</strong>';
          word.Example_sentences.forEach(example => {
            const exampleItem = document.createElement('p');
            exampleItem.innerHTML = example.replaceAll(word.Word, `<strong>${word.Word}</strong>`);
            examples.appendChild(exampleItem);
          });
          wordItem.appendChild(examples);
        }

        const additionalInfo = word.Additional_Information.replaceAll(word.Word, `<strong>${word.Word}</strong>`);
        const moreInfo = word.More_Information.replaceAll(word.Word, `<strong>${word.Word}</strong>`);


        // Add the additional information (if any)
        wordItem.addEventListener('mouseover', () => {
            const hoverCard = document.createElement('div');
            hoverCard.classList.add('hover-card');
            const hoverCardContent = document.createElement('div');
            hoverCardContent.classList.add('hover-card-content');
            const additionalInfoElement = document.createElement('p');
            additionalInfoElement.innerHTML = additionalInfo;
            hoverCardContent.appendChild(additionalInfoElement);
            if (moreInfo) {
              const moreInfoElement = document.createElement('p');
              moreInfoElement.innerHTML = '<br /><strong>More Info: </strong>'+moreInfo;
              hoverCardContent.appendChild(moreInfoElement);
            }
            hoverCard.appendChild(hoverCardContent);
            wordItem.appendChild(hoverCard);
          });

          wordItem.addEventListener('mouseout', () => {
            const hoverCard = wordItem.querySelector('.hover-card');
            hoverCard.remove();
          });
  
        // Add the list item to the word list
        wordList.appendChild(wordItem);
      });
    })
    .catch(error => console.error(error));


  

