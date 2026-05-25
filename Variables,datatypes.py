Var= "Variable is like a container that holds a value. It is used to store data that can be changed during the execution of a program. "

print(Var)

value1=20
value2=10.2
value3="Hello, World!"

print(type(value1)) # we can use type() function to check the data type of a variable.
print(type(value2))
print(type(value3))

# add two variable/numbers/add two strings, but we have to make sure that both variables are of the same type, not string and variables should be.
# type should be same for both variables. If we try to add a string and a number, it will result in an error.


num1=10
num2=5.6
result=num1+num2

print("The sum of", num1, "and", num2, "is", result)

#add two strings. 
#string alsways should be in quotes, either single or double quotes.
str1="Hello"
str2="World"
result=str1 + " " + str2 # we can use the + operator to concatenate two strings. We can also add a space between the two strings by adding " " in between them.
print(result)

# If we try to add a string and a number, it will result in an error.
num3=10
str3="Python"
# result=num3 + str3 # This will raise a TypeError: unsupported operand type(s) for +: 'int' and 'str'

#add two variables of different types, we need to convert one of the variables to the same type as the other variable. We can use the str() function to convert a number to a string, or the int() function to convert a string to a number.
num4=10
str4="20"
result=num4 + int(str4) # convert str4 to an integer before adding
print("The sum of", num4, "and", str4, "is", result)

# we can also convert a number to a string using the str() function.
num5=10
str5="The number is: " + str(num5) # convert num5 to a string before concatenating
print(type(str5))
print(str5)

str6="83"
str7="17"
print(str6 + " " + str7) # This will concatenate the two strings and result in "83 17"

# change type of variable from string to integer using int() function.

str6="83"
str7="17"
print(int(str6) + int(str7)) # This will convert the strings to integers and result in 100


print("Enter a number: ")

num=input() # input() function is used to take input from the user. It always returns a string, so we need to convert it to an integer using int() function if we want to perform arithmetic operations on it.
num=int(num) +10 # add 10 to the input number and we have convertyed the input to an integer before adding.
print("The number is:", num)