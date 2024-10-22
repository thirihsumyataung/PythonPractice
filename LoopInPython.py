#from TuplesInPython import aFruit

#LOOP


# WHILE CONDITION:
# while CONDITION: => while the condition is true, the block of code will work

i = 1
while i <= 10:
    print (i)
    i+=1

#continue statement we can stop the current iteration, and continue with the next:

print("\n\n\n")
j = 0
while j < 10:
    j += 1
    if j==7 or j==9: # Keep going for next iteration, skip the condition i = 7 or i = 9
        continue
    print(j)



#With the break statement we can stop the loop even if the while condition is true:
print("\n\n\n")
x = 1
while x < 15:
  print(x)
  if x == 7:
    break
  x += 1

print("\n\n\n")
for letter in "Cloud Academy":
    print(letter)
#1st iteration of the loop, we print out C
#2nd iteration of the loop, we print out l
#3rd iteration of the loop, we print out o
#4th iteration of the loop, we print out u
#5th iteration of the loop, we print out d

# ------ SO ON
aFib = [0,1]

aFib.append(aFib[1] + aFib[0])
aFib.append(aFib[2] + aFib[1])
aFib.append(aFib[3] + aFib[2])
aFib.append(aFib[4] + aFib[3])
aFib.append(aFib[5] + aFib[4])

print(aFib)

def aRecFib(num):
    originalFib = [0,1]
    for index in range(2,num):
        aVal = originalFib[index-1]+originalFib[index-2]
        originalFib.append(aVal)
        #print(index,aVal)
    return originalFib

print(aRecFib(7)) #Fib list returned from Recursive Function

terms = int(input("Enter the terms: "))
print(aRecFib(terms))