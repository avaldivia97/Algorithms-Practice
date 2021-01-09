// The DNA strand is missing the pairing element. Take each character, get its pair, and return the results as a 2d array.

// Base pairs are a pair of AT and CG. Match the missing element to the provided character.

// Return the provided character as the first element in each array.

// For example, for the input GCG, return [["G", "C"], ["C","G"],["G", "C"]]

// The character and its pair are paired up in an array, and all the arrays are grouped into one encapsulating array.

// Link to problem:
// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/dna-pairing

function pairElement(str) {
    let pairs = [];
    for(let c = 0; c< str.length; c++){
      if(str[c] === "A") {pairs.push(["A", "T"])}
      else if(str[c] === "T") {pairs.push(["T", "A"])}
      else if(str[c] === "G") {pairs.push(["G", "C"])}
      else if(str[c] === "C") {pairs.push(["C", "G"])}
    }
    return pairs;
  }
  
pairElement("GCG");