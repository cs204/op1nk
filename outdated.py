def month_to_number(month):
    months = {
        "январь": "01",
        "февраль": "02",
        "март": "03",
        "апрель": "04",
        "май": "05",
        "июнь": "06",
        "июль": "07",
        "август": "08",
        "сентябрь": "09",
        "октябрь": "10",
        "ноябрь": "11",
        "декабрь": "12",
    }
    return months.get(month.lower())

def date_input():
    while True:
        date_str = input("Дата: ")
        parts = date_str.split()

        if len(parts) == 3:
            day, month, year = parts
            if month in months.keys():
                month = month_to_number(month)
                if day.isdigit() and 1 <= int(day) <= 31 and year.isdigit() and len(year) == 4:
                    return f"{year}-{month}-{day}"
        elif len(parts) == 1:
            date_parts = date_str.split(".")
            if len(date_parts) == 3:
                month, day, year = date_parts
                if month.isdigit() and 1 <= int(month) <= 12 and day.isdigit() and 1 <= int(day) <= 31 and year.isdigit() and len(year) == 4:
                    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"

        print("Неверный формат даты. Попробуйте снова.")

if __name__ == "__main__":
    date_in_iso_format = date_input()
    print(f"Дата в формате ISO 8601: {date_in_iso_format}")
