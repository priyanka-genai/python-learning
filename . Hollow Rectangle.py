'''
******
*    *
*    *
******

'''

# 4 row and 6 column hollow rectangle

r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))

for i in range(1,r+1):
    if i==1 or i==r:
        for j in range(c):
            print("*",end="")
    else:
        print("*",end="")
        for j in range(c-2):
            print(" ",end="")
        print("*",end="")
    print()
