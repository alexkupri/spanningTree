def ConnectEdges(edges):
    """ there can be some optimizations here """
    """ edges can be very incomplete """
    edges.sort(key=lambda e:e.dist)
    verticeSet=set(e.i for e in edges)|set(e.j for e in edges)
    n=0
    idxmap=dict()
    for e in verticeSet:
        idxmap[e]=n
        n=n+1
    parent=[-1 for j in xrange(n)]
    mx=0
    def get_anc(j):
        j=idxmap[j]
        while parent[j]>0:            
            j=parent[j]
        return j
    result=[]
    for curEdge in edges:
        if get_anc(curEdge.i)!=get_anc(curEdge.j):
            result.append(curEdge)
            parent[get_anc(curEdge.i)]=get_anc(curEdge.j)
            mx=curEdge.dist
    return result,mx
