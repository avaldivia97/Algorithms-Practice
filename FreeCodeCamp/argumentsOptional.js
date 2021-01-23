// Create a function that sums two arguments together. If only one argument is provided, then return a function that expects one argument and returns the sum.

// For example, addTogether(2, 3) should return 5, and addTogether(2) should return a function.

// Calling this returned function with a single argument will then return the sum:

// var sumTwoAnd = addTogether(2);

// sumTwoAnd(3) returns 5.

// If either argument isn't a valid number, return undefined.

// Link to problem:
// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/arguments-optional

function addTogether() {
    let isNum = (x) => {
      if (typeof x === "number") return true;
      else return false;
    }
  
    if (arguments.length === 2 && isNum(arguments[0]) && isNum(arguments[1])){
      return arguments[0] + arguments[1];
    }
  
    if (arguments.length === 1 && isNum(arguments[0])){
      let i = arguments[0];
      return function mySum(j){
        if (isNum(j)) return i + j;
      }
    }
    return undefined;
  }
  
addTogether(2, 3);