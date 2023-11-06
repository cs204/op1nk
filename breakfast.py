menu = {
    "кофе": 20.00,
    "чай": 10.00,
    "булочка": 5.00,
    "салат": 30.40,
    "пирожное": 45.50
}

def main():
    order = []
    total_cost = 0.0

    try:
        while True:
            dish = input("Блюдо: ").lower()
            if dish in menu:
                order.append(dish)
                total_cost += menu[dish]
            else:
                print(f"Блюдо '{dish}' отсутствует в меню. Продолжайте заказ.")
    except EOFError:
        pass

    print(f"Сумма: {total_cost:.2f}")

if __name__ == "__main__":
    main()