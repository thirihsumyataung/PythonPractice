#from basicCalculator import result
#from basicCalculator import result
#from basicCalculator import result


# FUNCTIONS

# def functionName():
# all the codes after this line is going to be in function

#Creating a function
def aFunc():
    print("\nHello, Printing from the function....")

aFunc()

#Arguments
# If we declared the two arguments, function will expect as two arguments
# IF not, there will be an ERROR
def funcArguments(fname):
    print("\nNames printing using name: ", fname)

funcArguments("Tommy")
funcArguments("Shelby")
funcArguments("Louis")

# *
#Arbitrary Arguments, *args
# If we don't know the number of arguments, use *

def funcAStar(*arguments):
    #print(arguments)
     # return as a single tuple ( argument1, ) then (argument2, )
    for argument in arguments:
        print(argument)


funcAStar("Tom")
funcAStar("Molly")
funcAStar("Sally")
funcAStar("Lolly")

#Arbitrary Keyword Arguments, **kwargs
#key = value syntax.
def money(**values):
    print("\nBillion value is: ", values["Billion"])

money(Million="300 Million Dollar", Trillion="1 Trillion Dollar", Billion="500 Billion Dollar")

# Default Parameter Value
# Once we declared the function, we assign the value in argument
def defaultPara(country="Thailand"):
    print("I am from ",country)

defaultPara("Norway")
defaultPara("Swedan")
defaultPara()
defaultPara("United States")

#Passing a List as an Argument
# You can send the list as the argument, and we can access using LOOP
def myFunction(food):
    for x in food:
        print(x)

fruits = ["Pineapple", "Apple", "Durian", "Cherry", "Water melon"]
myFunction(fruits)

#RETURN the value
def cal(x):
    return 3 * x

print(cal(5))
print(cal(7))
print(cal(9))
print(cal(10))

#    Positional Arguments and Keyword Arguments
# Any argument before the / , are positional-only,
# and any argument after the *, are keyword-only.

def addition(num1, num2, /, *, num3, num4):
    print(num1,num2,num3,num4)
    print(num1+num2+num3+num4)

def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n-1)+ Fibonacci(n-2)



addition(4,5, num3= 20, num4=10)
print(Fibonacci(6))

def FiboList(n):
    FibListsItem = []

    for i in range(n):
        if n < 0:
            print("Incorrect Input")
        elif n==0:
            #FibListsItem[0] = 0
            FibListsItem.append(0)
            return FibListsItem #return 0
        elif n==1 or n==2:
            #FibListsItem[1] = 1
            FibListsItem.append(1)
            return FibListsItem #return 1
        else:
            FibNum = FiboList(n-1)+FiboList(n-2)
            FibListsItem.append(FibNum)
            return FibNum


print(FiboList(6))

def TriRecursion(k):
    if(k > 0):
        result = k + TriRecursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n----- Recursion Example -----")
TriRecursion(6)


def say_hi():
    print("Hello, Tommy ")

print("\n--- Top ---")
say_hi()
print("\n--- Bottom ---")

def cube(num):
    return num * num * num

result = cube(4) # return 64 => 4 * 4 * 4
print(result)


def aCal(k):
    results = 0
    if(k <= 0):
        print("Error Input")
    else:
        results =  k + aCal(k-1) # 5 + 4 + 3 + 2 + 1 => 15
    return results

print(aCal(5))

