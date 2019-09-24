import re
import sys
# YOUR CODE GOES HERE
street_cordinates = {}
acceptance = 1
def validation_input(user_input): #this function holds regular expressions to filter wrog frmats and patterns
    acceptance2 = 0
    while (acceptance2 == 0):
        # extracting numbers re.findall(r'-?\d+\.?\d*')
        validationac = re.compile(' ^[a|c]\s\"\w+\s?\w+\"\s(\(\s?-?\d+\s?,\s?-?\d+\s?\))+')
        validationg = re.compile('^g')
        validationr = re.compile('^[r]\s"\w+')
        # user_input = str(input("input the command and required input data required\n"))
        # print(user_input)
        if validationac.search(user_input):
            match = validationg.findall(user_input)
            #print("inputted good")
            acceptance2 = 1
        if validationr.search(user_input):
            match = validationg.findall(user_input)
            #print("inputted good")
            acceptance2 = 1
        if validationg.search(user_input):
            match = validationg.findall(user_input)
            #print("inputted good")
            acceptance2 = 1
        else:
            acceptance2 = 0
            print("Error: inputted wrong format of data.. Try again") # #this function holds regular expresso
    return user_input
def a(streetnamea, coordinatesa):
    #add strinf to dictionary
    print("welcome to add street")
    street_cordinates[streetnamea] = coordinatesa

def c(streetnamec, coordinatesc):
    #update the dictionary corresponding key
    print("welcome to change street")
    if (bool(street_cordinates)):
        for key in current_dict.keys():
            if key == streetnamec:
                street_cordinates[key] = coordinatesc
            else: 
                 print("Error: streetname Do not exist")
    else: 
        print("Error: there are no street or cordinates to change")

def r(streetnamer):
    print("welcoe to remove street")
    if (bool(street_cordinates)):
       for key in current_dict.keys():
           if key == streetnamec:
                del wordFreqDic[streetnamer]
             else: 
                 print("Error: streetname Do not exist")
    else: 
        print("Error: there are no street or cordinates to remove")
def g():
    print("welcome to graphing and hell")
    #graph this monster
def coordinatefunction(coordinates):
    coordinatelist1 = []
    xcoord = ""
    ycoord = ""  # variables are meant to help hold and confirm multiple digits in
    xbegin = 0
    ybegin = 0  # Variable are meant to indicate what axis you are on
    coordinatesdigits=[]
  #  coordinatelist2 = coordinates.replace(" ","")  # replace white space with a comma easy to then detect what coordinate you are in
    for i in street_cordinates.values():# for(int i =0; i < len(temp); i++)
        print ("current coordinate ",i)
        for j in range(len(i)):
            if i[j] == "(" :
                xbegin = 1
                ybegin =0
            if i[j] == ",":
                ybegin = 1
            if (xbegin and ybegin == 0 and i[j] != "(" and i[j] != "," and i[j] != ")"):
                xcoord +=  i[j]
            if (xbegin and ybegin == 1 and i[j] != "(" and i[j] != "," and i[j] != ")"):
                ycoord += i[j]
            if i[j] == ")":
                xbegin = 0
                ybegin = 0
                xcoordint = int(xcoord,10)
                ycoordint = int(ycoord,10)
                coordinatesdigits = [xcoordint,ycoordint]
               # coordinatesdigitsfinal = coordinatesdigits[1].replace(" ","")
                coordinatelist1.append(coordinatesdigits)
                xcoord = ""
                ycoord = ""
                print("coordinatesdigits = ", coordinatelist1)

#def splitting_data(user_input, comand, streetname, coordinates):
def main():
    ### YOUR MAIN COD E GOES HERE
    while (acceptance == 1):
        user_input = str(input("input the command and required input data required\n"))
        validation_input(user_input)
       # inputlist = user_input.split('"')
        inputlist = user_input.split('"')
        comand = inputlist[0]
        print("comand = "+ comand)
        street_name = inputlist[1]
        coordinates = inputlist[2]
        coordinates2= coordinates.replace(" ", "")
        # Consider a forloop statement here for the situation the error s not caught somewhere else
        if comand[0] == "a":
            a(street_name,coordinates2)
        elif comand == 'c':
            c(street_name,coordinates2)
        elif comand == 'r':
            r(street_name,coordinates2)
        elif comand == 'g':
            g()
        else:
            print("You have inputed the wrong comand ")
        #print(street_cordinates)
        print(street_cordinates) # printing out the dictionary to make sure its correct
        coordinatefunction(coordinates2)
       # print(coordinatelist1)


        # print()
    # sys.exit(0)
if __name__ == '__main__':

----------------------------------------------------------------------------------------------------------------
import sys

# YOUR CODE GOES HERE

def main():
    ### YOUR MAIN CODE GOES HERE

    ### sample code to read from stdin.
    ### make sure to remove all spurious print statements as required
    ### by the assignment
    while True:
        line = sys.stdin.readline()
        if line == '':
            break
        print 'read a line:', line

    print 'Finished reading input'
    # return exit code 0 on successful termination
    sys.exit(0)

if __name__ == '__main__':
    main()
