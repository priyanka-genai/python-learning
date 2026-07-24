


r=int(input("Enter the number of rows: "))
for i in range(1,r+1):
    for j in range(i-1):
        print(" ",end="")
    for j in range(2*(r-i)+1):
        print("*",end="")
    print()