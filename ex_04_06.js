var computepay = function(hours, rate){
  var h = Number(hours);
  var r = Number(rate);
  var pay;
  var ot;
  if(h > 40){
    ot = h-40;
    pay = r*40 + r*ot*1.5;
  } else {
    pay = r*h;
  };
  return pay;
};
var hours = prompt("Enter hours:");
var rate = prompt("Enter rate:");
console.log(computepay(hours, rate));
