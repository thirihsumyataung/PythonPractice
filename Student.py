from classInPython import Student

# from fileName import className
aperson = Student("Mg Mg", "Computer Science", 3.75, False)
print(aperson.name)
if aperson.is_on_honor_roll() :
    print(aperson.name + " is on honor roll")
else :
    print("Sorry, you are not on honor roll.")


