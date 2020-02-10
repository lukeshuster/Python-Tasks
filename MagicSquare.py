# WRITTEN BY LUKE SHUSTER

import math
filename = input("Enter name of file: ") +".txt"
magicfile = open(filename,'r')
while True:
    try:
        magicsum = int(input("Enter an integer Magic Sum: "))
        break
    except ValueError:
        print("ERROR - Ensure you enter an integer")

magiclist = []
for line in magicfile: # Pull the contents of the input into a list
        magiclist.append(line.strip().split(' '))

while True:
    sumdiag1 = 0
    sumdiag2 = 0
    for i in range (0, len(magiclist)):
        print("     "+str(i+1), end = "")
    print("\n" +"    "+ len(magiclist)*"------") # printing the horizontal coordinates

    for i in range (0, len(magiclist)):
        print(str(i+1) +" |", end = "") # printing the vertical coordinates
        sumrow = 0
        sumcol = 0
        for k in range (0, len(magiclist)):
            print("  "+str(magiclist[i][k]) +"  |", end = "") #printing the actual magic square
            magiclist[i][k] = int(magiclist[i][k])
            magiclist[k][i] = int(magiclist[k][i])
            sumrow += magiclist[i][k]
            sumcol += magiclist[k][i]
            if magiclist[i] == magiclist[k]:
                sumdiag1 += magiclist[i][k]
        print("\n" + "  |"+ len(magiclist)*"------")
        sumdiag2 += magiclist[i][(len(magiclist)-1)-i]

        if sumrow > magicsum or sumcol > magicsum or sumdiag1 > magicsum or sumdiag2 > magicsum:
            print("ERROR - Invalid input, violates the Magic Square property")
            exit()

    xcoord = input("choose horizontal row number (1-"+str(len(magiclist))+") or (q) to quit: ")
    xcoord = xcoord.lower()
    if xcoord  == "q" or xcoord == "quit":
        print("Goodbye!")
        break;
    elif xcoord.isnumeric(): # ensuring a positive integer is entered
        xcoord = int(xcoord) - 1; # correcting offset
        if xcoord < 0 or xcoord >= len(magiclist):
            print("ERROR - Please ensure you enter an integer within the number range")
    else:
        print("ERROR - Please ensure you enter a positive integer")

    ycoord = input("choose vertical column number (1-"+str(len(magiclist))+") or (q) to quit: ")
    ycoord = ycoord.lower()
    if ycoord  == "q" or ycoord == "quit":
        print("Goodbye!")
        break;
    elif ycoord.isnumeric():
        ycoord = int(ycoord) - 1;
        if ycoord < 0 or ycoord >= len(magiclist):
            print("ERROR - Please ensure you enter an integer within the number range")
    else:
        print("ERROR - Please ensure you enter a positive integer")

    if magiclist[xcoord][ycoord] == 0:
        sumdiag1 = 0
        sumdiag2 = 0
        magiclist[xcoord][ycoord] = int(input("Choose a number to enter here "))
        for i in range (0, len(magiclist)):
            sumrow = 0
            sumcol = 0
            for k in range (0, len(magiclist)):
                sumrow += magiclist[i][k]
                sumcol += magiclist[k][i]
                if magiclist[i] == magiclist[k]:
                    sumdiag1 += magiclist[i][k]
            sumdiag2 += magiclist[i][(len(magiclist)-1)-i]
            if sumrow > magicsum or sumcol > magicsum or sumdiag1 > magicsum or sumdiag2 > magicsum:
                print("ERROR - This value violates the magic square property")
                magiclist[xcoord][ycoord] = 0

    else:
        print("ERROR - Please ensure you select a zero element")


magicfile.close()



