// Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery. Update the current existing inventory item quantities (in arr1). If an item cannot be found, add the new item and quantity into the inventory array. The returned inventory array should be in alphabetical order by item.

// Link to problem:
// https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/inventory-update

function updateInventory(arr1, arr2) {
    let inventoryIndexOf = (array, item) => {
        for (let i = 0; i < array.length; i++){
            if (array[i][1] === item) return i;
        }
        return -1;
    }

    for (let j = 0; j < arr2.length; j++){
        let index = inventoryIndexOf(arr1, arr2[j][1]);
        if (index >= 0){
            arr1[index][0] = arr1[index][0] + arr2[j][0];
        }
        else arr1.push(arr2[j]);
    }

    arr1.sort((prev, next) => {
        if(prev[1] < next[1]) return -1;
        if(prev[1] > next[1]) return 1;
        else return 0;
    })

    return arr1;
}

// Example inventory lists
var curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
];

var newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
];

updateInventory(curInv, newInv);