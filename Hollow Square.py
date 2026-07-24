'''
*****
*   *
*   *
*   *
*****

'''

r=int(input("Enter the number of rows for the square: "))
for i in range(1,r+1):
    if i==1 or i==r:
        for j in range(r):  #for print 5 * in first and last row 
            print("*",end="")
    else:
        print("*",end="")
        for j in range(r-2):  # for print 3 spaces in middle rows
            print(" ",end="")
        print("*",end="")
    print()