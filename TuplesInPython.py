
# Tuple

# to create the item with only one item, you need to add comma after the 1st itme
# Otherwise, python will not know as tuple

# Once you declared the tuple, you cannot assigned or updated the members of tuple
#There are four collection data types in the Python programming language:
        #List is a collection which is ordered and changeable. Allows duplicate members.
        #Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
        #Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
        #Dictionary is a collection which is ordered** and changeable. No duplicate members.
aTuple=('apple',)
print(type(aTuple)) #<class 'tuple'>

bTuple=('apple')
print(type(bTuple)) # <class 'str'>


# print out the tuple if they are tuple
tuples = ('apple', 'banana', 'cherry')

if type(tuples)==tuple : print("Tuples: " , tuples)

# Access Tuples
print("Access the tuple from 1 index position tuples[1] : ", tuples[1])

# Access Tuples using For Loop
print("\n----- Access the tuples using FOR Loop ----- ")
i = 0
for item in tuples:
    print("Tuples from [ %d ] "%i, " index is : ", item)
    i = i +1


print("\n----- Access the tuples using FOR Loop Using RANGE(LEN(tuples))----- ")
# i is index number
for i in range(len(tuples)):
    print("Tuples from [ %d ] " % i, " index is : ", tuples[i])

tuples2 = ('Millions', 'Billion', 'Trillion', 'Trillion', 'Trillion')
print("\n----- Access the Tuple2 using WHILE Loop ----- ")
i = 0
while i < len(tuples2):
    print("Tuples from [ %d ] " % i, " index is : ", tuples2[i])
    i = i +1


# JOIN Tuples  --> Join the two tuples using operators such as + or *
tup1 = ('Washington','New York', 'Florida', 'California')
tropic = ('Pineapple', 'Durian', 'Banana')
print("\n ----- JOIN the Tuples -----")
tup2 = tup1 + tropic
print ("Join the two tuples using + sign : ", tup2)
tup3 = ("Pink", "Yellow", "Red", "Violet", "Black")
tup5 = tup2 + tup3
print ("Join the three tuples using + sign : ", tup5)
tup7 = tropic * 3
print("\n\n--- Using * sign to make it multiple the same tuple ----")
print(tup7)
print(len(tup7))
#Once tuples are assigned, they cannot be updated or assigned to other items
#tup6 = tup2 - tropic
#print("Remove the Tropical fruits tuples from TUP5 using - sign : ", tup6) # Return Errpr Message

# Count(ItemName)
print("\n--- Using COUNT() method to know how many TRILLIONS in tuples2 ---")
print(f"There are {tuples2.count('Trillion')} TRILLIONS.")

#Index(ItemName) --> To know the index position of the item
print("\n--- Using INDEX() method to know the position of the item in tuples ---")
print(f"Durian located at the index [{tup5.index('Durian')}] in TUP5.")
print("\nAccess the item from tuples using index number: ", tup5[5], tup5[0],tup5[-3])



# Unpack Tuples
#Note: The number of variables must match the number of values in the tuple,
#if not, you must use an asterisk to collect the remaining values as a list.

print("\n---Unpack the TUPLES ---")
(yellow, green, *red) = tup5 # only one starred expression allowed when we unpack the tuples
print(yellow)
print(green)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(aFruit, *tropicalFruits,aCherry) = fruits
print(aFruit)
print(tropicalFruits)
print(aCherry)

#Once a tuple is created, you cannot change its values.
# Tuples are unchangeable, or immutable as it also is called.

#But there is a workaround.
# You can convert the tuple into a list, change the list, and convert the list back into a tuple.

tuple_x = ('Kiwi','Million','Trillion', 'Billion',5, True)
print("\n \n--- Original TUPLE_X ---")
print(tuple_x)

#1) Covert Tuples into List
y = list(tuple_x) # tuple_y is a List type of tuple_x
y[-2] = y[-2]+4
y[-1] = False
y.insert(-1,True)
y.insert(0,'Multi Million')

tuple_x = tuple(y)
print("\n \n--- Updated TUPLE_X ---")
print(tuple_x)

# del keyword to remove the tuples completely
del tuple_x
print(tuple_x) # Error Message Expected
