let numbers = [4, 18, 23, 12, 18, 7, 23];
let number = 18;
let lastIndex = -1;

for (let i = numbers.length - 1; i >= 0; i--) {
  if (numbers[i] === number) {
    lastIndex = i;
    break;
  }
}

alert("Последний индекс числа " + number + " в массиве: " + lastIndex);
