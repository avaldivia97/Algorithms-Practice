// Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

// Example:

// Input: [0,1,0,3,12]
// Output: [1,3,12,0,0]
// Note:

// You must do this in-place without making a copy of the array.
// Minimize the total number of operations.

// Link to problem:
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/

var moveZeroes = function(nums) {
    length = nums.length;
    for(let i = 0; i < length; i++){
        if(nums[i] === 0){
            nums.splice(i, 1);
            nums.push(0);
            i--;
            length--;
        }
    }
};