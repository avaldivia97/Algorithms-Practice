// We'll pass you an array of two numbers. Return the sum of those two numbers plus the sum of all 
// the numbers between them. The lowest number will not always come first.

// For example, sumAll([4,1]) should return 10 because sum of all the numbers between 1 and 4 (both
// inclusive) is 10.

// Link to problem 
// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/sum-all-numbers-in-a-range

function sumAll(arr) {
    let greater, lower;
    let sum = 0;
    if(arr[0] > arr[1]){
      greater = arr[0];
      lower = arr[1];
    }
    else{
      greater = arr[1];
      lower = arr[0];
    }
    for (let x = lower; x <= greater; x++){
      sum+=x;
    }
    return sum;
  }
  
  sumAll([1, 4]);