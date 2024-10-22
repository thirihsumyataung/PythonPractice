#result = 10/0 #ZeroDivisionError: division by zero

try:
    # result = 10 / 0
    number = int(input("Enter a number  : "))
    print(number)
except ZeroDivisionError as err: # store this error as a variable
    print(err)
except ValueError as er:
    print(er)


#except SpecificError:
    #print("Error Message")