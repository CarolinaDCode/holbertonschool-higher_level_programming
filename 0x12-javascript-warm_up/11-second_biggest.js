#!/usr/bin/node
const myVar = process.argv;
let arraicito = [];
if (myVar.length < 3 || myVar[2] == 1) {
    console.log('0');
} else {
    for (let i = 2; i < myVar.length; i++) {
        arraicito.push(parseInt(myVar[i]));
        arraicito.sort();
    }
    const index = arraicito.length;
    let num2max = arraicito[index - 2];
    console.log(num2max);
}
//index es la cantidad real, este numero dentro de indice no existe porque es mayor
//entonces si se le va restar se le tiene que restar uno más aparte del numero mayor
//osea restarle 2 numeros
