// Find the smallest common multiple of the provided parameters that can be evenly divided by both, as well as by all sequential numbers in the range between these parameters.

// The range will be an array of two numbers that will not necessarily be in numerical order.

// For example, if given 1 and 3, find the smallest common multiple of both 1 and 3 that is also evenly divisible by all numbers between 1 and 3. The answer here would be 6.

// Link to problem:
// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/smallest-common-multiple

function smallestCommons(arr) {
    let range = [];
    
    for(let i = Math.max(arr[0], arr[1]); i >= Math.min(arr[0],arr[1]); i--){
    range.push(i);
    }
  
    let GCD = (x, y) =>{
      if (y === 0) return x;
      else return GCD(y, x % y);
    }
  
    let solution = range[0];
    for(let i = 1; i < range.length;i++){
      let gcd = GCD(solution, range[i]);
      solution = solution * range[i] / gcd
    }
    return solution;
  }
  
  
smallestCommons([1, 5]);