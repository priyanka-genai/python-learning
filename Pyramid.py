'''
    *
   ***
  *****
 *******
*********

'''


r=int(input("Enter the number of rows: "))
for i in range(1,r+1):  # for rows
    for j in range(r-i):  # for spaces
        print(" ",end="")
    for j in range(2*i-1): # for stars
        print("*",end="")
    print()