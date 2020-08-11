from chapter7.modGraph import Graph
from chapter7.modknightTour import knightTour
from chapter7.modknightTour import knightTourOrdered
import time

moveOffsets = [(-1,-2),(-1,2), (-2,-1),(-2,1), (1,-2),(1,2), (2,-1),(2,1)]

def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row,col,bdSize)
            newPositions = genLegalMoves(row,col,bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0],e[1],bdSize)
                ktGraph.addEdge(nodeId,nid)
    return ktGraph

def posToNodeId(row,col,bdSize):
    return row*bdSize + col

def genLegalMoves(row,col,bdSize):
    newMoves = []
    for i in moveOffsets:
        newX = row + i[0]
        newY = col + i[1]
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(x,bdSize):
    if x>=0 and x<bdSize:
        return True
    else:
        return False

if __name__ == '__main__':
    bdsize = 31
    # kg = knightGraph(bdsize)
    # print('Number of Vertices',kg.numVertices)
    # path = []
    # start = time.time()
    # knightTour(0,path,kg.getVertex(12),bdsize*bdsize-1)
    # print('Path length',len(path))
    # print('Path',[item.id for item in path])
    # print('Sets equal',set(item.id for item in path)==set(range(bdsize*bdsize)))
    # print("Time={0:10.4f}s".format(time.time()-start))

    kg = knightGraph(bdsize)
    print('Number of Vertices',kg.numVertices)
    path = []
    start = time.time()
    knightTourOrdered(0,path,kg.getVertex(12),bdsize*bdsize-1)
    print('Ordered Path length',len(path))
    print('Ordered Path',[item.id for item in path])
    print('Ordered Sets equal',set(item.id for item in path)==set(range(bdsize*bdsize)))
    print("Ordered Time={0:10.4f}s".format(time.time()-start))

