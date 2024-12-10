import numpy as np


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
        M = M + abs(c[i])
    signsNewer = signs

    # Validation of input, if invalid return 0
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
    for i in range(0, numConstraints):
        if signs[i] == -1:  # <=
            newColumn = np.zeros((numConstraints, 1))
            for j in range(0, numConstraints):
                if j == i:
                    newColumn[j, 0] = 1
                    A = np.append(A, newColumn, axis=1)
                    basicIndices = np.append(basicIndices, len(A[1]) - 1)
                    c = np.append(c, 0)

        elif signs[i] == 1:  # >=
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
                    artificialIndices = np.append(artificialIndices, len(A[1]) - 1)
                    c = np.append(c, M)

        elif signs[i] == 0:  # =
            newColumn = np.zeros((numConstraints, 1))
            for j in range(0, numConstraints):
                if j == i:
                    newColumn[j, 0] = 1
                    A = np.append(A, newColumn, axis=1)
                    basicIndices = np.append(basicIndices, len(A[1]) - 1)
                    artificialIndices = np.append(artificialIndices, len(A[1]) - 1)
                    c = np.append(c, M)


    return c, A, b, signsNewer, basicIndices.astype(int), artificialIndices.astype(int), validInput