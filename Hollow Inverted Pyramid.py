'''

*********
 *     *
  *   *
   * *
    *

'''


r = int(input("Enter number of rows: "))

for i in range(1, r + 1):

    # Print spaces
    for j in range(i - 1):
        print(" ", end="")

    # Print stars
    if i == 1:
        for j in range(2 * r - 1):
            print("*", end="")
    else:
        print("*", end="")
        for j in range(2 * (r - i) - 1):
            print(" ", end="")
        if i != r:
            print("*", end="")

    # Move to next row
    print()