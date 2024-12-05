import numpy as np
from bfs import changeToStandardForm
from bfs import renderLLP

def revised_simplex(c, A, b, initial_B_idx):
    m, n = A.shape

    # Initialize indices
    B_idx = initial_B_idx  # Indices of the basic variables
    N_idx = [i for i in range(n) if i not in B_idx]  # Indices of non-basic variables

    B = A[:, B_idx]  # Basis matrix
    N = A[:, N_idx]  # Non-basic columns

    x = np.zeros(n)  # Solution vector
    x[B_idx] = np.linalg.solve(B, b)  # Initial basic feasible solution

    while True:
        # Compute reduced costs
        c_B = c[B_idx]
        c_N = c[N_idx]

        y = np.linalg.solve(B.T, c_B)
        reduced_costs = c_N - y @ N

        # Check for optimality
        if all(reduced_costs <= 0):
            # Optimal solution found
            x[B_idx] = np.linalg.solve(B, b)
            optimal_value = c @ x
            return x, optimal_value
            # return optimal solution

        # Determine entering variable
        entering_idx = np.argmax(reduced_costs)
        entering_var = N_idx[entering_idx]

        # Determine leaving variable
        ratios = np.zeros((len(b), 1))
        for i in range(len(b)):
            if A[i][entering_idx] > 0:
                ratios[i] = b[i] / A[i][entering_idx]
            else:
                ratios[i] = np.inf

        leaving_idx = np.argmin(ratios)
        leaving_var = B_idx[leaving_idx]

        # Update basis

        B_idx[leaving_idx] = entering_var
        N_idx[entering_idx] = leaving_var

        B = A[:, B_idx]
        N = A[:, N_idx]

# ----------------------- Enter the LLP below this line ----------------------- #

nature = 1  # 1 is minimization, -1 is maximization
c = nature * np.array([7, 6])
A = np.array([[2, 4], [3, 2]])
b = np.array([16, 12])
signs = np.array([-1, -1])  # 1 is >= , -1 is <= , 0 is =

# ----------------------- Enter the LLP above this line ----------------------- #

renderLLP(c, A, b, signs)
c, A, b, signs, basicIndices, artificialIndices = changeToStandardForm(c, A, b, signs)
print()
renderLLP(c, A, b, signs)

x, optimal_value = revised_simplex(c, A, b, basicIndices)

print()
print("Optimal solution:", x)
print("Optimal value:", optimal_value)