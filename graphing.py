import numpy as np
from simplex import revisedSimplexMethod
import matplotlib.pyplot as plt
from bfs import convertToCanonicalForm


colours = ['black', 'g', 'b','r','c','m','y']

bArray=[]
solutionArray=[]
nature = 1                                             # CW Example // Solution should be 200# CW Example // Solution should be 200
c = nature * np.array([7, 0, 11, -10, -1, 26])
A = np.array([[1, -1, 1, 0, 1, 1], [0, 1, -1, 1, 0, 3], [1, 1, -3, 1, 1, 0], [1, 1, 0, 0, 0, 1]])
b = np.array([76, 18, 12, 50])
signs = np.array([0, -1, -1, 1])  # 1 is >= , -1 is <= , 0 is =
tempArray=[]

for j in range(0,len(b)):
    solutionArray=[]
    bArray=[]
    for i in range (1,100):
        b = np.array([76, 18, 12, 50])
        b[j]=i
        cNew, ANew, bNew,signsNew, basicIndicesNew, artificialIndices,validInput = convertToCanonicalForm(c, A, b, signs)

        solution = revisedSimplexMethod(cNew, ANew, bNew, basicIndicesNew)
        bArray.append(i)
        solutionArray.append(solution['optimal_value'])
    for i in range(0,len(solutionArray)):
        print(solutionArray[i])


    plt.scatter(bArray, solutionArray, label='Constraint: '+str(j+1), s=2, marker='o',color=colours[j])



plt.xlabel('b Value')
plt.ylabel('Solution')
lgnd=plt.legend(fontsize=10,loc='upper left',fancybox=True,shadow=True,bbox_to_anchor=(1,0.5),)
#for i in range(0,len(c)):
    #lgnd.legend_handles[i]._sizes=[30]
plt.title("Solution varying b value in each constraint ")
plt.tight_layout()
plt.show()

