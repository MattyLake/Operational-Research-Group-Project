import numpy as np
from main import revised_simplex
import matplotlib.pyplot as plt
from bfs import changeToStandardForm,renderLLP

bArray=[]
firstSolutionArray=[]
secondSolutionArray=[]
thirdSolutionArray=[]



for i in range (1,25):
    nature = 1  # 1 is minimization, -1 is maximization
    c = nature * np.array([7, 6])
    A = np.array([[2, 4], [3, 2]])
    signs = np.array([-1, -1])  # 1 is >= , -1 is <= , 0 is =
    b=np.array([i,12])
    c, A, b, signs, basicIndices, artificialIndices = changeToStandardForm(c, A, b, signs)
    renderLLP(c, A, b, signs)

    solution,solutionVal=revised_simplex(c,A,b,basicIndices)
    print("sol",solutionVal)
    bArray.append(i)
    firstSolutionArray.append(solutionVal)

for i in range (1,25):
    nature = 1  # 1 is minimization, -1 is maximization
    c = nature * np.array([7, 6])
    A = np.array([[2, 4], [3, 2]])
    signs = np.array([-1, -1])  # 1 is >= , -1 is <= , 0 is =
    b=np.array([16,i])
    c, A, b, signs, basicIndices, artificialIndices = changeToStandardForm(c, A, b, signs)
    renderLLP(c, A, b, signs)

    solution,solutionVal=revised_simplex(c,A,b,basicIndices)
    print("sol",solutionVal)
    secondSolutionArray.append(solutionVal)


plt.scatter(bArray,firstSolutionArray,color='blue',label='First b value',s=20,marker='x')
plt.scatter(bArray,secondSolutionArray,color='red',label='Second b value',s=20,marker='x')
plt.xlabel('b Value')
plt.ylabel('Solution')
plt.legend()
plt.title("Solutions varying b value in constraints")
plt.show()
