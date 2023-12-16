while True:
    expression = input("Введіть вираз: ")

    if expression.lower() == 'exit':
        print("Програма завершена.")
        break

    expression_without_spaces = expression.replace(" ", "")

    numbers = expression_without_spaces.split('+')

    try:
        num1 = float(numbers[0])
        num2 = float(numbers[1])

        result = num1 + num2

        print("Результат:", result)

    except (ValueError, IndexError):
        print("Некоректний вираз. Будь ласка, спробуйте знову.")