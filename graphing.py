import numpy as np
from main import revised_simplex
import matplotlib.pyplot as plt
from bfs import changeToStandardForm,renderLLP

bArray=[]
solutionArray=[]



for i in range (1,25):
    nature = 1  # 1 is minimization, -1 is maximization
    c = nature * np.array([7, 6])
    A = np.array([[2, 4], [3, 2]])
    signs = np.array([-1, -1])  # 1 is >= , -1 is <= , 0 is =
    b=np.array([i,12])
    c, A, b, signs, basicIndices, artificialIndices = changeToStandardForm(c, A, b, signs)
    renderLLP(c, A, b, signs)

    solution,solutionVal=revised_simplex(c,A,b,basicIndices) #return solution here and append to list (add feasible solutions)
    print("sol",solutionVal)
    bArray.append(i)
    solutionArray.append(solutionVal)


print(bArray)
print(solutionVal)
plt.scatter(bArray,solutionArray)
plt.xlabel('b value')
plt.ylabel('Solution')
plt.title("Solutions varying first constraint")
plt.show()
