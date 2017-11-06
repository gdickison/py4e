// Prompt the user to enter a number. Keep prompting until the user enters "done". If the user enters anything other than a number or "done" print "Invalid input." When the user enters "done" exit the program and print the maximum, minimum, total, count, and average of the numbers entered.

var largest;
var smallest;
var count = 0;
var total = 0;
var average = 0;
while(true){
  var entry = prompt("Enter a number: ");
  if(entry == "done"){
    break;
  } else {
    try {
      if(isNaN(entry)) throw "Invalid input";
      if(entry == "") throw "Invalid input";
    }
    catch(err) {
      alert(err);
      console.log(err);
      continue;
    };
  };
  num = Number(entry);
  if(count == 0){
    largest = num;
    smallest = num;
  } else if(num > largest){
    largest = num;
  } else if(num < smallest){
    smallest = num;
  };
  count = count + 1;
  total = total + num;
  average = total / count;
  console.log(count + " " + num);
};
console.log("Maximum is " + largest);
console.log("Minimum is " + smallest);
console.log("Count is " + count);
console.log("Total is " + total);
console.log("Average is " + average);
