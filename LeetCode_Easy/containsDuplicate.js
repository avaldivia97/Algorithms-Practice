// Given an array of integers, find if the array contains any duplicates.

// Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

// Example 1:

// Input: [1,2,3,1]
// Output: true
// Example 2:

// Input: [1,2,3,4]
// Output: false
// Example 3:

// Input: [1,1,1,3,3,4,3,2,4,2]
// Output: true

// Link to problem:
// https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/

var containsDuplicate = function(nums) {
    let duplicates = false;
    if(nums.length === 0 || nums.length === 1) return duplicates;
    nums.forEach((element, index) => {
        if(nums.indexOf(element) !== index){
            duplicates = true;
        }
    })
    return duplicates;
};