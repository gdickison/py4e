// 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
// # Score Grade
// # >= 0.9 A
// # >= 0.8 B
// # >= 0.7 C
// # >= 0.6 D
// # < 0.6 F
// # If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
var score = prompt("Enter Score:");
try {
  if(isNaN(score)) throw "Enter a number between 0.0 and 1.0";
  if(Number(score) < 0.0 || Number(score) > 1.0) throw "Enter a number between 0.0 and 1.0";
}
catch(err) {
  alert(err);
};
iscore = Number(score);
if(iscore >= 0.9){
  console.log("A");
} else if(iscore >= 0.8){
  console.log("B");
} else if(iscore >= 0.7){
  console.log("C");
} else if(iscore >= 0.6){
  console.log("D");
} else {
  console.log("F");
};
