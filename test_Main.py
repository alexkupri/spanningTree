from test_Models import ModelGenerator
from test_Solvers import getPairOfSolvers
import test_Experiments

def printhelp():
    print('Some large explaination here.')
    exit(0)

def makeExperiment(taskGen,fastSolver,slowSolver,name,parameter):
    if name=='correctness':
        test_Experiments.checkCorrectness(taskGen,fastSolver,slowSolver,parameter)
    elif name=='statistics':
        test_Experiments.showStatistics(taskGen,fastSolver,parameter)
    else:
        raise Exception('Unknown type of experiment.')

def mainf(par):
    if len(par)==0:
        printhelp()
    taskGen=ModelGenerator(par[0],par[1])
    fastSolver,slowSolver=getPairOfSolvers(par[2],par[3])
    makeExperiment(taskGen,fastSolver,slowSolver,par[4],par[5])
    
mainf(['cartesianU',2,'spanning',1,'statistics',4100])
#mainf(['cartesianU',2,'spanning',1,'correctness',20])
