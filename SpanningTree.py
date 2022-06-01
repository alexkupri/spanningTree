from ConnectEdges import ConnectEdges
from Structures import Edge
inf=float('inf')
def Interconnect(model,node1,node2,threshold,current):
    mindist=model.dist(node1.capital,node2.capital)-node1.radius-node2.radius
    if mindist>threshold and mindist>current:
        """ Here is our main cutting optimization: no need to explore """
        return [],current
    if node1.num<node2.num:
        node1,node2=node2,node1
    if node1.num==1:
        d=model.dist(node1.capital,node2.capital)
        current=min(current,d)
        return [Edge(node1.capital,node2.capital,d)],current
    e1,current=Interconnect(model,node1.lbranch,node2,threshold,current)
    e2,current=Interconnect(model,node1.rbranch,node2,threshold,current)
    return e1+e2,current

def SpanningTree(model,tree):
    if tree.num==1:
        return [],0
    e1,len1=SpanningTree(model,tree.lbranch)
    e2,len2=SpanningTree(model,tree.rbranch)
    e3,dummy=Interconnect(model,tree.lbranch,tree.rbranch,max(len1,len2),inf)
    return ConnectEdges(e1+e2+e3)
