// Return the number of total permutations of the provided string that don't have repeated consecutive letters. Assume that all characters in the provided string are each unique.

// For example, aab should return 2 because it has 6 total permutations (aab, aab, aba, aba, baa, baa), but only 2 of them (aba and aba) don't have the same letter (in this case a) repeating.

// Link to problem:
// https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/no-repeats-please

function permAlone(str) {
    let arr = str.split("");
    let perms = [];
    let tmp;
  
    let regex = /(.)\1+/;
  
    if(str.match(regex) !== null && str.match(regex)[0] === str) return 0;
  
    let swap = (i1, i2) => {
      tmp = arr[i1];
      arr[i1] = arr[i2];
      arr[i2] = tmp;
    }
  
    let heapsAlgorithm = (int) => {
      if (int === 1){
        perms.push(arr.join(""));
      }
      else{
        for(let i = 0; i != int; ++i){
          heapsAlgorithm(int - 1);
          swap(int % 2 ? 0 : i, int - 1);
        }
      }
    }
  
    heapsAlgorithm(arr.length);
  
    let filtered = perms.filter((string) => {
      return !string.match(regex);
    });
  
    return filtered.length;
  }
  
permAlone('aab');