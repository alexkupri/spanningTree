from Structures import Edge
import SpanningTree
import Structures
import BoundedEdges
class EdgeSelector:
    """ The main class which solves three similar tasks on graphs. """
    
    def __init__(self,originalModel):
        """ Constructor.

        orignalModel is our task, which must have functions:
        nVertices() and dist(i,j). It describes distances between each pair.
        """
        self.__orig__=originalModel
        self.__n__=originalModel.nVertices();
        self.__cachedEdges__=dict();
        self.__root__=Structures.RegionalTree(self,0,xrange(0,self.__n__));
        
    def dist(self,i,j):
        """ Internal function, proxy with cache """
        if i>j:
            return self.dist(j,i)
        if i==j:
            return 0
        if (i,j) in self.__cachedEdges__:
            return self.__cachedEdges__[(i,j)]
        result=self.__orig__.dist(i,j)
        self.__cachedEdges__[(i,j)]=result
        return result

    def boundedEdges(self,radius):
        """ The simplest task: returns all edges which are not longer than radius"""
        return BoundedEdges.BoundedEdges(self,self.__root__,radius)
        
    def spanningTree(self):
        """ Returns minimal spanning tree """
        res,dummy=SpanningTree.SpanningTree(self,self.__root__)
        return res
