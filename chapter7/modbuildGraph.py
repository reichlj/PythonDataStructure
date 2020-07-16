from chapter7.modGraph import Graph as Graph
from chapter7.mybfs import bfs as bfs
from chapter7.mybfs import traverse as traverse

def buildGraph(wordFile, debug=False):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    if debug:
        print('Number of buckets: ' + str(len(d.keys())))
        for key in d:
            print(key,str(len(d[key])),'elements')
    return g

if __name__ == "__main__":
    g = buildGraph('wordFile.txt',True)
    print(g)
    bfs(g,g.getVertex('FOOL'))
    traverse(g.getVertex('POLL'))


