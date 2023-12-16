operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

while True:
    expression = input("Введіть математичний вираз: ")

    if expression.lower() == 'exit':
        print("Програма завершена.")
        break

    expression_without_spaces = expression.replace(" ", "")

    for operator in operators:
        if operator in expression_without_spaces:
            numbers = expression_without_spaces.split(operator)

            try:
                num1 = float(numbers[0])
                num2 = float(numbers[1])

                result = operators[operator](num1, num2)

                print(f"Результат {operator}:", result)

            except (ValueError, IndexError, ZeroDivisionError):
                print("Некоректний вираз. Будь ласка, спробуйте знову.")

            break
    else:
        print("Непідтримувана операція. Будь ласка, використовуйте +, -, *, /.")