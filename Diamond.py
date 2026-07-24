'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

'''

r=int(input("Enter the number of rows: "))
for i in range(1,r+1):
    for j in range(r-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()

for i in range(r-1,0,-1):
    for j in range(r-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()    