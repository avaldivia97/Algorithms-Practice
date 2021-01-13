// Flatten a nested array. You must account for varying levels of nesting.

// Link to problem:
// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/steamroller

function steamrollArray(arr, steamrolled = []) {
    arr.forEach((element) => {
      if(Array.isArray(element)){
        steamrollArray(element, steamrolled)
      }
      else{
        steamrolled.push(element);
      }
    })
    return steamrolled;
  }
  
steamrollArray([1, [2], [3, [[4]]]]);