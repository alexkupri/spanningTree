class RegionalTree:
    __slots__=('capital','num','radius','lbranch','rbranch')
    def __init__(self,model,capital,points):
        self.capital=capital
        self.num=len(points)
        maxrad=0
        """ maxidx is new capital, which is the most distant point from the current one"""
        for j in points:
            if model.dist(capital,j)>maxrad:
                maxrad,maxidx=model.dist(capital,j),j
        self.radius=maxrad
        if self.num==1:
            return
        """ dividing cities into two parts: near current city and near new capital"""
        leftlist,rightlist=[],[]
        for j in points:
            if model.dist(capital,j)<=model.dist(maxidx,j) and j!=maxidx:
                """ For special case with all zero dist"""
                leftlist.append(j)
            else:
                rightlist.append(j)
        self.lbranch=RegionalTree(model,capital,leftlist)
        self.rbranch=RegionalTree(model,maxidx,rightlist)

class Edge:
    __slots__=('i','j','dist')
    def __init__(self,i,j,dist):
        self.i,self.j,self.dist=min(i,j),max(i,j),dist
