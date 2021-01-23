// Return an English translated sentence of the passed binary string.

// The binary string will be space separated.

// Link to problem:
// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/binary-agents

function binaryAgent(str) {
    let binaryArr = str.split(" ");
    let charArr = [];
    binaryArr.forEach(element => {
      element = String.fromCharCode(parseInt(element, 2));
      charArr.push(element);
    });
    str = charArr.join('');
    return str;
  }
  
binaryAgent("01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111");