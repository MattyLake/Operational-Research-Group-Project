import numpy as np
c = -np.array([1, 4, 7, 5])
A = np.array([[2, 1, 2, 4], [3, -1, -2, 6]])
b = np.array([10, 5])
signs = np.array([-1,0]) # 1 is >= , -1 is <= , 0 is =
basicIndicies=np.array([])
artificalIndicies=np.array([])
numConstraints=len(signs)
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



print(A)
print(basicIndicies)
print(artificalIndicies)