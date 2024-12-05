import numpy as np
from main import simplexMatrix
import matplotlib.pyplot as plt

nature = -1  # 1 is minimization, -1 is maximization
c = nature * np.array([7, 6])
A = np.array([[2, 4], [3, 2]])
b = np.array([16, 12])
signs = np.array([-1, -1])  # 1 is >= , -1 is <= , 0 is =
bArray=[]
solutionArray=[]
for i in range (1,25):
    b=np.array([i,12])
    solution=simplexMatrix(nature,c,A,b,signs) #return solution here and append to list (add feasible solutions)
    if solution != "unfeasible":
        bArray.append(i)
        solutionArray.append(solution)


plt.scatter(bArray,solutionArray)
plt.xlabel('b value')
plt.ylabel('Solution')
plt.title("Solutions varying first constraint")
plt.show()
