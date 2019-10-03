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
edgedreamfinal = set()
edgecritduplicate = set()
acceptance = 1
user_input = ""
midpointe = set()
tempelement = set()
def validation_input():  # this function holds regular expressions to filter wrog frmats and patterns
    acceptance2 = 0
    global user_input
    while (acceptance2 == 0):
        # extracting numbers re.findall(r'-?\d+\.?\d*')
        validationac = re.compile('^[a|c]\s+\"(\s*\w+\s*)+\"\s+((\(\s*-?[0-9]+\s*,\s*-?[0-9]+\s*\)\s*)+)$')
        validationg = re.compile('^g')
        validationr = re.compile('^[r]\s+\"(\s*\w+\s*)+\"\s+')
        if validationac.match(user_input):
            acceptance2 = 1

        elif validationr.match(user_input):
            acceptance2 = 1

        elif validationg.match(user_input):
            acceptance2 = 1
        else:
            acceptance2 = 0
            sys.stderr.write("Error: inputted wrong format of data.. Try again \n")  # #this function holds regular expresso
            try:
                user_input = raw_input()
            except EOFError:
                sys.stderr.write("Error: EOF or empty input!")
                sys.exit()
               # user_input = " "
            #print user_input
           # user_input = raw_input()
            # global user_input = userinput
def a(streetnamea, coordinatesa):
    # add strinf to dictionary
    truth = 0
    for key in street_cordinates.keys():
        if key == streetnamea:
            sys.stderr.write("Error: streetname already exists \n")
            truth = 1
    if truth != 1:
            street_cordinates[streetnamea] = coordinatesa
def c(streetnamec, coordinatesc):
    truth = 0
    if (bool(street_cordinates)):
        for key in street_cordinates.keys():
            if key == streetnamec:
                street_cordinates[key] = coordinatesc
                truth = 1
        if truth != 1:
            sys.stderr.write("Error: streetname Do not exist \n")
    else:
        sys.stderr.write("Error: there are no street or cordinates to change \n")
def r(streetnamer):
    truth = 0
    if (bool(street_cordinates)):
        for key in street_cordinates.keys():
            if key == streetnamer:
                del street_cordinates[streetnamer]
                truth = 1
        if truth != 1:
            sys.stderr.write("Error: streetname Do not exist \n")
    else:
        sys.stderr.write("Error: there are no street or cordinates to remove \n")
def g():
    # graph this monster
   # print("edge dream = ", edgedream)
  #  print("edgecrit2 = ", edgecrit2)
   # print("edge supposed = ", edgedreamfinal)
   if (bool(street_cordinates)):
        global verticesout
        sys.stdout.write("V = { ")
        sys.stdout.write("\n")
        for keys, values in vertices_dictionary.items():
            valuelist = list(values)
            formatted = ['%.2f' % elem for elem in valuelist]
            #print("formatted = ") = formatted
            #formatted2 = sys.stdout.write.format(*formatted)
           # sys.stdout.write(" {}: {}".format(keys, *formatted, sep =' '))
           # sys.stdout.write(keys)
           # sys.stdout.write(": (")
            ##sys.stdout.write(*formatted, sep =', ')
            sys.stdout.write(" {}: {}".format(keys, " ("))
            sys.stdout.write(', '.join(formatted))
            sys.stdout.write(")")
           # sys.stdout.write(', '.join(formatted))
          #  sys.stdout.write(")")
            sys.stdout.write("\n")
        sys.stdout.write("}")


        sys.stdout.write("\n")
        sys.stdout.write("\n")
        sys.stdout.write("E = { ")
        sys.stdout.write("\n")
        edgedone = list(edgedream)
        for edges in edgedone:
            sys.stdout.write(" {}".format(edges))
            if edges != edgedone[-1]:
                sys.stdout.write(', ')
            sys.stdout.write("\n")
        sys.stdout.write("}")
        sys.stdout.write("\n")
   else:
       sys.stderr.write("Error: there are no streets or cordinates to graph \n")
def coordinatefunction(coordinates):
    coordinatelist1 = []
    coordinatesdigits = []
    xcoord = ""
    ycoord = ""  # variables are meant to help hold and confirm multiple digits in
    xbegin = 0
    ybegin = 0  # Variable are meant to indicate what axis you are on
    david = coordinates
    for j in range(len(david)):
        if david[j] == "(":
            xbegin = 1
            ybegin = 0
        if david[j] == ",":
            ybegin = 1
        if (xbegin and ybegin == 0 and david[j] != "(" and david[j] != "," and david[j] != ")"):
            xcoord += david[j]
        if (xbegin and ybegin == 1 and david[j] != "(" and david[j] != "," and david[j] != ")"):
            ycoord += david[j]
        if david[j] == ")":
            xbegin = 0
            ybegin = 0
            # xcoordint = int(xcoord,10)
            # ycoordint = int(ycoord,10)
            coordinatesdigits = tuple([int(xcoord, 10), int(ycoord, 10)])
            coordinatelist1.append(coordinatesdigits)
            xcoord = ""
            ycoord = ""
    return coordinatelist1
def verticesfinder():
    vstreet = {}
    dunno = []
    for key, value in street_cordinates.items():
        vstreet.update({key: random.randint(1, 20000)})
    for key1, value1 in street_cordinates.items():
        for key2, value2 in street_cordinates.items():
            if key1 != key2:
                val1 = vstreet.get(key1) + vstreet.get(key2)
                if val1 not in dunno:
                    dunno.append(val1)
                    verticesfinal(value1, value2)
def verticesfinal(a, b):
    seta = coordinatefunction(a)
    setb = coordinatefunction(b)
    #  print("set a = ",seta)
    # print("set b = ", setb)
    pointa = 0
    pointb = 1
    sizea = len(seta) - 1
    sizeb = len(setb) - 1
    for i in range(sizea):
        pointc = 0
        pointd = 1
        for i in range(sizeb):
            intersects = intersection(seta[pointa], seta[pointb], setb[pointc], setb[pointd])
            if intersects != 0:
                #print("INtersection = ", intersects)
                vertices.add(intersects)
                vertices.add(seta[pointa])
                vertices.add(seta[pointb])
                vertices.add(setb[pointc])
                vertices.add(setb[pointd])
                edgesbegin(intersects, seta[pointa], seta[pointb], setb[pointc], setb[pointd])

            pointc += 1
            pointd += 1
        pointa += 1
        pointb += 1
    verticesout = list(vertices)
    for i in range(len(verticesout)):
        # global  vertices_dictionary = {}
        vertices_dictionary[i + 1] = verticesout[i]
        # Edgecall = edgesbegin(seta[pointa],seta[pointb],setb[pointc],setb[pointd])
def intersection(apoint1, apoint2, bpoint1, bpoint2):
    xdifference = (apoint1[0] - apoint2[0], bpoint1[0] - bpoint2[0])
    ydifference = (apoint1[1] - apoint2[1], bpoint1[1] - bpoint2[1])
    div = determinantslover(xdifference, ydifference)
    if div == 0:
        # print('lines do not intersect')
        return 0
    d = (determinantslover(apoint1, apoint2), determinantslover(bpoint1, bpoint2))
    x = round((determinantslover(d, xdifference) / div), 7)
    y = round((determinantslover(d, ydifference) / div), 7)
    vectora = round(math.sqrt((apoint1[0] ** 2) + (apoint1[1] ** 2)), 7)
    vectorb = round(math.sqrt((apoint2[0] ** 2) + (apoint2[1] ** 2)), 7)
    maximum = round(max(vectora, vectorb), 7)
    minimum = round(min(vectora, vectorb), 7)
    # midpoint = [((x+y/2),((apoint1[1]+apoint1[2])/2)]
    m = math.sqrt((x ** 2) + (y ** 2))
    # print("midpoint = ", m)
    # print("x = ",x,"y = ", y)
    if (m >= minimum and m <= maximum):
        vertices.add((x, y))
        global midpointe
        midpointe.add((x, y))
        return x, y
    else:
        return 0
def edgesbegin(midpoint, apoint1, apoint2, bpoint1, bpoint2):
    edgecrit1.add((apoint1, midpoint))
    edgecrit1.add((midpoint, apoint2))
    edgecrit1.add((bpoint1, midpoint))
    edgecrit1.add((midpoint, bpoint2))
    return edgecrit1
def finaledge1():
    test = 1
    midpoint = 0
    edgeish = list(edgecrit1)
    check = list(midpointe)
    for i in range(len(edgeish)):
        test=1
        keep = edgeish[i]
        for j in range(len(check)):
            if check[j] in keep:
                midpoint = check[j]
                break
        for keys, values in street_cordinates.items():
            onestreet = coordinatefunction(values)
            a = 0
            b = 1
            for first in range(len(onestreet) - 1):
                needed = edgesintersection(keep[0], keep[1], onestreet[a], onestreet[b])
                if needed != 0:
                   # print("needed = ", needed)
                    #print("keep_need = ", keep)
                    if needed not in keep:
                     #   print("keep1 = " ,keep)
                        test = 0
                        reversable_pointcheck(midpoint, needed)

            a += 1
            b += 1
        if test == 1:
         #print("keep2 = " ,keep)
         edgecrit2.add(keep)
        # shenanigans
def shenanigans():
    deadline1 = list(edgecrit2)
    for i in range(len(deadline1)):
        test = 1
        deadline2 = deadline1[i]
        for keys, values in street_cordinates.items():
            deadlinestreet = coordinatefunction(values)
            a = 0
            b = 1
            for first in range(len(deadlinestreet) - 1):
                deadlinejust = edgesintersection(deadline2[0], deadline2[1], deadlinestreet[a], deadlinestreet[b])
                if deadlinejust == 0:
                    del deadline1[i]
            a += 1
            b += 1
        global edgedreamfinal
        edgedreamfinal.add(deadline1[i])
        # shenanigans
def reversable_pointcheck(x, y):
    pyt1 = (x[0] - y[0]) ** 2
    pyt2 = (x[1] - y[1]) ** 2
    magna = math.sqrt(pyt1 + pyt2)
    mag2 =0
    mag1 = round(magna, 7)
    if len(tempelement) == 0:
        tempelement.add((x, y))
    else:
        Tempelement = list(tempelement)
        for things in Tempelement:
            xa = things[0]
            ya = things[1]
            test1 = (xa[0] - ya[0]) ** 2
            test2 = (xa[1] - ya[1]) ** 2
            whatevs = math.sqrt(test1 + test2)
            mag2 = round(whatevs, 7)
        if mag2 != mag1:
            tempelement.add((x, y))
# def shenanigans():
def edgesintersection(keepa, keepb, bpoint1, bpoint2):
    xdifference = (keepa[0] - keepb[0], bpoint1[0] - bpoint2[0])
    ydifference = (keepa[1] - keepb[1], bpoint1[1] - bpoint2[1])
    div = determinantslover(xdifference, ydifference)
    if div == 0:
        # print('lines do not intersect')
        return 0
    d = (determinantslover(keepa, keepb), determinantslover(bpoint1, bpoint2))
    x = round((determinantslover(d, xdifference) / div), 7)
    y = round((determinantslover(d, ydifference) / div), 7)
    vectora = round((math.sqrt((keepa[0] ** 2) + (keepa[1] ** 2))), 7)
    vectorb = round((math.sqrt((keepb[0] ** 2) + (keepb[1] ** 2))), 7)
    vectorc= round((math.sqrt((bpoint1[0] ** 2) + (bpoint1[1] ** 2))), 7)
    vectord = round((math.sqrt((bpoint2[0] ** 2) + (bpoint2[1] ** 2))), 7)
    maximum = round(max(vectora, vectorb), 7)
    minimum = round(min(vectora, vectorb), 7)
    maximuma = round(max(vectorc, vectord), 7)
    minimuma= round(min(vectorc, vectord), 7)
    # midpoint = [((x+y/2),((apoint1[1]+apoint1[2])/2)]
    m = round(math.sqrt((x ** 2) + (y ** 2)), 7)
    # print("midpoint = ", m)
    # print("x = ",x,"y = ", y)
    if (m >= minimum and m <= maximum and m >= minimuma and m <= maximuma):
        return x,y
    else:
        return 0
def edgeid():
    edgeish = list(edgecrit2)
    #print("edgish", edgeish)
    ida = 0
    idb = 0
    #print ("vertices_dictionary.items()", vertices_dictionary.items())
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
def determinantslover(a, b):
    return (a[0] * b[1]) - (a[1] * b[0])
def main():

   ##raw_input
    while (acceptance == 1):
        global user_input
        user_input = raw_input()
        validation_input()
        if user_input == "g":
            g()
        else:
            inputlist = user_input.split('"')
            comand = inputlist[0]
            street_name = inputlist[1]
            coordinates = inputlist[2]
          #  print( "Coordinates ",coordinates)
            coordinates2 = coordinates.replace(" ", "")
            # Consider a forloop statement here for the situation the error s not caught somewhere else
           # print("Coordinates2 ", coordinates2)
            if comand[0] == "a":
                a(street_name, coordinates2)
            elif comand[0] == "c":
                c(street_name, coordinates2)
            elif comand[0] == "r":
                r(street_name)
            else:
                sys.stderr.write("You have inputed the wrong comand \n")
            vertices_dictionary.clear()
            vertices.clear()
            verticesout.clear()
            edgecrit1.clear()
            edgecrit2.clear()
            edgedream.clear()
            edgecritduplicate.clear()
            midpointe.clear()
            tempelement.clear()
            edgedreamfinal.clear()
            coordinatefunction(coordinates2)
        verticesfinder()
        finaledge1()
        edgeid()
        # sys.exit(0)
if __name__ == '__main__':
   # try:
        main()
   # except Exception:
   #     sys.stderr.write("Error: Wrong input format... \n")
