// Passing Values to Functions with Arguments

// Example
function ourFunctionWithArgs(a, b) {
  console.log(a - b);
}
ourFunctionWithArgs(10, 5); // Outputs 5

// Only change code below this line.

function functionWithArgs(arg1, arg2) {
  console.log(arg1 + arg2);
}
functionWithArgs(7, 7); // Outputs 14

//---------------------------------------------------------------------------------------------------------------

// Global scope and Functions

// Declare your variable here
var myGlobal = 10;

function fun1() {
  // Assign 5 to oopsGlobal Here
  oopsGlobal = 5;
}

// Only change code above this line
function fun2() {
  var output = "";
  if (typeof myGlobal != "undefined") {
    output += "myGlobal: " + myGlobal;
  }
  if (typeof oopsGlobal != 5) {
    output += " oopsGlobal: " + oopsGlobal;
  }
  console.log(output);
}

//---------------------------------------------------------------------------------------------------------------

// Local Scope and Functions

function myLocalScope() {
  "use strict"; // you shouldn't need to edit this line
  var myVar;
  console.log(myVar);
}
myLocalScope();

// Run and check the console
// myVar is not defined outside of myLocalScope
// console.log(myVar);

// Now remove the console log line to pass the test

//---------------------------------------------------------------------------------------------------------------

// Global vs. Local Scope in Functions

// Setup
var outerWear = "T-Shirt";

function myOutfit() {
  // Only change code below this line
  var outerWear = "sweater";

  // Only change code above this line
  return outerWear;
}

myOutfit();

//---------------------------------------------------------------------------------------------------------------

// Return a Value from a Function with Return

// Example
function minusSeven(num) {
  return num - 7;
}

// Only change code below this line

function timesFive(num) {
  return num * 5;
}

console.log(timesFive(10));

//---------------------------------------------------------------------------------------------------------------

// Understanding Undefined Value returned from a Function

// Example
var sum = 0;
function addThree() {
  sum = sum + 3;
}

// Only change code below this line
var sum = 0;
function addFive() {
  sum = sum + 5;
}

// Only change code above this line
var returnedValue = addFive();

//---------------------------------------------------------------------------------------------------------------

// Assignment with a Returned Value

// Example
var changed = 0;

function change(num) {
  return (num + 5) / 3;
}

changed = change(10);

// Setup
var processed = 0;

function processArg(num) {
  return (num + 3) / 5;
}

// Only change code below this line

processed = processArg(7);

//---------------------------------------------------------------------------------------------------------------

// Stand in line

function nextInLine(arr, item) {
  // Your code here
  arr.push(item);
  var removed = arr.shift();

  return removed; // Change this line
}

// Test Setup
var testArr = [1, 2, 3, 4, 5];

// Display Code
console.log("Before: " + JSON.stringify(testArr));
console.log(nextInLine(testArr, 6)); // Modify this line to test
console.log("After: " + JSON.stringify(testArr));

//---------------------------------------------------------------------------------------------------------------

// Use Conditional Logic with If Statements

// Example
function ourTrueOrFalse(isItTrue) {
  if (isItTrue) {
    return "Yes, it's true";
  }
  return "No, it's false";
}

// Setup
function trueOrFalse(wasThatTrue) {
  // Only change code below this line.
  if (wasThatTrue === true) {
    return "Yes, that was true";
  } else {
    return "No, that was false";
  }

  // Only change code above this line.
}

// Change this value to test
trueOrFalse(true);

//---------------------------------------------------------------------------------------------------------------

// Comparison with the Equality Operator

// Setup
function testEqual(val) {
    if (val == 12) { // Change this line
      return "Equal";
    }
    return "Not Equal";
  }
  
  // Change this value to test
  testEqual(10);

//---------------------------------------------------------------------------------------------------------------

// Comparison with the Strict Equality Operator

// Setup
function testStrict(val) {
    if (val === 7) { // Change this line
      return "Equal";
    }
    return "Not Equal";
  }
  
  // Change this value to test
  testStrict(10);

//---------------------------------------------------------------------------------------------------------------

// Practice comparing different values

// Setup
function compareEquality(a, b) {
    if (a === b) { // Change this line
      return "Equal";
    }
    return "Not Equal";
  }
  
  // Change this value to test
  compareEquality(10, "10");

//---------------------------------------------------------------------------------------------------------------

// Comparison with the Inequality Operator

// Setup
function testNotEqual(val) {
    if (val != 99) { // Change this line
      return "Not Equal";
    }
    return "Equal";
  }
  
  // Change this value to test
  testNotEqual(10);

//---------------------------------------------------------------------------------------------------------------

// Comparison with the Strict Inequality Operator

// Setup
function testStrictNotEqual(val) {
    // Only Change Code Below this Line
    
    if (val !== 17) {
  
    // Only Change Code Above this Line
  
      return "Not Equal";
    }
    return "Equal";
  }
  
  // Change this value to test
  testStrictNotEqual(10);

//---------------------------------------------------------------------------------------------------------------

// Comparison with the Greater than operator

function testGreaterThan(val) {
    if (val > 100) {  // Change this line
      return "Over 100";
    }
    
    if (val > 10) {  // Change this line
      return "Over 10";
    }
  
    return "10 or Under";
  }
  
  // Change this value to test
  testGreaterThan(10);

//---------------------------------------------------------------------------------------------------------------

// Comparison with the Greater than Or Equal to operator

function testGreaterOrEqual(val) {
    if (val >= 20) {  // Change this line
      return "20 or Over";
    }
    
    if (val >= 10) {  // Change this line
      return "10 or Over";
    }
  
    return "Less than 10";
  }
  
  // Change this value to test
  testGreaterOrEqual(10);

//---------------------------------------------------------------------------------------------------------------

// Comparison with the Less Than Operator

function testLessThan(val) {
    if (val < 25) {  // Change this line
      return "Under 25";
    }
    
    if (val < 55) {  // Change this line
      return "Under 55";
    }
  
    return "55 or Over";
  }
  
  // Change this value to test
  testLessThan(10);

  