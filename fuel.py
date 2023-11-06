def calculate_fuel_percentage():
    while True:
        try:
            fraction = input("Дробь: ")
            x, y = map(int, fraction.split('/'))

            if x <= 0 or y <= 0 or x > y:
                print("Некорректные значения. Попробуйте снова.")
                continue

            percentage = round(x / y * 100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")

            break
        except ValueError:
            print("Ошибка: Введите целые числа.")
        except ZeroDivisionError:
            print("Ошибка: Знаменатель не может быть нулем.")

if __name__ == "__main__":
    calculate_fuel_percentage()