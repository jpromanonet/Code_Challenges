// Appending variables to strings.

// Example
var anAdjective = "awesome!";
var ourStr = "freeCodeCamp is ";
ourStr += anAdjective;

// Only change code below this line

var someAdjective = 'is super fun!';
var myStr = "Learning to code is ";
myStr += someAdjective;

//-----------------------------------------------------------------------------------------------

// Find the length of a string

// Example
var firstNameLength = 0;
var firstName = "Ada";

firstNameLength = firstName.length;

// Setup
var lastNameLength = 0;
var lastName = "Lovelace";

// Only change code below this line.

lastNameLength = lastName.length;

//-----------------------------------------------------------------------------------------------

// Index 0 

// Example
var firstLetterOfFirstName = "";
var firstName = "Ada";

firstLetterOfFirstName = firstName[0];

// Setup
var firstLetterOfLastName = "";
var lastName = "Lovelace";

// Only change code below this line
firstLetterOfLastName = lastName[0];

//-----------------------------------------------------------------------------------------------

// Understand string inmutability

// Setup
var myStr = "Jello World";

// Only change code below this line

myStr = "Hello World"; // Fix Me

//-----------------------------------------------------------------------------------------------

// Use Bracket Notation to Find the Nth Character in a String

// Example
var firstName = "Ada";
var secondLetterOfFirstName = firstName[1];

// Setup
var lastName = "Lovelace";

// Only change code below this line.
var thirdLetterOfLastName = lastName[2];

//-----------------------------------------------------------------------------------------------

// Use Bracket Notation to Find the Last Character in a String

// Example
var firstName = "Ada";
var lastLetterOfFirstName = firstName[firstName.length - 1];

// Setup
var lastName = "Lovelace";

// Only change code below this line.
var lastLetterOfLastName = lastName[lastName.length -1];

//-----------------------------------------------------------------------------------------------

// Use Bracket Notation to Find the Nth-to-Last Character in a String

// Example
var firstName = "Ada";
var thirdToLastLetterOfFirstName = firstName[firstName.length - 3];

// Setup
var lastName = "Lovelace";

// Only change code below this line
var secondToLastLetterOfLastName = lastName[lastName.length - 2];

//-----------------------------------------------------------------------------------------------

// Word Blanks

function wordBlanks(myNoun, myAdjective, myVerb, myAdverb) {
    // Your code below this line
    var result = "The " + myAdjective + " " + myNoun + " " + myVerb + " " + myAdverb;
  
    // Your code above this line
    return result;
  }
  
  // Change the words here to test your function
  wordBlanks("dog", "big", "ran", "quickly");

//-----------------------------------------------------------------------------------------------

// Store Multiple Values in one Variable using JavaScript Arrays

// Example
var ourArray = ["John", 23];

// Only change code below this line.
var myArray = ["Paul", 25];

//-----------------------------------------------------------------------------------------------

// Multidimensional array

// Example
var ourArray = [["the universe", 42], ["everything", 101010]];

// Only change code below this line.
var myArray = [["The Light", 300000], ['Mars', 2033]];

//-----------------------------------------------------------------------------------------------

// Access Array Data With Indexes

// Example
var ourArray = [50,60,70];
var ourData = ourArray[0]; // equals 50

// Setup
var myArray = [50,60,70];

// Only change code below this line.
var myData = myArray[0];

//-----------------------------------------------------------------------------------------------

// Modify Array Data With Indexes

// Example
var ourArray = [18,64,99];
ourArray[1] = 45; // ourArray now equals [18,45,99].

// Setup
var myArray = [18,64,99];

// Only change code below this line.
myArray[0] = 45;

//-----------------------------------------------------------------------------------------------

// Access Multi-Dimensional Arrays With Indexes

// Setup
var myArray = [[1,2,3], [4,5,6], [7,8,9], [[10,11,12], 13, 14]];

// Only change code below this line.
var myData = myArray[2][1];