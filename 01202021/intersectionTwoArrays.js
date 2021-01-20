// Given two arrays, write a function to compute their intersection.

// Example 1:

// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2,2]
// Example 2:

// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [4,9]
// Note:

// Each element in the result should appear as many times as it shows in both arrays.
// The result can be in any order.

// Link to problem: 
// https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/674/

var intersect = function(nums1, nums2) {
    let inter = [];
    for(let i = 0; i < nums2.length; i++){
        if(nums1.includes(nums2[i])){
            inter.push(nums2[i]);
            nums1.splice(nums1.indexOf(nums2[i]), 1)
        }
    }
    return inter;
};