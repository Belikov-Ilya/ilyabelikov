function getSortedArray(arr, key) {
  return arr.sort((a, b) => a[key] - b[key]);
}

let cars = [
  { brand: "Toyota", year: 2015 },
  { brand: "BMW", year: 2010 },
  { brand: "Audi", year: 2018 },
];

let sortedCars = getSortedArray(cars, "year");
console.log(sortedCars);
