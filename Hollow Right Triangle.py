'''
Hollow Right Triangle

*
**
* *
*  *
*****

'''

r=int(input("Enter the number of rows: "))
for i in range(1,r+1):
    if i==1 or i==r:
        for j in range(i):
            print("*",end="")
    else:
        print("*",end="")
        for j in range(i-2):
            print(" ",end="")
        print("*",end="")
    print()