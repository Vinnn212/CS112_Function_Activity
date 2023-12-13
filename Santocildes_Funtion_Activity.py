def calculating_sum(num1, num2, num3):
    total = num1 + num2 + num3

    if num1 == num2 == num3:
        return num1 * num2 * num3
    elif num1 == num3:
        return num1 * num3 + num2
    elif num2 == num3:
        return num2 * num3 + num1
    elif num1 == num2:
        return num1 * num2 + num3
    else:
        return total

print("")
numb1 = eval(input("Enter a first number: "))
numb2 = eval(input("Enter a second number: "))
numb3 = eval(input("Enter a third number: "))

result = calculating_sum(numb1, numb2, numb3)
print("")
print("The result is: ", result)