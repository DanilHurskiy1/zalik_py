def calculate_expression(expression):
    expression_without_spaces = expression.replace(" ", "")

    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }


    current_number = ''
    current_operator = None
    result = None


    for char in expression_without_spaces:
        if char.isdigit() or char == '.':

            current_number += char
        elif char in operators:

            if current_number:
                num = float(current_number)
                if result is None:
                    result = num
                else:
                    result = operators[current_operator](result, num)
            current_number = ''
            current_operator = char


    if current_number:
        num = float(current_number)
        if result is None:
            result = num
        else:
            result = operators[current_operator](result, num)

    return result

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