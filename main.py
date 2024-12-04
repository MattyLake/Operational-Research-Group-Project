import numpy as np
from bfs import changeToStandardForm
from bfs import renderLLP

# ----------------------- Enter the LLP below this line ----------------------- #

nature = -1  # 1 is minimization, -1 is maximization
c = nature * np.array([6, 1, 0])
A = np.array([[-1, 3, 0], [1, -3, 0], [1, 1, -1]])
b = np.array([6, 6, 1])
signs = np.array([-1,0,1])  # 1 is >= , -1 is <= , 0 is =

# ----------------------- Enter the LLP above this line ----------------------- #

renderLLP(c, A, b, signs)
print("-----------------------------------------------")
print("Converting to standard form...")
c, A, b, signs, basicIndices, artificialIndices = changeToStandardForm(c, A, b, signs)
renderLLP(c, A, b, signs)
print("Basic Indices: ", basicIndices)
print("Artificial Indices: ", artificialIndices)
print("-----------------------------------------------")

# Define the initial basic feasible solution
nonBasicIndices = [i for i in range(len(c)) if i not in basicIndices]

B = A[:, basicIndices]
Atilde = A[:, nonBasicIndices]

cB = c[basicIndices]
cNB = c[nonBasicIndices]

print("B: \n", B, "\n")
print("Atilde: \n", Atilde, "\n")