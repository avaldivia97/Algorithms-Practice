// Given a positive integer num, return the sum of all odd Fibonacci numbers that are less than or equal to num.

// The first two numbers in the Fibonacci sequence are 1 and 1. Every additional number in the sequence is the sum of the two previous numbers. The first six numbers of the Fibonacci sequence are 1, 1, 2, 3, 5 and 8.

// For example, sumFibs(10) should return 10 because all odd Fibonacci numbers less than or equal to 10 are 1, 1, 3, and 5.

// Link to problem:
// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/sum-all-odd-fibonacci-numbers

function sumFibs(num) {
    let sum = 0;
    if(num < 0){
      return sum;
    }
    let fibNums = [1, 1];
    while((fibNums[0] + fibNums[1]) <= num){
      fibNums.unshift(fibNums[0] + fibNums[1])
    }
    for(let i = 0; i < fibNums.length; i++){
      if(fibNums[i] % 2 === 1){
        sum+=fibNums[i];
      }
    }
    return sum;
  }
  
sumFibs(75025);