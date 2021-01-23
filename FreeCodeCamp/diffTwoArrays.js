// Compare two arrays and return a new array with any items only found in one of the two given arrays, 
// but not both. In other words, return the symmetric difference of the two arrays.

// Note
// You can return the array with its elements in any order.

// Link to problem:
// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/diff-two-arrays\

function diffArray(arr1, arr2) {
    let newArr = arr1.concat(arr2);
    newArr = newArr.filter(item => !arr1.includes(item) || !arr2.includes(item));
    return newArr;
  }
  
  diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]);