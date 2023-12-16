expression = input("Введіть вираз: ")

numbers = expression.split('+')

num1 = float(numbers[0])
num2 = float(numbers[1])

result = num1 + num2

print("Результат:", result)