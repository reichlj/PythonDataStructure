def knightTour(n,path,nextVertex,limit):
    nextVertex.setColor('gray')
    path.append(nextVertex)
    if n < limit:
        nbrList = list(nextVertex.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1,path,nbrList[i],limit)
            i = i + 1
        if not done:
            path.pop()
            nextVertex.setColor('white')
    else:
        done = True
    return done

def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]

def knightTourOrdered(n,path,nextVertex,limit):
    nextVertex.setColor('gray')
    path.append(nextVertex)
    if n < limit:
        nbrList = orderByAvail(nextVertex)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTourOrdered(n+1,path,nbrList[i],limit)
            i = i + 1
        if not done:
            path.pop()
            nextVertex.setColor('white')
    else:
        done = True
    return done