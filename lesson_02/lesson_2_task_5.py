def month_to_season(number):
    if 1 <= number <= 2 or number == 12:
        return "Зима"
    elif 3 <= number <= 5:
        return "Весна"
    elif 6 <= number <= 8:
        return "Лето"
    elif 9 <= number <= 11:
        return "Осень"
    else:
        return "Неверный номер месяца"
    
number = int(input("Введите номер месяца (1-12): "))
print(month_to_season(number)) 