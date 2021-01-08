// Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.

// Link to problem:
// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/spinal-tap-case

function spinalCase(str) {
    let re1 = /([a-z])([A-Z])/g;
    let re2 = /\s+|_+/g;
    str = str.replace(re1, "$1 $2").replace(re2, "-").toLowerCase();
    return str;
  }
  
  console.log(spinalCase('ThisIsSpinalTap'));