# WRITTEN BY LUKE SHUSTER

def createDatabase(): # Returns a list li containing the records in CD_Store.txt
    li = [] # empty container
    file = open('CD_Store.txt','r')
    for line in file: # store each entry in a list inside the list
            li.append(line.split(","))
    return li;

def displayMenu():     # prints the menu and returns a selection made
    print("Welcome to the menu!"+"\n"+"Enter the corresponding number to select an option:"+"\n"+"1.  Print list of CD's"+"\n"+"2.  Sort CD's by Title"+"\n"+"3.  Sort CD's by Artist"+"\n"+"4.  Sort CD's by Genre"
          +"\n"+"5.  Sort CD's by Price"+"\n"+"6.  Find all CD's by Title"+"\n"+"7.  Find all CD's by Artist"+"\n"+"8.  Find all CD's by Genre"+"\n"+"9.  Find all CD's by Price"+"\n"+"10.  Quit"+"\n")

    while True:
        try:        # input error checking
            s = int(input("Enter a integer selection (1-10): "))
            if s < 1 or s >10:  # if the input is negative ask again
                print("ERROR - Ensure your selection is one of the above options.")
                continue
            break
        except ValueError:
            print("ERROR - Ensure you enter an integer selection.")
    return s;


# PRINT LIST -- INPUT LIST OF CD'S  -- OUTPUT NONE
def printList(l):
    for i in range(0,len(l)):
        print("Title:   "+l[i][0])
        print("Artist:   "+l[i][1])
        print("Genre:   "+l[i][2])
        print("Price:   "+l[i][3])
    return None;


# SORT BY TITLE -- INPUT LIST OF CD'S  -- OUTPUT ALPHABETICALLY SORTED LIST OF CD'S BY TITLE
def sortByTitle(l):                                                 # COMMENTED HERE -- essentially the same code for sortByArtist(), sortByGenre, sortByPrice -- avoiding duplicating comments
    sorted = []                                                     # Empty list to hold new sorted list
    tempList = l                                                    # copy of list so original doesn't get modified
    for i in range (0, len(l)):
        smallest = tempList[0][0].lower()                           # Initialising the smallest, using .lower toi ignore capitalization
        val = tempList[0]                                           #
        delIndex = 0                                                #
        k = tempList                                                # Temporary list to avoid errors with reducing loop size
        for j in range(0, len(k)):                                  # loops the list decreasing each time as the smallest set is removed each pass
            if min(smallest,tempList[j][0].lower()) != smallest:    # compares each value against the smallest, if the new value is smaller than the old it becomes the new smallest
                smallest = min(smallest,tempList[j][0].lower())
                val = tempList[j]                                   # storing the sublist of the smallest
                delIndex = j                                        # sorting the index of the smallest (for deletion later)
        sorted.append(val)                                          # Adding the smallest sublist of the group to the sorted list
        del tempList[delIndex]                                      # removing the smallest of the group for the next pass
    print('\n'+'Sorted by Title.')
    return sorted;

# SORT BY ARTIST -- INPUT LIST OF CD'S  -- OUTPUT ALPHABETICALLY SORTED LIST OF CD'S BY ARTIST
def sortByArtist(l):
    sorted = []
    tempList = l
    for i in range (0, len(l)):
        smallest = tempList[0][1].lower()
        val = tempList[0]
        delIndex = 0
        k = tempList
        for j in range(0, len(k)):
            if min(smallest,tempList[j][1].lower()) != smallest:
                smallest = min(smallest,tempList[j][1].lower())
                val = tempList[j]
                delIndex = j
        sorted.append(val)
        del tempList[delIndex]
    print('\n'+'Sorted by Artist.')
    return sorted;

# SORT BY GENRE -- INPUT LIST OF CD'S  -- OUTPUT ALPHABETICALLY SORTED LIST OF CD'S BY GENRE
def sortByGenre(l):
    sorted = []
    tempList = l
    for i in range (0, len(l)):
        smallest = tempList[0][2].lower()
        val = tempList[0]
        delIndex = 0
        k = tempList
        for j in range(0, len(k)):
            if min(smallest,tempList[j][2].lower()) != smallest:
                smallest = min(smallest,tempList[j][2].lower())
                val = tempList[j]
                delIndex = j
        sorted.append(val)
        del tempList[delIndex]
    print('\n'+'Sorted by Genre.')
    return sorted;

# SORT BY PRICE -- INPUT LIST OF CD'S  -- OUTPUT SMALLEST TO LARGEST SORTED LIST OF CD'S BY PRICE
def sortByPrice(l):
    sorted = []
    tempList = l
    for i in range (0, len(l)):
        smallest = float(tempList[0][3])
        val = tempList[0]
        delIndex = 0
        k = tempList
        for j in range(0, len(k)):
            if min(smallest,float(tempList[j][3])) != smallest:
                smallest = min(smallest,float(tempList[j][3])) # .strip('\n')
                val = tempList[j]
                delIndex = j
        sorted.append(val)
        del tempList[delIndex]
    print('\n'+'Sorted by Price.')
    return sorted;

# FIND ALL TITLE -- INPUT LIST OF CD'S && TARGET SEARCH STRING  -- OUTPUT PRINTED TITLES & DATA EXACTLY MATCHING SEARCH STRING
def findByTitle(l,s):
    found = False                                           # Simple flag to check if a result was found
    for i in range (0,len(l)):
        if s == l[i][0]:                                    # if the search string matches
            found = True
            print('\n'+"Title:   "+l[i][0])                 # print the result
            print("Artist:   "+l[i][1])
            print("Genre:   "+l[i][2])
            print("Price:   "+l[i][3])
    if not found:
        print("Sorry no titles match that search."+'\n')
    return None;

# FIND ALL ARTIST -- INPUT LIST OF CD'S && TARGET SEARCH STRING  -- OUTPUT PRINTED ARTIST & DATA EXACTLY MATCHING SEARCH STRING
def findByArtist(l,s): #input - a target string + list of CD's
    found = False
    for i in range (0,len(l)):
        if s == l[i][1]:
            found = True
            print('\n'+"Title:   "+l[i][0])
            print("Artist:   "+l[i][1])
            print("Genre:   "+l[i][2])
            print("Price:   "+l[i][3])
    if not found:
        print("Sorry no artists match that search."+'\n')
    return None;

# FIND ALL GENRE -- INPUT LIST OF CD'S && TARGET SEARCH STRING  -- OUTPUT PRINTED GENRE & DATA EXACTLY MATCHING SEARCH STRING
def findByGenre(l,s):  #input - a target string + list of CD's
    found = False
    for i in range (0,len(l)):
        if s == l[i][2]:
            found = True
            print('\n'+"Title:   "+l[i][0])
            print("Artist:   "+l[i][1])
            print("Genre:   "+l[i][2])
            print("Price:   "+l[i][3])
    if not found:
        print("Sorry no genres match that search."+'\n')
    return None;

# FIND ALL PRICE -- INPUT LIST OF CD'S && TARGET SEARCH STRING  -- OUTPUT ALL SETS OF DATA WITH PRICE <= SEARCH FLOAT
def findByPrice(l,p):  #input - a target string + list of CD's
    priceList = []
    found = False
    for i in range (0,len(l)):
        if p > float(l[i][3]):                  # print all the results <= the search number
            found = True
            print('\n'+"Title:   "+l[i][0])
            print("Artist:   "+l[i][1])
            print("Genre:   "+l[i][2])
            print("Price:   "+l[i][3])
    if not found:
        print("Sorry nothing is below that price."+'\n')
    return None;

# GET STRING -- INPUT STRING PROMPT FOR INPUT  -- OUTPUT STRING
def getSearchString(searchPrompt):
    while True: # input error checking
        try:
            s = str(input(searchPrompt))
            break
        except ValueError:
            print("ERROR - Ensure you enter a string.")
    return s;

# GET FLOAT -- INPUT STRING PROMPT FOR INPUT  -- OUTPUT FLOAT
def getSearchPrice(searchPrompt):
    while True: # input error checking
        try:
            f = float(input(searchPrompt))
            break
        except ValueError:
            print("ERROR - Ensure you enter a decimal number.")
    return f;


cdList = []
cdList = createDatabase()                                             # populate the database
while True:                                                           # main code loop
    sel = displayMenu()                                               # print menu and get selection
    # selection choices
    if sel == 1:printList(cdList)
    if sel == 2:cdList = sortByTitle(cdList)
    if sel == 3:cdList = sortByArtist(cdList)
    if sel == 4:cdList = sortByGenre(cdList)
    if sel == 5:cdList = sortByPrice(cdList)
    if sel == 6:
        searchString = getSearchString("Please enter a Title to search: ")
        findByTitle(cdList,searchString)
    if sel == 7:
        searchString = getSearchString("Please enter an Artist to search: ")
        findByArtist(cdList,searchString)

    if sel == 8:
        searchString = getSearchString("Please enter a Genre to search: ")
        findByGenre(cdList,searchString)
    if sel == 9:
        searchPrice = getSearchPrice("Please enter a decimal price to search up to: ")
        findByPrice(cdList,searchPrice)
    if sel == 10:quit()
