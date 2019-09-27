from __future__ import division
import re
import sys
import random
import math
street_cordinates = {}
vertices_dictionary = {}
vertices = set()
verticesout = set()
edgecrit1 = set()
edgecrit2 = set()
edgedream = set()
edgecritduplicate = set()
acceptance = 1
user_input = ""
midpointe = set()
tempelement = set()



def validation_input(): #this function holds regular expressions to filter wrog frmats and patterns
    acceptance2 = 0
    global user_input
    while (acceptance2 == 0):
       # extracting numbers re.findall(r'-?\d+\.?\d*')
        validationac = re.compile('^[a|c]\s"(\w+\s*\w+)+"\s(\(\s*-?\d+,\s*-?\d+\))+')
        validationg = re.compile('^g')
        validationr = re.compile('^[r]\s"\w+')
        if validationac.match(user_input):
           acceptance2 = 1

        elif validationr.match(user_input):
           acceptance2 = 1

        elif validationg.match(user_input):
           acceptance2 = 1
        else:
            acceptance2 = 0
            sys.stderr.write("Error: inputted wrong format of data.. Try again") # #this function holds regular expresso

            user_input = raw_input("input the command and required input data required\n")
            #global user_input = userinput
def a(streetnamea, coordinatesa):
    #add strinf to dictionary
    street_cordinates[streetnamea] = coordinatesa
def c(streetnamec, coordinatesc):
    truth = 0
    if (bool(street_cordinates)):
        for key in street_cordinates.keys():
            if key == streetnamec:
                street_cordinates[key] = coordinatesc
                truth = 1
        if truth != 1:
            sys.stderr.write("Error: streetname Do not exist")
    else:
        sys.stderr.write("Error: there are no street or cordinates to change")
def r(streetnamer):
    truth = 0
    if (bool(street_cordinates)):
       for key in street_cordinates.keys():
           if key == streetnamer:
                del street_cordinates[streetnamer]
                truth = 1
       if truth != 1:
          sys.stderr.write("Error: streetname Do not exist")
    else:
        sys.stderr.write("Error: there are no street or cordinates to remove")
def g():

    #graph this monster


    global verticesout
    sys.stdout.write("vertices = { ")
    sys.stdout.write("\n")
    for keys, values in vertices_dictionary.items():
        sys.stdout.write(" {}: {}".format(keys,values))
        sys.stdout.write("\n")
    sys.stdout.write("}")


    sys.stdout.write("\n")
    sys.stdout.write("\n")
    sys.stdout.write("Edges")
    sys.stdout.write("\n")
    edgedone = list(edgedream)
    for edges in edgedone:
        sys.stdout.write(" {},".format(edges))
        sys.stdout.write("\n")
    sys.stdout.write("}")
    sys.stdout.write("\n")

def coordinatefunction(coordinates):
    coordinatelist1 = []
    coordinatesdigits = []
    xcoord = ""
    ycoord = ""  # variables are meant to help hold and confirm multiple digits in
    xbegin = 0
    ybegin = 0  # Variable are meant to indicate what axis you are on
    david=coordinates
    for j in range(len(david)):
        if david[j] == "(":
            xbegin = 1
            ybegin =0
        if david[j] == ",":
            ybegin = 1
        if (xbegin and ybegin == 0 and david[j] != "(" and david[j] != "," and david[j] != ")"):
            xcoord +=  david[j]
        if (xbegin and ybegin == 1 and david[j] != "(" and david[j] != "," and david[j] != ")"):
            ycoord += david[j]
        if david[j] == ")":
            xbegin = 0
            ybegin = 0
            #xcoordint = int(xcoord,10)
            #ycoordint = int(ycoord,10)
            coordinatesdigits = tuple([int(xcoord,10),int(ycoord,10)])
            coordinatelist1.append(coordinatesdigits)
            xcoord = ""
            ycoord = ""
    return coordinatelist1
def verticesfinder():
    vstreet ={}
    dunno =[]
    for key, value in street_cordinates.items():
        vstreet.update({key: random.randint(1,20000)})
    for key1, value1 in street_cordinates.items():
        for key2, value2 in street_cordinates.items():
            if key1 != key2:
                val1 = vstreet.get(key1) + vstreet.get(key2)
                if val1 not in dunno:
                    dunno.append(val1)
                    verticesfinal(value1, value2)
def verticesfinal(a,b):
    seta = coordinatefunction(a)
    setb = coordinatefunction(b)
  #  print("set a = ",seta)
   # print("set b = ", setb)
    pointa = 0
    pointb = 1
    sizea = len(seta)-1
    sizeb = len(setb)-1
    for i in range(sizea):
        pointc =0
        pointd = 1
        for i in range(sizeb):
            intersects = intersection(seta[pointa],seta[pointb],setb[pointc],setb[pointd])
            if intersects != 0:
                vertices.add(intersects)
                vertices.add(seta[pointa])
                vertices.add(seta[pointb])
                vertices.add(setb[pointc])
                vertices.add(setb[pointd])
                edgecall = edgesbegin(intersects,seta[pointa],seta[pointb],setb[pointc],setb[pointd])

            pointc +=1
            pointd +=1
        pointa +=1
        pointb += 1
    verticesout = list(vertices)
    for i in range(len(verticesout)):
        # global  vertices_dictionary = {}
        vertices_dictionary[i + 1] = verticesout[i]
        #Edgecall1 = edgesbegin(seta[pointa],seta[pointb],setb[pointc],setb[pointd])
def intersection(apoint1, apoint2, bpoint1, bpoint2):
    xdifference = (apoint1[0] - apoint2[0], bpoint1[0] - bpoint2[0])
    ydifference = (apoint1[1] - apoint2[1], bpoint1[1] - bpoint2[1])
    div = det(xdifference, ydifference)
    if div == 0:
       # print('lines do not intersect')
        return 0
    d = (det(apoint1, apoint2), det(bpoint1, bpoint2))
    x = round((det(d, xdifference) / div),7)
    y = round((det(d, ydifference) / div),7)
    vectora = round(math.sqrt((apoint1[0] ** 2) + (apoint1[1] ** 2)),7)
    vectorb = round(math.sqrt((apoint2[0] ** 2) + (apoint2[1] ** 2)),7)
    maximum = round(max(vectora, vectorb),7)
    minimum =round(min(vectora, vectorb),7)
    # midpoint = [((x+y/2),((apoint1[1]+apoint1[2])/2)]
    m = math.sqrt((x ** 2) + (y ** 2))

   # print("midpoint = ", m)
    #print("x = ",x,"y = ", y)
    if (m >= minimum and m <= maximum):
        vertices.add((x, y))
        global midpointe
        midpointe.add((x,y))
        return x, y
    else:
        return 0
def edgesbegin(midpoint,apoint1, apoint2, bpoint1, bpoint2):
    edgecrit1.add((apoint1,midpoint))
    edgecrit1.add((midpoint,apoint2))
    edgecrit1.add((bpoint1,midpoint))
    edgecrit1.add((midpoint,bpoint2))
    edgeish = set()
    edgeish1 = set()
def finaledge1():
    test = 1
    midpoint =[]
    edgeish = list(edgecrit1)
    check = list(midpointe)
    for i in range(len(edgeish)):
        keep = edgeish[i]
        keepa = list(keep[0])
        keepb = list(keep[1])
        for j in range (len(check)):
            if check[j] in keep:
                midpoint = check[j]
                break
        for keys,values in street_cordinates.items():
            onestreet = coordinatefunction(values)
            a =0
            b = 1
            for first in range(len(onestreet)-1):
                 needed = edgesintersection(keep[0],keep[1],onestreet[a],onestreet[b])
                 if needed != 0:
                     if needed not in keep:
                        test = 0
                        reversable_pointcheck(midpoint, needed)
            a +=1
            b += 1
        if test ==1:
           edgecrit2.add(keep)
    #shenanigans
    print(tempelement)
    # ID shenanigans 3

def reversable_pointcheck(x,y): 
    pyt1 = (x[0]-y[0])**2
    pyt2 = (x[1]-y[1])**2
    magna = math.sqrt(pyt1 + pyt2)
    mag1 = round(magna, 7)
    if len(tempelement)==0:
        tempelement.add((x,y))
    else:
        Tempelement = list(tempelement)
        for things in Tempelement:
            xa = things[0]
            ya = things[1]
            test1 = (xa[0]-ya[0])**2
            test2 = (xa[1]-ya[1])**2
            whatevs = math.sqrt(test1 + test2)
            mag2 = round(whatevs,7)
        if mag2 != mag1:
            tempelement.add((x,y))

#def shenanigans():

def edgeid():
    edgeish = list(edgecrit2)
    print("edgish", edgeish)
    ida = 0
    idb = 0
    print ("vertices_dictionary.items()" , vertices_dictionary.items())
    for i in range(len(edgeish)):
        pairs = edgeish[i]
        paira = pairs[0]
        pairb = pairs[1]
        for keys, values in vertices_dictionary.items():
            if paira == values:
               ida = keys
               break
        for key, value in vertices_dictionary.items():
           if pairb == value:
               idb = key
               break
        edgetired = "<{},{}>".format(ida, idb)
        edgedream.add(edgetired)
def edgesintersection(keepa, keepb, bpoint1, bpoint2):
    xdifference = (keepa[0] - keepb[0], bpoint1[0] - bpoint2[0])
    ydifference = (keepa[1] - keepb[1], bpoint1[1] - bpoint2[1])
    div = det(xdifference, ydifference)
    if div == 0:
       # print('lines do not intersect')
        return 0
    d = (det(keepa, keepb), det(bpoint1, bpoint2))
    x = round((det(d, xdifference) / div),7)
    y = round((det(d, ydifference) / div),7)
    vectora = round((math.sqrt((keepa[0] ** 2) + (keepa[1] ** 2))),7)
    vectorb = round((math.sqrt((keepb[0] ** 2) + (keepb[1] ** 2))),7)
    maximum = round(max(vectora, vectorb),7)
    minimum = round(min(vectora, vectorb),7)
    # midpoint = [((x+y/2),((apoint1[1]+apoint1[2])/2)]
    m = round(math.sqrt((x ** 2) + (y ** 2)),7)
   # print("midpoint = ", m)
    #print("x = ",x,"y = ", y)
    if (m >= minimum and m <= maximum):
        return x, y
    else:
        return 0
def det(a, b):
    return (a[0] * b[1]) - (a[1] * b[0])
def main():
    while (acceptance == 1):
        global user_input
        user_input = raw_input("input the command and required input data required\n")
        validation_input()
        if user_input == "g":
            g()
        else:
            inputlist = user_input.split('"')
            comand = inputlist[0]
            street_name = inputlist[1]
            coordinates = inputlist[2]
            coordinates2= coordinates.replace(" ", "")
            # Consider a forloop statement here for the situation the error s not caught somewhere else
            if comand[0] == "a":
                a(street_name,coordinates2)
            elif comand[0] == "c":
                c(street_name,coordinates2)
            elif comand[0] == "r":
                r(street_name)
            else:
                sys.stderr.write("You have inputed the wrong comand ")
            vertices_dictionary.clear()
            vertices.clear()
            verticesout.clear()
            edgecrit1.clear()
            edgecrit2.clear()
            edgedream.clear()
            edgecritduplicate.clear()
            midpointe.clear()
            tempelement.clear()
            coordinatefunction(coordinates2)
       # print(street_cordinates) # printing out the dictionary to make sure its correct
            verticesfinder()
            finaledge1()
            edgeid()
         
        # sys.exit(0)
if __name__ == '__main__':
    try:
        main()
    except Exception:
        sys.stderr.write("Error: Wrong input format...")
