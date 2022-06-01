import EdgeSelector
import ConnectEdges
class BoundedSolverAdapter:
    def solve(self,task):
        return EdgeSelector.EdgeSelector(task).boundedEdges(self.parameter)

class BruteForceBoundedSolver:
    def solve(self,task):
        return [EdgeSelector.Edge(j,k,task.dist(j,k)) for j in xrange(task.nVertices()) \
                for k in xrange(j) if task.dist(j,k)<=self.parameter]

class SpanningTreeAdapter:
    def solve(self,task):
        return EdgeSelector.EdgeSelector(task).spanningTree()

def CheckSpanningTree(edges,n):
    #we check, if all vertices are reachable from 0.
    s=set([0])
    while len(s)<n:
        before=len(s)
        for e in edges:
            if e.i in s:
                s.add(e.j)
            if e.j in s:
                s.add(e.i)
        if len(s)==before:
            raise Exception('Disjoint graph components.')
    if len(edges)!=n-1:
        raise Exception('There are redundant edges.')

class BruteForceSpanningTree:
    def solve(self,task):
        edges=[EdgeSelector.Edge(j,k,task.dist(j,k)) \
               for j in xrange(task.nVertices()) for k in xrange(j)]
        res,dummy=ConnectEdges.ConnectEdges(edges)
        #We use working funtion directly from test. This is a little hack.
        #So we check twice, if the vertices is really a spanning tree.
        CheckSpanningTree(res,task.nVertices())
        return res

def getPairOfSolvers(name,parameter):
    """ returns quick solver and bruteforce solver """
    if name=='bounded':
        quick=BoundedSolverAdapter()
        slow=BruteForceBoundedSolver()
    elif name=='spanning':
        quick=SpanningTreeAdapter()
        slow=BruteForceSpanningTree()
    else:
        raise Exception('Unknown solvers.')
    quick.parameter=parameter
    slow.parameter=parameter
    return quick,slow
