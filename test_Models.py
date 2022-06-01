import math
import random
class CartesianModel:
    def __init__(self):
        self.accesses=0
    def nVertices(self):
        return len(self.data)
    def dist(self,i,j):
        self.accesses=self.accesses+1
        return math.sqrt(sum((self.data[i][k]-self.data[j][k])**2 for k in xrange(len(self.data[i]))))

class CartesianUniformGenerator:
    def __init__(self,dim):
        self.__dim__=dim
    def Generate(self,size):
        coeff=math.pow(size,1.0/self.__dim__)
        result=CartesianModel()
        result.data=[[self.getValue()*coeff for j in xrange(self.__dim__)]for k in xrange(size)]
        return result
    def getValue(self):
        return random.random()

def ModelGenerator(name,param):
    if name=='cartesianU':
        return CartesianUniformGenerator(int(param))
    raise Exception('Unexpected model generator.')
