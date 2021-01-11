// Convert the characters &, <, >, " (double quote), and ' (apostrophe), in a string to their corresponding HTML entities.

// Link to problem: 
// https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/convert-html-entities

function convertHTML(str) {
    for(let i = 0; i< str.length; i++){
      switch(str[i]){
        case '&':
        str = str.replace(str[i], "&amp;")
        break;
        case '<':
        str = str.replace(str[i], "&lt;")
        break;
        case '>':
        str = str.replace(str[i], "&gt;")
        break;
        case '"':
        str = str.replace(str[i], "&quot;")
        break;
        case "'":
        str = str.replace(str[i], "&apos;")
        break;
  
      }
    }
    return str;
  }
  
convertHTML("Dolce & Gabbana");