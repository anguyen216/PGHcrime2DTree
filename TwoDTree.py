#2D tree and Pittsburgh Crime Record
import math
import csv

#Node of the 2d tree
class twoDNode:
    #pre-condition: xy is a tuple of x and y (float or int). data - other info 
    #post-condition: a node is created with coordinate (x,y), some information
    # and it's children set to None
    def __init__(self,xy,data=None):
        self.coord = xy
        self.leftChild = None
        self.rightChild = None
        self.info = data

    def getCoord(self):
        return self.coord
    
    def setNode(self,newCoord):
        self.coord = newCoord

    def getInfo(self):
    	if self.info is None:
            return self.coord
        return self.info

    def getChildren(self):
        children = []
        children.append(self.leftChild)
        children.append(self.rightChild)
        return children

    def getLeft(self):
        return self.leftChild
    
    def getRight(self):
        return self.rightChild

    def setLeft(self,newNode):
        self.leftChild = newNode
    
    def setRight(self,newNode):
        self.rightChild = newNode

    def __str__(self):
    	if self.info is None:
            return str(self.coord)
        else:
            return str(self.info)

class TwoDTree:

    def __init__(self):
        self.root = None
        self.depth = 0

    #pre-condition: coord - a tuple of floats/int, data - other info
    #post-condition: properties of 2D tree are preserved
    def setRoot(self,coord,data=None):
        self.root = twoDNode(coord,data)

    #pre-condition: coord - a tuple of floats/int, data - other info
    #post-condition: properties of 2D tree are preserved
    def insert(self,coord,data=None):
        if self.root is None:
            self.setRoot(coord,data)
        else:
            self._insertNode(self.root,coord,self.depth,data)

    #pre-condition: 2D node, coord - a tupple floats/ints, depth - int
    # data can be anything including None
    def _insertNode(self,currentNode,coord,depth,data):
        axis = depth % 2
        next_depth = depth + 1
        if coord[axis] <= currentNode.getCoord()[axis]:
            if currentNode.getLeft() is None:
                currentNode.setLeft(twoDNode(coord,data))
            else:
                self._insertNode(currentNode.getLeft(),coord,next_depth,data)

        elif coord[axis] > currentNode.getCoord()[axis]:
            if currentNode.getRight() is None:
                currentNode.setRight(twoDNode(coord,data))
            else:
                self._insertNode(currentNode.getRight(),coord,next_depth,data)

    #pre-condition: the 2D tree has been constructed
    #post-condition: properties of 2D tree are preserved
    def preOrderPrint(self):
        return self._preOrderTravel(self.root)

    #pre-condition: current node - 2D Node
    def _preOrderTravel(self,currentNode):
        if currentNode is not None:
            print (currentNode.getInfo())
            if currentNode.getLeft() is not None:
                self._preOrderTravel(currentNode.getLeft())
            if currentNode.getRight() is not None:
                self._preOrderTravel(currentNode.getRight())

    #pre-condition: the 2D tree has been constructed
    #post-condition: properties of 2D tree are preserved
    def inOrderPrint(self):
        return self._inOrderTravel(self.root)

    #pre-condition: currentNode - 2D node
    def _inOrderTravel(self,currentNode):
        if currentNode is not None:
            if currentNode.getLeft() is not None:
                self._inOrderTravel(currentNode.getLeft())
            print (currentNode.getInfo())
            if currentNode.getRight() is not None:
                self._inOrderTravel(currentNode.getRight())
            
    #pre-condition: the 2D tree has been constructed
    #post-condition: properties of 2D tree are preserved
    def postOrderPrint(self):
        return self._postOrderTravel(self.root)

    #pre-condition: currentDode - 2D node
    def _postOrderTravel(self,currentNode):
        if currentNode is not None:
            if currentNode.getLeft() is not None:
                self._postOrderTravel(currentNode.getLeft())
            if currentNode.getRight() is not None:
                self._postOrderTravel(currentNode.getRight())
            print (currentNode.getInfo())

    #pre-condition: the 2D tree has been constructed
    #post-condition: properties of 2D tree are preserved
    def levelOrderPrint(self):
        toVisit = [self.root]
        while toVisit != []:
            node = toVisit.pop()
            print (node.getInfo())
            children = node.getChildren()
            if children[0] is not None:
                toVisit.insert(0,children[0])
            if children[1] is not None:
                toVisit.insert(0,children[1])

    #pre-condition: the 2D tree has been constructed
    #post-condition: properties of 2D tree are preserved
    def reverseLevelOrderPrint(self):
        toVisit = [self.root] #queue
        reverse = [] #stack
        while len(toVisit) > 0:
            node = toVisit.pop()
            reverse.append(node.getInfo())
            children = node.getChildren()
            if children[0] is not None:
                toVisit.insert(0,children[0])
            if children[1] is not None:
                toVisit.insert(0,children[1])
        while reverse != []:
            print (reverse.pop())

    #pre-condition: the 2D tree has been constructed and is not
    # empty. coordinates - floats/ints. (x1,y1) - left bottom
    # (x2,y2) - top right 
    #post-condition: a array of 0 or more node's info is returned. 
    # These nodes' coords are within the range specified 
    def findPointsInRange(self,x1,y1,x2,y2):
        givenRect = [(x1,y1),(x2,y2)] 
        res = []
        #return kml_input =  
        self._checkPoint(self.root,givenRect,self.depth,res)
        return res

    #pre-condition: cNode - 2D node, range - input coord, depth - int
    # pointList - result coord array
    #post-condition: list of 0 or more nodes in the given range is returned
    # properties of 2D tree are preserved
    def _checkPoint(self,cNode,range,depth,pointList):
        axis = depth % 2
        next_depth = depth + 1

        if cNode is None:
            return

        #if range is on the left of node - search left of node
        #if range is on the right of node - search right of node
        #if node is in the range - search both sides
        if cNode.getCoord()[axis] > range[1][axis]:
            self._checkPoint(cNode.getLeft(),range,next_depth,pointList)
        elif cNode.getCoord()[axis] < range[0][axis]:
            self._checkPoint(cNode.getRight(),range,next_depth,pointList)
        elif range[0][axis] <= cNode.getCoord()[axis] <= range[1][axis]:
            if range[0][1 - axis] <= cNode.getCoord()[1 - axis] <= range[1][1 - axis]:
                pointList.append(cNode.getInfo())
            self._checkPoint(cNode.getLeft(),range,next_depth,pointList)
            self._checkPoint(cNode.getRight(),range,next_depth,pointList)

    #pre-condition: x1 - float/int, y1 - float/int
    #post-condition: the info of the nearest point to query point (x1,y1) 
    def nearestNeighbor(self,x1,y1):
        qryPoint = (x1,y1)
        bestNode = self.root
        best_dst = self._calDist(self.root.getCoord(), qryPoint)
        p1 = self._findNearest(qryPoint, self.root.getLeft(), best_dst, self.depth, bestNode)
        p2 = self._findNearest(qryPoint, self.root.getRight(), best_dst, self.depth, bestNode)
        d1 = self._calDist(p1.getCoord(), qryPoint)
        d2 = self._calDist(p2.getCoord(), qryPoint)
        if d1 > d2:
            return p2.getInfo()
        else: return p1.getInfo()

    #pre-condition: qryPoint - tupple of coord, cNode - 2d node, distance - float
    # depth - int, best_sofar information of the current closest node
    def _findNearest(self, qryPoint, cNode, best_dst, depth, bestNode):
        axis = depth % 2
        next_depth = depth + 1

        if cNode is None:
            return bestNode

        if best_dst > self._calDist(qryPoint,cNode.getCoord()):
            best_dst = self._calDist(qryPoint,cNode.getCoord())
            bestNode = cNode

        #compare best distance with distance between current node and query point
        if best_dst > abs(qryPoint[axis] - cNode.getCoord()[axis]):
            self._findNearest(qryPoint,cNode.getLeft(),best_dst,next_depth,bestNode)
            self._findNearest(qryPoint,cNode.getRight(),best_dst,next_depth,bestNode)
        else:
            if qryPoint[axis] <= cNode.getCoord()[axis]:
                self._findNearest(qryPoint,cNode.getLeft(),best_dst,next_depth,bestNode)
            else: 
                self._findNearest(qryPoint,cNode.getRight(),best_dst,next_depth,bestNode)

        return bestNode

    #calculate distance between two points
    #pre-condition: each point is a tupple of coordindates
    #post-condition: distance (float) between 2 points
    def _calDist(self,point1,point2):
    	x1 = point1[0]
    	y1 = point1[1]
    	x2 = point2[0]
    	y2 = point2[1]
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

    #pre-condition: crimelist - array of arrays storing info
    #post-condition: the 2d tree is constructed and may be printed or 
    # queried
    def buildTree(self, crimelist):
        # insert X-Y coord as float in the 2d tree and store them as coord
            # store the entire crime as info
        for crime in crimelist:
            self.insert((float(crime[0]),float(crime[1])),crime)

def writeKML(kml_input):
    out_f = open('PGHCrimes.kml','w')
    out_f.write("<?xml version='1.0' encoding='UTF-8' ?>\n")
    out_f.write("<kml xmlns='http://earth.google.com/kml/2.2'>\n")
    out_f.write("<Document>\n")
    out_f.write("<Style id='style1'>\n")
    out_f.write("<IconStyle><Icon>\n")
    out_f.write("<href>http://maps.gstatic.com/intl/en_ALL/mapfiles/ms/micons/blue-dot.png</href>\n")
    out_f.write("</Icon></IconStyle></Style>\n")

    for crime in kml_input:
        out_f.write("<Placemark>\n")
        out_f.write("<name>" + crime[4] + "</name>\n")
        out_f.write("<description>" + crime[3] + "</description>\n")
        out_f.write("<styleUrl>#style1</styleUrl>\n")
        out_f.write("<Point>\n")
        out_f.write("<coordinates>" + crime[8] + "," + crime[7] + "</coordinates>\n")
        out_f.write("</Point></Placemark>\n")

    out_f.write("</Document></kml>")
    out_f.close()

#argument: filename - path to the data file that will be loaded into the 2d tree
#based on user input, output the appropriate information
def TwoDTreeDriver(filename):
    # parse input file
    crimeData = TwoDTree()
    # separate file data by line
    list = []
    csvfile = open(filename,'r')
    for line in csvfile:
        list.append(line)
    csvfile.close() # close the file to be a good noodle

    #split line using comma
    crimelist = []
    for item in list:
        crimelist.append(item.split(','))

    crimeData.buildTree(crimelist)
    print ("Crime file loaded into 2d tree with 27218 records.")
    while True:
        print ("What would you like to do?")
        print ("1: inorder")
        print ("2: pre-order")
        print ("3: level-order")
        print ("4: post-order")
        print ("5: reverse level-order")
        print ("6: search for points within range")
        print ("7: search for nearest neighbor")
        print ("8: quit")

        val = raw_input()
        if val == "1":
            crimeData.inOrderPrint()
        if val == "2":
            crimeData.preOrderPrint()
        if val == "3":
            crimeData.levelOrderPrint()
        if val == "4":
            crimeData.postOrderPrint()
        if val == "5":
            crimeData.reverseLevelOrderPrint()
            
        #store user input in an array
            # convert each raw_input in the array into float
        if val == "6":
            print ("input x1 y1 x2 y2 separate by space")
            user = raw_input()
            raw_coord = user.split(" ")
            coord = map(float,raw_coord)
            kml = crimeData.findPointsInRange(coord[0],coord[1],coord[2],coord[3])
            writeKML(kml)
            print ("The crime data has been written to PGHCrimes.KML. It is viewable in Google Earth")

        #store user input in an array
            #convert each raw_input in the array into float
        if val == "7":
            print ("input x and y coordinate separate by space")
            user = raw_input()
            raw_query = user.split(" ")
            coord = map(float,raw_query)
            print (crimeData.nearestNeighbor(coord[0],coord[1]))

        if val == "8":
            print ("Thank you for exploring Pittsburgh crimes in the 1990's")
            return

def main():
    TwoDTreeDriver("crimefile-1.csv")

if __name__ == "__main__":
    main()

