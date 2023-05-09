function getPrice(hours, urgent) {
  let rate = 1500;
  if (urgent) {
    hours /= 2;
    rate *= 2.5;
  }
  if (hours > 150) {
    rate -= 250;
  }
  let cost = hours * rate;
  alert("Стоимость проекта: " + cost + " рублей");
}

// пример использования
getPrice(100, false);
