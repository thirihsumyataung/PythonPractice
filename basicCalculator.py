
# Input is always string by default
# int() by adding this --> we changed input string into int --> for whole number
# float() we can use any number we want
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
#result = int(num1) + int(num2)
result = float(num1) + float(num2)

print(result)
print('{:.2f}'.format(result)) # to format the result into **.**