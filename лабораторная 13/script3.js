function calculateSalary(dirtySalary) {
  let taxRate = 0.35;
  if (dirtySalary >= 100000) {
    taxRate = 0.45;
  }
  let netSalary = dirtySalary * (1 - taxRate);
  return Math.round(netSalary);
}
let dirtySalary = 75000;
let netSalary = calculateSalary(dirtySalary);
console.log("Грязная зарплата:", dirtySalary);
console.log("Чистая зарплата:", netSalary);
