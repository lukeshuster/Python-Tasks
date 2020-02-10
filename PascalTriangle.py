# WRITTEN BY LUKE SHUSTER

def printPascal(li): # input- list of previous line in triangle, output & print- list with next line of triangle
    newLine = []    # container for new line of triangle
    old = 0
    if len(li) == 1:    # ugly method to from [1] to [1,2,1]
        newLine = [1,2]
    else:
        for x in li:
            newLine.append(int(x+old))  # add the two adjacent values to give the next value for the new line
            old = x
    newLine.append(1) # adds the final 1 at the end of the line
    print(newLine)
    return newLine;

line = []
while True: # input error checking
    try:
        rows = int(input("Enter a non-negative integer: "))
        if rows < 0:  # if the input is negative ask again
            print("ERROR - Ensure you enter a positive integer")
            continue
        break
    except ValueError:
        print("ERROR - Ensure you enter an integer")

for i in range(0,rows+1):   # repeat the function (input + 1) times
    line = printPascal(line)


