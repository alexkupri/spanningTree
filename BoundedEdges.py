import Structures
def PairwiseSelect(model,subtree1,subtree2,radius):
    capitaldist=model.dist(subtree1.capital,subtree2.capital)
    if capitaldist-subtree1.radius-subtree2.radius>radius:
        return []
    """ Here is main cut of branches: we do not explore edges further"""
    if subtree1.num==1 and subtree2.num==1:
        return [Structures.Edge(subtree1.capital,subtree2.capital,capitaldist)]
    if subtree1.num>subtree2.num:
        return PairwiseSelect(model,subtree1.lbranch,subtree2,radius)+\
               PairwiseSelect(model,subtree1.rbranch,subtree2,radius)
    else:
        return PairwiseSelect(model,subtree1,subtree2.lbranch,radius)+\
               PairwiseSelect(model,subtree1,subtree2.rbranch,radius)        

def BoundedEdges(model,tree,radius):
    if tree.num==1:
        return []
    s1=BoundedEdges(model,tree.lbranch,radius)
    s2=BoundedEdges(model,tree.rbranch,radius)
    s3=PairwiseSelect(model,tree.lbranch,tree.rbranch,radius)
    return s1+s2+s3
