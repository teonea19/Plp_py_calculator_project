
print("****************************************************")
print("************** MY SIMPLE CALCULATOR ****************")
print("****************************************************")

num1 = int (input("Enter first number: "))
num2 = int (input("Enter second number: "))

add = num1 + num2
print(f"{num1} + {num2} = {add}")

sub = num1 - num2
print(f"{num1} - {num2} = {sub}")

mul = num1 * num2
print(f"{num1} * {num2} = {mul}")

if num2 != 0:
    div = float(num1 / num2)
    print(f"{num1} / {num2} = {div}")
else:
    print("Division by Zero not accepted")

