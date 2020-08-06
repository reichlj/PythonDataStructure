class Vertex:

    def __init__(self, key):
        self.id= key
        self.connectedTo = {}
        self.distance = -1
        self.predecessor = None
        self.discovery_time = -1
        self.finish_time = -1
        self.color = "white"

    def __str__(self):
        return str(str.id) + ' connectedTo ' +\
               str([x.id for x in self.connectedTo])

    def addNeighbor(self, vertex,weight=0):
        self.connectedTo[vertex] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,vertex):
        return self.connectedTo[vertex]

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getDistance(self):
        return self.distance

    def setDistance(self, distance):
        self.distance = distance

    def getPred(self):
        return self.predecessor

    def setPred(self, predecessor):
        self.predecessor = predecessor

    def getDiscovery(self):
        return self.discovery_time

    def setDiscovery(self, time):
        self.discovery_time = time

    def getFinish(self):
        return self.finish_time

    def setFinish(self, time):
        self.finish_time = time