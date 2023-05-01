// Load the JSON file using jQuery's getJSON function
$.getJSON("data.json", function(data) {
    // Define a function to generate ten random words from the data
    function generateWords() {
      // Shuffle the data array to randomize the order of words
      const shuffledData = data.sort(() => 0.5 - Math.random());
      // Select the first ten words from the shuffled array
      const randomWords = shuffledData.slice(0, 10);
      
      // Generate HTML for the ten random words
      const wordsHTML = randomWords.map(function(word) {
        return `
          <h2>${word.Word}</h2>
          <p>${word.Meaning}</p>
          <p><strong>Synonyms:</strong> ${word.Synonyms}</p>
          <p><strong>Antonyms:</strong> ${word.Antonyms}</p>
          <p>${word.Example_sentences[0].replace(word.Word, '<strong>'+word.Word+'</strong>')}</p>
          <audio controls><source src="${word.Audio}" type="audio/mpeg"></audio>
        `;
      }).join("");
      // Update the words container with the generated HTML
      $("#words").html(wordsHTML);
    }
    // Attach the generateWords function to the button click event
    $("button").click(generateWords);
  });
  