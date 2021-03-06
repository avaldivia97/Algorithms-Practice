// Make a function that looks through an array of objects (first argument) and returns an array of 
// all objects that have matching name and value pairs (second argument). Each name and value pair 
// of the source object has to be present in the object from the collection if it is to be included 
// in the returned array.

// For example, if the first argument is [{ first: "Romeo", last: "Montague" }, { first: "Mercutio", 
// last: null }, { first: "Tybalt", last: "Capulet" }], and the second argument is { last: "Capulet" }, 
// then you must return the third object from the array (the first argument), because it contains the 
// name and its value, that was passed on as the second argument.

// Link to problem
// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/wherefore-art-thou

function whatIsInAName(collection, source) {
    var arr = [];
    // Only change code below this line
    let keys = Object.keys(source);
    arr =  collection.filter((object) => {
      return keys.every(key => {
        if (object.hasOwnProperty(key) && object[key] === source[key]){
          return true;
        }
        return false;
      })
      })
  
    return arr;
  }
  
console.log(whatIsInAName([{ "apple": 1, "bat": 2 }, { "apple": 1 }, { "apple": 1, "bat": 2, "cookie": 2 }], { "apple": 1, "cookie": 2 }));