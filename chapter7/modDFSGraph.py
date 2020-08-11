from chapter7.modGraph import Graph

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(None)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

if __name__ == '__main__':
    g = DFSGraph()
    g.addEdge('A','B')
    g.addEdge('A','D')
    g.addEdge('B','C')
    g.addEdge('B','D')
    g.addEdge('D','E')
    g.addEdge('E','F')
    g.addEdge('E','B')
    g.addEdge('F','C')
    g.dfs()
    for aVertex in g:
        print(aVertex.id,aVertex.discovery_time,'/',aVertex.finish_time)

