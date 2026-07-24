
'''Hollow Inverted Triangle Pattern

*****
****
*  *
* *
*

'''


r=int(input("Enter the number of rows: "))
for i in range(1,r+1):
    if i==1 or i==2 or i==r:
        for j in range(r-i+1):
            print("*",end="")
    else:
        print("*",end="")
        for j in range(r-i):
            print(" ",end="")
        print("*",end="")
    print()