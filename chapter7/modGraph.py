from chapter7.modVertex import Vertex

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def __contains__(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __iter__(self):
        return iter(self.vertList.values())

    def __str__(self):
        return "".join('({0:s}, {1:s})\n'.format(str(v.getId()),str(w.getId()))\
               for v in self for w in v.getConnections())

    def addEdge(self,from_key,to_key,cost=0):
        if from_key not in self.vertList:
            self.addVertex(from_key)
        if to_key not in self.vertList:
            self.addVertex(to_key)
        self.vertList[from_key].addNeighbor(self.vertList[to_key],cost)

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def getVertices(self):
        return self.vertList.keys()


