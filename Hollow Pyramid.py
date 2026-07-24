
'''
    *
   * *
  *   *
 *     *
*********
'''


r=int(input("Enter the number of rows: "))
for i in range(1,r+1):
    for j in range (r-i):
        print(" ",end="")
    if i==1:
        print("*",end="")
    
    elif i==r:
        for j in range(2*r-1):
            print("*",end="")
    else:
        print("*",end="")
        for j in range(2*i-3):
            print(" ",end="")
        print("*",end="")
    print()