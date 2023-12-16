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

                with open("main.log", "a") as log_file:
                    log_file.write(f"{expression} = {result}\n")

                return result

            except (ValueError, IndexError, ZeroDivisionError) as e:
                print(f"Помилка: {e}")
                return None

def main():
    while True:
        expression = input("Введіть математичний вираз (або 'exit' для виходу): ")

        if expression.lower() == 'exit':
            print("Програма завершена.")
            break

        result = calculate_expression(expression)
        if result is not None:
            print("Результат обчислення:", result)

if __name__ == "__main__":
    main()