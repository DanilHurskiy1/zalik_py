expression = input("Введіть вираз: ")

numbers = expression.split('+')

num1 = int(numbers[0])
num2 = int(numbers[1])

result = num1 + num2

print("Результат:", result)