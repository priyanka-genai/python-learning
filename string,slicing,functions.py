# String is combination of characters enclosed in single quotes, double quotes, or triple quotes.
# String is a sequence of characters. We can use string to store text data.
str1="Hello, World!" # string enclosed in double quotes
str2='Hello, World!' # string enclosed in single quotes
str3="""Hello, World!""" # string enclosed in triple quotes 
print(str1)
print(str2)
print(str3)


#slicing of string
str4="Python Programming"
print(str4[0]) # we can access individual characters of a string using indexing. The index starts from 0. So, str4[0] will give us the first character of the string, which is 'P'.
print(str4[7]) # str4[7] will give us the 8th character of the string, which is 'P'.
print(str4[-1]) # we can also use negative indexing to access characters from the end of the string. str4[-1] will give us the last character of the string, which is 'g'.


#length of string
print(len(str4)) # we can use the len() function to get the length of a string. len(str4) will give us the length of the string, which is 18.


print(str4[0:6]) # we can use slicing to access a range of characters in a string. str4[0:6] will give us the characters from index 0 to index 5, which is 'Python'.
print(str4[7:18]) # str4[7:18] will give us the characters from index 7 to index 17, which is 'Programming'.
print(str4[:]) # str4[:] will give us the entire string, which is 'Python Programming'.
print(str4[::]) # str4[::] will also give us the entire string, which is 'Python Programming'.
print(str4[::2]) # str4[::2] will give us every second character of the string, which is 'Pto rgamn'.
print(str4[0:19:1]) # str4[0:19:1] will give us the characters from index 0 to index 18 with a step of 1, which is 'Python Programming'.

print(str4[1:10:2]) # str4[1:10:2] will give us every second character from index 1 to index 9, which is 'yhn rg'.


#reversing a string
print(str4[::-1]) # str4[::-1] will give us the reverse of the string, which is 'gnimmargorP nohtyP'.
print(str4[::-2]) # str4[::-2] will give us every second character of the string in reverse order, which is 'gimrpPnhy'.


#functions- Isalpha(),isalnum(),endswith(),count(),capitalize(), find(),lower(),upper(),replace()
str5="Hello, World!"
print(str5.isalpha()) # str5.isalpha() will return False because the string contains a comma and a space, which are not alphabetic characters.
str6="HelloWorld"
print(str6.isalpha()) # str6.isalpha() will return True because the string contains only alphabetic characters.

print(str5.isalnum()) # str5.isalnum() will return False because the string contains a comma and a space, which are not alphanumeric characters.
str7="HelloWorld123"
print(str7.isalnum()) # str7.isalnum() will return True because the string contains only alphanumeric characters (letters and numbers).


print(str5.endswith("!")) # str5.endswith("!") will return True because the string ends with an exclamation mark.
print(str5.endswith(".")) # str5.endswith(".") will return False because the string does not end with a period.

print(str5.count("o")) # str5.count("o") will return 2 because the string contains two occurrences of the letter 'o'.


str8="hello, world!"
print(str8.capitalize()) # str8.capitalize() will return 'Hello, world!' because it capitalizes the first letter of the string and converts the rest of the letters to lowercase.
print(str8.find("o")) # str8.find("o") will return 4 because the first occurrence of the letter 'o' is at index 4.

print(str5.lower()) # str5.lower() will return 'hello, world!' because it converts all the letters in the string to lowercase.
print(str8.upper()) # str8.upper() will return 'HELLO, WORLD!' because it converts all the letters in the string to uppercase.

print(str5.replace("Hello", "Hi")) # str5.replace("Hello", "Hi") will return 'Hi, World!' because it replaces the substring "Hello" with "Hi" in the string.