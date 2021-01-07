// You will be provided with an initial array (the first argument in the destroyer function), 
// followed by one or more arguments. Remove all elements from the initial array that are of the same value as these arguments.

// Note
// You have to use the arguments object.

// Link to problem:
// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/seek-and-destroy

function destroyer(arr) {
    let indicesToBeDeleted = [];
    for (let c = 0; c < arguments[0].length; c++){
      for (let x = 1; x < arguments.length; x++){
        if (arguments[0][c] === arguments[x]){
          indicesToBeDeleted.push(c);
        }
      }
    }

    for (let c = 0; c < indicesToBeDeleted.length; c++){
      arguments[0].splice(indicesToBeDeleted[c], 1);
      for (let c = 0; c < indicesToBeDeleted.length; c++){
        indicesToBeDeleted[c] = indicesToBeDeleted[c] - 1;
      }
    }
    
    return arr;
  }
  
destroyer([1, 2, 3, 1, 2, 3], 2, 3);