
def max_num(num1,num2,num3):
    if(num1 > num2) and (num1 > num3 ):
        print(num1)
    elif (num2 > num1) and (num2 > num3):
        print(num2)
    else:
        print(num3)

print("\n\n-----MAX NUMBER-----")
max_num(300,4,45)
max_num(300,4,45000)