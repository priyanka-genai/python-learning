# list is a collection which is ordered and changeable. Allows duplicate members.
# Create a list:
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Accessing list items
print(thislist[0]) # we can access individual items of a list using indexing. The index starts from 0. So, thislist[0] will give us the first item of the list, which is 'apple'.
print(thislist[1]) # thislist[1] will give us the second item of the list, which is 'banana'.
print(thislist[2]) # thislist[2] will give us the third item of the list, which is 'cherry'.

# numbers in list
numlist = [1, 2, 3, 4, 5]
print(numlist)

 # Accessing list items

print(numlist[2]) # numlist[2] will give us the third item of the list, which is 3.
print(numlist[3]) # numlist[3] will give us the fourth item of the list, which is 4.
print(numlist[4]) # numlist[4] will give us the fifth item of the list, which is 5. 


#list functions
#sort() function is used to sort the list in ascending order.
numlist.sort()
print(numlist) # this will print the sorted list, which is [1, 2, 3, 4, 5].

#reverse() function is used to reverse the order of the list.
numlist.reverse()
print(numlist) # this will print the reversed list, which is [5, 4, 3, 2, 1].

#slice() function is used to access a range of items in the list. The syntax for slicing is list[start:stop:step]. The start index is inclusive, while the stop index is exclusive. The step parameter is optional and specifies the step size for slicing.
numlist1=[1,2,3,4,5,6,7,8,9,10]
print(numlist1[0:3]) # numlist1[0:3] will give us the items from index 0 to index 2, which is [1, 2, 3].
print(numlist1[1:4]) # numlist1[1:4] will give us the items from index 1 to index 3, which is [2, 3, 4].
print(numlist1[::2]) # numlist1[::2] will give us every second item of the list, which is [1, 3, 5, 7, 9].
print(numlist1[1:5:2]) # numlist1[1:5:2] will give us every second item from index 1 to index 4, which is [2, 4].