
# a list of friends
# elements in a list can be any type
# eg : aList  = ['Kevin', 2, false]
friends = ['Michael', 'Louis', 'Hervey', 'Biden', 'Kevin', 'Jennie', 'Lisa', 'Mona', 'Jin', 'Oscar', 'Toby']
####### there is the index position of the elements in the lists
## index starting from 0

print(friends) # return the list
print(friends[0]) # return the element at the index position 0
print(friends[-1]) # reverse the list
print(friends[1:3]) # range of the elements from position index 1 to index position 2 # not including 3 ( ]
print(friends[-3:]) # return the last 3 elements in the list

# List functions

# copy() --> to make the copy of the list
# assign to the new list --  List.copy()
friends2 = friends.copy()
print("Copy of the List: " , friends2)



# List.extend(list2)
lucky_nums=[3,6,9,7,11,10,12,99]
#friends.extend(lucky_nums)
print(friends)

# insert function -> need 2 parameters
# List.insert( Index Position,"Element Name")
# 1st is the index you want to insert the element
# 2nd -> the name of the element you want to insert
# all the elements have been pushed

friends.insert(1,"Teresa")
print("After adding the new element in the list: ", friends)



# remove(ElementName) -> to remove the element from the list

# pop() -> remove the last element of the list
# List.pop()
#friends.pop()

print("The last element remove from the list using POP() function is : ",(friends.pop()))
print("Elements in the list: ",friends)



# clear() -> to return the empty
# list List.clear()
friends.clear()
print("After using CLEAR() method: ", friends)


# count(Element)  --> to count how many elements appeared in the list
# List.count(ElementName)
pets = ['Gucci','Million','Billion','Trillion', 'LV','Million','Million' ]
print("Lets check how many MILLIONS in my pet list : " , pets.count("Million"), " MILLION")

# sort() --> To sort the elements in order alphabetically order
# List.sort() --> Sorting from A to Z
pets.sort()
print("Alphabetically Sorting the PET List: ", pets)

# sort() --> To sort the elements in reverse order alphabetically
# List.reverse() --> Sorting from Z to A
pets.reverse()
print("Alphabetically Reverse Sorting the PET List: ", pets)

