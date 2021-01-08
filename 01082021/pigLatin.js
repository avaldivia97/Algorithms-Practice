// Pig Latin is a way of altering English Words. The rules are as follows:
// -If a word begins with a consonant, take the first consonant or consonant cluster, move it to the end of the word, and add "ay" to it.
// -If a word begins with a vowel, just add "way" at the end.
// Translate the provided string to Pig Latin. Input strings are guaranteed to be English words in all lowercase.

// Link to problem:
// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/pig-latin

function translatePigLatin(str) {
    if (str.match(/^[aeiou]/)){
      str = str + "way";
      return str; 
    }
    let consonants = str.match(/^[^aeiou]+/);
    str = str.slice(consonants[0].length)
    str = str + consonants[0] + "ay";
    return str;
  }
  
  console.log(translatePigLatin("eightway"));