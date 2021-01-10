// Find the missing letter in the passed letter range and return it.

// If all letters are present in the range, return undefined.

// Link to problem:
// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/missing-letters

function fearNotLetter(str) {
    for(let c = 0; c < str.length; c++){
      if(str.charCodeAt(c+1) - str.charCodeAt(c) > 1){
        let missingChar = String.fromCharCode(str.charCodeAt(c) + 1);
        return missingChar;
      }
    }
    return undefined;
  }
  
fearNotLetter("abce");