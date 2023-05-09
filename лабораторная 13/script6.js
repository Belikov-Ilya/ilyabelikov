function getData(keys, data) {
  let result = [];
  for (let i = 0; i < data.length; i++) {
    let obj = {};
    for (let j = 0; j < keys.length; j++) {
      if (data[i][j] !== undefined) {
        obj[keys[j]] = data[i][j];
      }
    }
    result.push(obj);
  }
  return result;
}

let keys = ["имя", "возраст", "город"];
let data = [
  ["Джон", 30, "Нью-Йорк"],
  ["Джейн", 25, "Лос-Анджелес"],
  ["Боб", 40],
];

let result = getData(keys, data);
console.log(result);
