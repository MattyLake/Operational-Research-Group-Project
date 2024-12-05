import numpy as np
from bfs import changeToStandardForm
from bfs import renderLLP

# ----------------------- Enter the LLP below this line ----------------------- #

# nature = -1  # 1 is minimization, -1 is maximization
# c = nature * np.array([6, 1])
# A = np.array([[-1, 3], [1, -3], [1, 1]])
# b = np.array([6, 6, 1])
# signs = np.array([-1,0,1])  # 1 is >= , -1 is <= , 0 is =

nature = -1  # 1 is minimization, -1 is maximization
c = nature * np.array([7, 6])
A = np.array([[2, 4], [3, 2]])
b = np.array([16, 12])
signs = np.array([-1, -1])  # 1 is >= , -1 is <= , 0 is =

# ----------------------- Enter the LLP above this line ----------------------- #

renderLLP(c, A, b, signs)
print("-----------------------------------------------")
print("Converting to standard form...")
c, A, b, signs, basicIndices, artificialIndices = changeToStandardForm(c, A, b, signs)
renderLLP(c, A, b, signs)
print("Basic Indices: ", basicIndices)
print("Artificial Indices: ", artificialIndices)
print("-----------------------------------------------")

nonBasicIndices = [i for i in range(len(c)) if i not in basicIndices]


cB = c[basicIndices]

# For basic variables z represents unit contribution to the objective function
# For non-basic variables z represents the profit to give up if added to the basis
z = np.zeros((len(c), 1))
netEvaluation = c.reshape(-1, 1) - z

print("Net Evaluation: ", netEvaluation)

enteringIndex = np.argmin(netEvaluation)
print(enteringIndex)

ratios = np.zeros((len(b), 1))
for i in range(len(b)):
    if A[i][enteringIndex] > 0:
        ratios[i] = b[i] / A[i][enteringIndex]
    else:
        ratios[i] = np.inf

print("Ratios: ", ratios)
leavingIndex = np.argmin(ratios)

print("Entering Index: ", enteringIndex)
print("Leaving Index: ", basicIndices[leavingIndex])

basicIndices[leavingIndex] = enteringIndex

nonBasicIndices = [i for i in range(len(c)) if i not in basicIndices]
cB = c[basicIndices]

print("Basic Indices: ", basicIndices)
print("cB: ", cB)



print(A)



