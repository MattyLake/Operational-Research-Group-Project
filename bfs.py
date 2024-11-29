import numpy as np

def changeToStandardForm(c,A,b,signs):
    # TODO: Validation of input
    # TODO: Add additional rows for artificial variables and slack variables

    basicIndicies = np.array([])
    artificalIndicies = np.array([])
    numConstraints = len(signs)
    for i in range(0,numConstraints):
        if signs[i]==-1:
            newColumn=np.zeros((numConstraints,1))
            for j in range(0,numConstraints):
                if j==i:
                    newColumn[j,0]=1
                    A=np.append(A,newColumn,axis=1)
                    basicIndicies=np.append(basicIndicies,len(A[1])-1)

        elif signs[i]==1:
            for j in range(0,numConstraints):
                newColumn=np.zeros((numConstraints,1))
                if j==i:
                    newColumn[j,0]=-1
                    A=np.append(A,newColumn,axis=1)
                    newColumn=np.zeros((numConstraints,1))
                    newColumn[j,0]=1
                    A=np.append(A,newColumn,axis=1)
                    basicIndicies=np.append(basicIndicies,len(A[1])-1)
                    artificalIndicies = np.append(artificalIndicies, len(A[1]) - 1)

        elif signs[i]==0:
            newColumn=np.zeros((numConstraints,1))
            for j in range(0,numConstraints):
                if j==i:
                    newColumn[j,0]=1
                    A=np.append(A,newColumn,axis=1)
                    basicIndicies = np.append(basicIndicies, len(A[1]) - 1)
                    artificalIndicies = np.append(artificalIndicies, len(A[1]) - 1)

    return c,A,b,basicIndicies.astype(int),artificalIndicies.astype(int)


# nature = -1  # 1 is minimization, -1 is maximization
# c = nature * np.array([1, 4, 7, 5])
# A = np.array([[2, 1, 2, 4], [3, -1, -2, 6]])
# b = np.array([10, 5])
# signs = np.array([-1,0])  # 1 is >= , -1 is <= , 0 is =
#
# c,A,b,basicIndicies,artificalIndicies = changeToStandardForm(c,A,b,signs)
#
#
# print(A)
# print(basicIndicies)
# print(artificalIndicies)