var fruit = prompt("Enter a fruit:");
// var index = 0;
// while(index < fruit.length){
//   console.log(index + " " + fruit[index]);
//   index = index + 1;
// };

var splitFruit = fruit.split("");
splitFruit.forEach(function(letter){
  console.log(letter);
});
