#!/usr/bin/node
// index es la cantidad real, este numero dentro de indice no existe porque es mayor
// entonces si se le va restar se le tiene que restar uno más aparte del numero mayor
// osea restarle 2 numeros
const myVar = process.argv;
const arraicito = [];
if (myVar.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < myVar.length; i++) {
    arraicito.push(parseInt(myVar[i]));
    arraicito.sort((a, b) => a - b);
  }
  const index = arraicito.length;
  const num2max = arraicito[index - 2];
  console.log(num2max);
}
exports.myVar = myVar;
