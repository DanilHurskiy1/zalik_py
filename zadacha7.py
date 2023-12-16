def calculate_expression(expression):
    expression_without_spaces = expression.replace(" ", "")

    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }


    for operator in operators:
        if operator in expression_without_spaces:
            numbers = expression_without_spaces.split(operator)

            try:
                num1 = float(numbers[0])
                num2 = float(numbers[1])

                result = operators[operator](num1, num2)

                return result

            except (ValueError, IndexError, ZeroDivisionError):
                return "Некоректний вираз. Будь ласка, спробуйте знову."

def main():
    while True:
        expression = input("Введіть математичний вираз (або 'exit' для виходу): ")

        if expression.lower() == 'exit':
            print("Програма завершена.")
            break

        result = calculate_expression(expression)
        print("Результат обчислення:", result)

if __name__ == "__main__":
    main()