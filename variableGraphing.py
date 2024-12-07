import numpy as np
from main import revisedSimplexMethod
import matplotlib.pyplot as plt
from bfs import convertToCanonicalForm,renderLLP
from itertools import cycle

colours = ['black', 'g', 'b','r','c','m','y']

bArray=[]
solutionArray=[]
nature = 1  # 1 is minimization, -1 is maximization
c = nature * np.array([7, 6])
A = np.array([[2, 4], [3, 2]])
signs = np.array([-1, -1])  # 1 is >= , -1 is <= , 0 is =
tempArray=[]



for i in range (1,25):
    b=np.array([i,12])
    cNew, ANew, bNew, signsNew, basicIndicesNew, artificialIndicesNew = convertToCanonicalForm(nature,c, A, b, signs)
    renderLLP(nature,c, A, b, signs)

    solution,solutionVal=revisedSimplexMethod(ANew,bNew,cNew,basicIndicesNew)
    bArray.append(i)
    solutionArray.append(solution)

for i in range(0,len(solutionArray[0])):
    tempArray=[]
    for j in range(0,len(solutionArray)):
        tempArray.append(solutionArray[j][i])
    plt.scatter(bArray, tempArray, label='x_'+str(i+1), s=20, marker='x',color=colours[i],alpha=0.6)



plt.xlabel('b Value')
plt.ylabel('Value in Solution')
plt.legend()
plt.title("Values of variables in solution varying b value in constraints")
plt.show()
