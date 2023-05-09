function getOrder(computer) {
  let basePrice = 50000;
  let totalPrice = basePrice;

  // проверяем каждый технический показатель и добавляем стоимость
  if (computer.processor === "Intel Core i7") {
    totalPrice += 15000;
  } else if (computer.processor === "Intel Core i9") {
    totalPrice += 25000;
  }

  if (computer.ram === "16 ГБ") {
    totalPrice += 8000;
  } else if (computer.ram === "32 ГБ") {
    totalPrice += 16000;
  }

  if (computer.storage === "512 ГБ SSD") {
    totalPrice += 10000;
  } else if (computer.storage === "1 ТБ SSD") {
    totalPrice += 20000;
  }

  // выводим результат заказа
  let message = "Вы заказали компьютер со следующими характеристиками:\n";
  message += "Процессор: " + computer.processor + "\n";
  message += "Оперативная память: " + computer.ram + "\n";
  message += "Накопитель: " + computer.storage + "\n";
  message += "Итоговая цена: " + totalPrice + " рублей";

  alert(message);
}

// пример использования
let myComputer = {
  processor: "Intel Core i7",
  ram: "16 ГБ",
  storage: "512 ГБ SSD",
};

getOrder(myComputer); // выводит сообщение с характеристиками и ценой заказа
