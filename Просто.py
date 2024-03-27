def main(input: str) -> str:
    try:
        if not any(primer in input for primer in ['+', '-', '*', '/', '%']): 
            raise ValueError('Строка не является математической операцией')
        else:
            a, c, b = input.split()
            a = int(a)
            b = int(b)
            if b == 0 and c == "/":
                return " ноль делить нельзя!"
            elif a < 1 or a > 10 or b < 1 or b > 10:
                return "Числа должны быть от 1 до 10"
            elif c == "%":
                return ("Такого в условиях задачи не было =)")  
            elif c =="+":
                return str(a + b)
            elif c == "-":
                return str(a - b)
            elif c == "*":
                return str(a * b)
            elif c == "/":
                return str(a // b)
    except ValueError as e:
        return "Ошибка: " + str(e)

user_input_string = input("Введите выражение (например, '3 + 5'): ")
result = main(user_input_string)
print("Результат:", result)