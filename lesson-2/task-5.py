prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]


# первая часть
def price_description(prices):
    for price in prices:
        print(f'{price // 1:.0f} руб. {(price - price // 1) * 100:02.0f} коп.')


print("Вывод списка в отформатированном формате:")
price_description(prices)

# вторая часть
print("Сортировка по возрастанию:")
print(f"Обьект списка до сортировки: {id(prices)}")
prices.sort()
print(f"Обьект списка до сортировки: {id(prices)}")
price_description(prices)

# третья часть
print("Новый список отсортированный по убыванию:")
reversed_prices = prices[::-1]
price_description(reversed_prices)

# четвертая часть
print("5 самых дорогих товара:")
price_description(prices[-5::])
