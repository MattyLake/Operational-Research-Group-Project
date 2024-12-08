import numpy as np
from main import revisedSimplexMethod
def convertToCanonicalForm( c, A, b, signs):
    M = 1000
    for i in range(len(c)):
        M =M+abs(c[i])

    validInput = True
    for i in range(0, len(b)):
        if b[i] < 0:
            validInput = False
        if not (signs[i] == 1 or signs[i] == 0 or signs[i] == -1):
            validInput = False

    if not (len(A) == len(b) == len(signs)) or validInput == False or not (len(c) == len(A[0])):
        print("Invalid Input.")
        return c, A, b, 0, 0, 0

    basicIndices = np.array([])
    artificalIndices = np.array([])
    numConstraints = len(signs)
    for i in range(0, numConstraints):
        if signs[i] == -1: # <=
            newColumn = np.zeros((numConstraints, 1))
            for j in range(0, numConstraints):
                if j == i:
                    newColumn[j, 0] = 1
                    A = np.append(A, newColumn, axis=1)
                    basicIndices = np.append(basicIndices, len(A[1]) - 1)
                    c = np.append(c, 0)

        elif signs[i] == 1: # >=
            for j in range(0, numConstraints):
                newColumn = np.zeros((numConstraints, 1))
                if j == i:
                    newColumn[j, 0] = -1
                    A = np.append(A, newColumn, axis=1)
                    c = np.append(c, 0)
                    newColumn = np.zeros((numConstraints, 1))
                    newColumn[j, 0] = 1
                    A = np.append(A, newColumn, axis=1)
                    basicIndices = np.append(basicIndices, len(A[1]) - 1)
                    artificalIndices = np.append(artificalIndices, len(A[1]) - 1)
                    c = np.append(c, M)

        elif signs[i] == 0: # =
            newColumn = np.zeros((numConstraints, 1))
            for j in range(0, numConstraints):
                if j == i:
                    newColumn[j, 0] = 1
                    A = np.append(A, newColumn, axis=1)
                    basicIndices = np.append(basicIndices, len(A[1]) - 1)
                    artificalIndices = np.append(artificalIndices, len(A[1]) - 1)
                    c = np.append(c, M)

    return c, A, b,basicIndices.astype(int),artificalIndices.astype(int)

nature=1
c = nature*np.array([7, 0, 11, -10, -1, 26])
A = np.array([[1, -1, 1, 0, 1, 1], [0, 1, -1, 1, 0, 3], [1, 1, -3, 1, 1, 0], [1, 1, 0, 0, 0, 1]])
b = np.array([76, 18, 12, 50])
signs = np.array([0, -1, -1, 1])  # 1 is >= , -1 is <= , 0 is =


cNew,ANew,bNew,basicIndices,artificialIndices=convertToCanonicalForm(c,A,b,signs)
print("c: ", cNew)
print("A:\n ", ANew)
print("b: ", bNew)
print("Basic: ",basicIndices)
print("Artificial: ", artificialIndices)

#x,optimalValue=revisedSimplexMethod(ANew, bNew, cNew, basicIndices)

#print("x: ",x)
#print("optimalValue",optimalValue)

def revised_simplex(c, A, b, basic_vars):
    """
    Solves the linear programming problem using the Revised Simplex Method.

    Args:
        c (numpy.ndarray): Coefficients of the objective function.
        A (numpy.ndarray): Coefficient matrix of the constraints.
        b (numpy.ndarray): Right-hand side of the constraints.
        basic_vars (list): List of indices of the basic variables.

    Returns:
        solution: Dictionary with keys "optimal_value", "x", and "status".
    """
    # Initialize
    m, n = A.shape
    non_basic_vars = [i for i in range(n) if i not in basic_vars]
    iteration = 0

    while True:
        iteration += 1
        print(f"\nIteration {iteration}")

        # Partition A and c into basic and non-basic variables
        B = A[:, basic_vars]
        N = A[:, non_basic_vars]
        c_B = c[basic_vars]
        c_N = c[non_basic_vars]

        # Compute basic solution
        B_inv = np.linalg.inv(B)
        x_B = B_inv @ b

        # Compute reduced costs
        lambda_ = np.linalg.solve(B.T, c_B)  # Dual prices
        reduced_costs = c_N - (lambda_ @ N)

        print(f"Basic solution x_B: {x_B}")
        print(f"Reduced costs: {reduced_costs}")

        # Check for optimality
        if all(reduced_costs >= 0):
            x = np.zeros(n)
            x[basic_vars] = x_B
            optimal_value = c @ x
            return {
                "optimal_value": optimal_value,
                "x": x,
                "status": "Optimal solution found"
            }

        # Entering variable: Select the most negative reduced cost
        entering_index = np.argmin(reduced_costs)
        entering_var = non_basic_vars[entering_index]
        print(f"Entering variable: {entering_var}")

        # Compute direction vector d_B
        a_enter = N[:, entering_index]
        d_B = np.linalg.solve(B, a_enter)

        # Check for unboundedness
        if all(d_B <= 0):
            return {
                "status": "Unbounded solution"
            }

        # Determine the leaving variable
        ratios = np.array([
            x_B[i] / d_B[i] if d_B[i] > 0 else np.inf
            for i in range(len(d_B))
        ])
        leaving_index = np.argmin(ratios)
        leaving_var = basic_vars[leaving_index]
        print(f"Leaving variable: {leaving_var}")

        # Update basic and non-basic variables
        basic_vars[leaving_index] = entering_var
        non_basic_vars[entering_index] = leaving_var

print(revised_simplex(cNew,ANew,bNew,basicIndices))