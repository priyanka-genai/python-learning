'''
Right-Aligned Triangle Pattern

    *
   **
  ***
 ****
*****

'''

r=int(input("Enter the number of rows: "))
for i in range(1,r+1):     # for rows
    for j in range(r-i):   # for spaces
        print(" ",end="")
    for j in range(i):     # for stars
        print("*",end="")
    print()


