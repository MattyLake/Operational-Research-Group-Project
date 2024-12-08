import numpy as np

def revisedSimplexMethod(c, A, b, basic_vars):

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
        print(f"Direction vector d_B: {d_B}")
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