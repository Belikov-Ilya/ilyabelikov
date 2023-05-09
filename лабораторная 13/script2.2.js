let numbers = [5, 2, 9, 1, 5, 6, 3];
let index = 5;

for (let i = 0; i < numbers.length - 1; i++) {
  let min = i;
  for (let j = i + 1; j < numbers.length; j++) {
    if (numbers[j] < numbers[min]) {
      min = j;
    }
  }
  if (min !== i) {
    let temp = numbers[i];
    numbers[i] = numbers[min];
    numbers[min] = temp;
  }
}

let foundIndex = numbers.indexOf(index);

if (foundIndex === -1) {
  console.log("Элемент не найден");
} else {
  console.log(
    "Индекс элемента " + index + " в отсортированном массиве: " + foundIndex
  );
}
