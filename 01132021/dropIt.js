// Given the array arr, iterate through and remove each element starting from the first element (the 0 index) until the function func returns true when the iterated element is passed through it.

// Then return the rest of the array once the condition is satisfied, otherwise, arr should be returned as an empty array.

// Link to problem:
// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/drop-it

function dropElements(arr, func) {
    let index;
    for(let i = 0; i < arr.length; i++){
      if(func(arr[i]) === true){
        index = arr.indexOf(arr[i]);
        break;
      }
      index = arr.length;
    }
  
    for (let j = 0; j < index; j++){
      arr.shift();
    }
    return arr;
  }
  
dropElements([1, 2, 3], function(n) {return n < 3; });