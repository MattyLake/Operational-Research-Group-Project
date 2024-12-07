import numpy as np


def changeToStandardForm(c, A, b, signs):
    #TODO: Fix M when 0 coefficient is in objective function
    M = 1000000

    for j in range(0, len(A[1])):
        for i in range(0, len(A)):
            if A[i,j]!=0:
                M = abs(M * A[i, j])
        if c[j]!=0:
            M=abs(M*c[j])



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
        if signs[i] == -1:
            newColumn = np.zeros((numConstraints, 1))
            for j in range(0, numConstraints):
                if j == i:
                    newColumn[j, 0] = 1
                    A = np.append(A, newColumn, axis=1)
                    basicIndices = np.append(basicIndices, len(A[1]) - 1)
                    c = np.append(c, 0)
            signs[i] = 0

        elif signs[i] == 1:
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
            signs[i] = 0

        elif signs[i] == 0:
            newColumn = np.zeros((numConstraints, 1))
            for j in range(0, numConstraints):
                if j == i:
                    newColumn[j, 0] = 1
                    A = np.append(A, newColumn, axis=1)
                    basicIndices = np.append(basicIndices, len(A[1]) - 1)
                    artificalIndices = np.append(artificalIndices, len(A[1]) - 1)
                    c = np.append(c, M)

    if nature == -1:
        c = -c
        nature = 1

    return c, A, b, signs, basicIndices.astype(int), artificalIndices.astype(int)


def renderLLP(nature, c, A, b, signs):
    if nature == 1:
        print("maximize ", end="")
    elif nature == -1:
        print("minimize ", end="")
    for i in range(len(c)):
        print(c[i], "x_" + str(i), end="")
        if i != len(c) - 1:
            print(" + ", end="")
    print("\nsubject to ")
    for i in range(len(b)):
        for j in range(len(A[i])):
            print(A[i][j], "x_" + str(j), end="")
            if j != len(A[i]) - 1:
                print(" + ", end="")
        if signs[i] == -1:
            print(" <=", b[i])
        elif signs[i] == 1:
            print(" >=", b[i])
        else:
            print(" =", b[i])

# nature = -1  # 1 is minimization, -1 is maximization
# c = nature * np.array([1, 4, 7, 5])
# A = np.array([[2, 1, 2, 4], [3, -1, -2, 6]])
# b = np.array([10, 5])
# signs = np.array([-1,0])  # 1 is >= , -1 is <= , 0 is =
#
# c,A,b,basicIndicies,artificalIndicies = changeToStandardForm(c,A,b,signs)


# print(A)
# print(basicIndicies)
# print(artificalIndicies)

# c = -np.array([1, 4, 7,3])
# A = np.array([[2, 1, 2, 3], [3, 1, -2, 2]])
# b = np.array([10, 5])
# signs = np.array([-1,0]) # 1 is >= , -1 is <= , 0 is =

# c,A,b,basicIndicies,artificalIndicies = changeToStandardForm(c,A,b,signs)
#
# print(c)
# print(A)
# print(basicIndicies)
# print(artificalIndicies)
