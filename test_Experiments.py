import math
def checkCorrectness(taskGen,fastSolver,slowSolver,parameter):
    task=taskGen.Generate(parameter)
    l1=fastSolver.solve(task)
    l2=slowSolver.solve(task)
    s1=set([(e.i,e.j) for e in l1])
    s2=set([(e.i,e.j) for e in l2])
    if s1!=s2:
        raise Exception('Test failed: sets do not match.')
    print 'Test succeeded. There are ',len(s1),' edges.'

def showStatistics(taskGen,fastSolver,parameter):
    print 'The columns are: (1) number of poins, (2) number of calls of dist(i,j)'
    print '(3) number of calls of dist(i,j) per edge, (4) number of edges per vertice'
    nums=[2**i for i in xrange(int(math.log(parameter,2)))]
    exps=10
    for sz in nums:
        s,e=0.0,0.0
        for j in xrange(exps):
            task=taskGen.Generate(sz)
            res=fastSolver.solve(task)
            s=s+task.accesses
            e=e+len(res)
        print '{0:5} {1:8} {2:5.3} {3:5.3}'.format(sz, s/exps, s/exps/sz, e/exps/sz)
