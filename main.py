import numpy as np
from bfs import convertToCanonicalForm
from bfs import renderLLP

def revisedSimplexMethod(A, b, c, initialBasicIndices):
    # Initialize indices
    B = initialBasicIndices  # Indices of the basic variables#
    N = [i for i in range(len(c)) if i not in B]  # Indices of non-basic variables

    # Basis and non-basic matrices
    BMatrix = A[:, B]
    NMatrix = A[:, N]

    # Solution vector
    x = np.zeros(len(c))

    # Initial basic feasible solution
    x[B] = np.linalg.solve(BMatrix, b)

    while True:
        # Compute reduced costs
        cB = c[B]
        cN = c[N]

        y = np.linalg.solve(BMatrix.T, cB)
        reducedCosts = cN - y @ NMatrix

        # Check for optimality
        if all(reducedCosts <= 0):
            # Optimal solution found
            x[B] = np.linalg.solve(BMatrix, b)
            optimalValue = cB @ x[B]
            return x, optimalValue

        # Determine entering variable
        enteringIndex = np.argmax(reducedCosts)
        enteringVariable = N[enteringIndex]

        # Determine leaving variable
        ratios = np.zeros(len(b))
        for i in range(len(b)):
            if A[i, enteringVariable] > 0:
                ratios[i] = x[B[i]] / A[i, enteringVariable]
            else:
                ratios[i] = np.inf

        leavingIndex = np.argmin(ratios)
        leavingVariable = B[leavingIndex]

        # Update basis
        B[leavingIndex] = enteringVariable
        N[enteringIndex] = leavingVariable

        BMatrix = A[:, B]
        x[B] = np.linalg.solve(BMatrix, b)


# ------------------------- Enter LLP Below --------------------------------

# nature = 1  # 1 is maximization, -1 is minimization    # READY-MIKKS EXAMPLE // Solution should be 21
# c = nature * np.array([5, 4])
# A = np.array([[6, 4], [1, 2], [-1, 1], [0, 1]])
# b = np.array([24, 6, 1, 2])
# signs = np.array([-1, -1, -1, -1])  # 1 is >= , -1 is <= , 0 is =

# nature = -1  # -1 is maximization, 1 is minimization     # BOOK EXAMPLE
# c = np.array([4, 1])
# A = np.array([[3, 1], [4, 3], [1, 2]])
# b = np.array([3, 6, 4])
# signs = np.array([0, 1, -1])  # 1 is >= , -1 is <= , 0 is =

# nature = -1  # 1 is maximization, -1 is minimization    # CW EXAMPLE
# c = np.array([7, 0, 11, -10, -1, 26])
# A = np.array([[1, -1, 1, 0, 1, 1], [0, 1, -1, 1, 0, 3], [1, 1, -3, 1, 1, 0], [1, 1, 0, 0, 0, 1]])
# b = np.array([76, 18, 12, 50])
# signs = np.array([0, -1, -1, 1])  # 1 is >= , -1 is <= , 0 is =

nature = -1  # 1 is maximization, -1 is minimization    # Video Example // Solution should be 16
c = np.array([6, -7, -4])
A = np.array([[2, 5, -1], [-1, 1, 2], [3, 2, 2]])
b = np.array([18, 14, 26])
signs = np.array([-1, 1, 0])  # 1 is >= , -1 is <= , 0 is =

# ------------------------- Enter LLP Above --------------------------------

print("Original LLP:")
renderLLP(nature, c, A, b, signs)

natureNew, c, A, b, signs, basicIndices = convertToCanonicalForm(nature, nature * c, A, b, signs)

print()
print("Canonical form:")
renderLLP(natureNew, c, A, b, signs)
solution, optimalValue = revisedSimplexMethod(A, b, c, basicIndices)

print()
print("Solution:")
print("Optimal value:", nature*optimalValue)
