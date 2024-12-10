import numpy as np

# Same as bfs.py however, sign change has been removed to avoid looping error in graphing

def convertToCanonicalForm(c, A, b, signs):
    """
        Converts the LPP to canonical form.

        Args:
            c (numpy.ndarray): Coefficients of the objective function.
            A (numpy.ndarray): Coefficient matrix of the constraints.
            b (numpy.ndarray): Right-hand side of the constraints.
            signs (numpy.ndarray): List of indices of the basic variables.

        Returns:
            c (numpy.ndarray): Canonical Coefficients of the objective function.
            A (numpy.ndarray): Canonical Coefficient matrix of the constraints.
            b (numpy.ndarray): Canonical Right-hand side of the constraints.
            signs (list): List of {0} of length of constraints.
            basicIndices (list): List of indices of the basic variables.
            artificalIndices (list): List of indices of the artificial variables.
        """
    M = 1000  # Big M
    for i in range(len(c)):
        M = M + abs(c[i]) # Ensures M is proportionally big compared to the inputted question
    signsNew = signs

    # Validation of input, if invalid return 0 (Checks dimensions are correct, b values are positive and sign values are valid)
    validInput = True
    for i in range(0, len(b)):
        if b[i] < 0:
            validInput = False
        if not (signs[i] == 1 or signs[i] == 0 or signs[i] == -1):
            validInput = False
    if not (len(A) == len(b) == len(signs)) or validInput == False or not (len(c) == len(A[0])):
        print("\nInvalid Input.     !Check LPP!")
        validInput=False
        return c, A, b, 0, 0, 0,validInput

    # Main conversion of constraints to canonical form
    basicIndices = np.array([])
    artificialIndices = np.array([])
    numConstraints = len(signs)

    # Loops through constraints adding slack,surplus and artificial variables where needed
    for i in range(0, numConstraints):

        # If sign is <= then it will add a single slack variable to LPP

        if signs[i] == -1:  # <=
            newColumn = np.zeros((numConstraints, 1))
            for j in range(0, numConstraints):
                if j == i:
                    newColumn[j, 0] = 1

                    # Adds slack variable to A in current constraint as and 0 in other constraints
                    A = np.append(A, newColumn, axis=1)
                    # Stores position of new slack variable in basicIndices as it is always an initial basic variable
                    basicIndices = np.append(basicIndices, len(A[1]) - 1)
                    # Adds 0 to c as the added slack variable is not in objective function but dimensions must be kept consistent
                    c = np.append(c, 0)

        # If sign is >= then it will add a surplus variable and an artificial variable to the LPP
        elif signs[i] == 1:  # >=
            for j in range(0, numConstraints):
                newColumn = np.zeros((numConstraints, 1))
                if j == i:
                    # Adds surplus variable to A in current constraint as and 0 in other constraints
                    newColumn[j, 0] = -1
                    A = np.append(A, newColumn, axis=1)
                    c = np.append(c, 0)

                    # Adds artificial variable the through the same method as a slack variable however M is added to objective function
                    newColumn = np.zeros((numConstraints, 1))
                    newColumn[j, 0] = 1
                    A = np.append(A, newColumn, axis=1)

                    # Stores position of artificial variable in basic and artifical Indices as it is always initially a basic variable
                    basicIndices = np.append(basicIndices, len(A[1]) - 1)
                    artificialIndices = np.append(artificialIndices, len(A[1]) - 1)
                    c = np.append(c, M)

        # If sign is = then it will add a single artificial variable
        elif signs[i] == 0:  # =
            newColumn = np.zeros((numConstraints, 1))
            for j in range(0, numConstraints):
                if j == i:
                    newColumn[j, 0] = 1
                    A = np.append(A, newColumn, axis=1)
                    basicIndices = np.append(basicIndices, len(A[1]) - 1)
                    artificialIndices = np.append(artificialIndices, len(A[1]) - 1)
                    c = np.append(c, M)


    return c, A, b, signsNew, basicIndices.astype(int), artificialIndices.astype(int), validInput