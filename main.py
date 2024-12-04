import numpy as np
from bfs import changeToStandardForm
from bfs import renderLLP

# ----------------------- Enter the LLP below this line ----------------------- #

nature = -1  # 1 is minimization, -1 is maximization
c = nature * np.array([6, 1])
A = np.array([[-1, 3], [1, -3], [1, 1]])
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

print("cB: ", cB)
print("cNB: ", cNB)

Binverse = np.linalg.inv(B)

for i in range(len(basicIndices)):
    print("x", basicIndices[i], " = ", b[i])

print(cB @ Binverse @ A - c)
if np.any(cB @ Binverse @ A - c) < 0:
    print("Finished")
else:
    # Find the entering variable
    enteringIndex = np.argmin(cB @ Binverse @ A - c)
    enteringVariable = nonBasicIndices[enteringIndex]
    print("Entering Variable: ", enteringVariable)

    # Find the leaving variable
    ratios = [] # Finding the smallest positive ratio
    for i in range(len(b)):
        if B[i, enteringIndex] > 0:
            ratios.append(b[i] / B[i, enteringIndex])
        else:
            ratios.append(np.inf)
    ratios = np.array(ratios)
    leavingIndex = np.argmin(ratios)
    leavingVariable = basicIndices[leavingIndex]
    print("Leaving Variable: ", leavingVariable)

    # Update the basic and non-basic indices
    basicIndices[leavingIndex] = enteringVariable
    nonBasicIndices[enteringIndex] = leavingVariable
    print("Basic Indices: ", basicIndices)
    print("Non-Basic Indices: ", nonBasicIndices)

    # Update B and Atilde
    B = A[:, basicIndices]
    Atilde = A[:, nonBasicIndices]

    print("B: \n", B, "\n")
    print("Atilde: \n", Atilde, "\n")

    # Update cB and cNB
    cB = c[basicIndices]
    cNB = c[nonBasicIndices]


