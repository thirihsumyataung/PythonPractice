
# FILE
# Dealing with files in python

# r --> read
# w --> write
# a --> add
# r+ --> Read and write

#always make sure you close the file, after you read it

# To make sure it is readable file --> using file.readable() method
employee_file = open("employees.txt","r") # To read from this file
employee_file2 = open("employees1.txt","w") # to write in this file

# Copy the employee_file
for emp in employee_file.readlines():
    employee_file2.writelines(emp)

#print(employee_file.readable())
'''
print(employee_file.readline()) # to write a single line of text from .txt file 
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
'''
#print(employee_file.writable())
#employee_file.write("\nToby - Human Resources")

#employee_file = open("employees.txt","w") #Rewrite the txt file

#print(employee_file.readlines()) #Printing the file as LIST
#print(employee_file.readlines()[2]) #Printing the element  at the index position
#print(employee_file.read()) #actually read it
'''
print("\n\n-----------------")
for emp in employee_file.readlines():
    print(emp)
'''
employee_file.close() #close the file -- No longer we can access it
employee_file2.close()