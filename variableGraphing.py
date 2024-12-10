import numpy as np
from simplex import revisedSimplexMethod
import matplotlib.pyplot as plt
from bfsGraphing import convertToCanonicalForm



# ------------------------- Enter LPP Below Line --------------------------------

nature = 1 # 1 for minimisation, -1 for maximisation
c = nature * np.array([7, 0, 11, -10, -1, 26]) # objective function
A = np.array([[1, -1, 1, 0, 1, 1], [0, 1, -1, 1, 0, 3], [1, 1, -3, 1, 1, 0], [1, 1, 0, 0, 0, 1]])
b = np.array([76, 18, 200,50])
signs = np.array([0, -1, -1, 1] ) # # 1 is >= , -1 is <= , 0 is =

# ------------------------- Enter LPP Above Line --------------------------------

bVaryNum=4 # Pick constraint number to vary b in starting from 1,2,3 etc


colours = ['black', 'g', 'b','r','c','m','y']
bArray=[]
solutionArray=[]
tempArray=[]


for i in range (1,200):
    feasible=True
    b[bVaryNum-1]=i # Varies chosen b value between 1 and 200

    # Converts LPP to canonical form and finds solution
    cNew, ANew, bNew,signsNew, basicIndicesNew, artificialIndices,validInput = convertToCanonicalForm(c, A, b, signs)
    solution = revisedSimplexMethod(cNew, ANew, bNew, basicIndicesNew)


    # Checks if input is valid and ensures the solution found is feasible
    if solution['status'] == "Unbounded solution":
        print("Unbounded solution")

    else:
        if len(artificialIndices) > 0:
            for m in range(0, len(artificialIndices)):
                if solution['x'][artificialIndices[m]] != 0:  # Feasibility check ( Artificial variables should =0 in equation)
                    feasible = False

        # If found solution is feasible add it to solutionArray as well as the current b value
        if feasible == True:
            bArray.append(i)
            solutionArray.append(solution['x'])

# Loops through solution array (number of times decided by number of variables in initial question) and plots points in scatter
for i in range(0,len(c)):
    tempArray=[]
    for j in range(0,len(solutionArray)):
        tempArray.append(solutionArray[j][i])

    plt.scatter(bArray, tempArray, label='x_'+str(i+1), s=2, marker='o',color=colours[i]) # points belonging to the same variables in solution array assigned same color

#Displays final graph with visible key
plt.xlabel('b Value')
plt.ylabel('Value in Solution')
lgnd=plt.legend(fontsize=10,loc='upper left',fancybox=True,shadow=True,bbox_to_anchor=(1,0.5),)
for i in range(0,len(c)):
    lgnd.legend_handles[i]._sizes=[30]
plt.title("Values of variables in solution varying b value in constraint: "+str(bVaryNum))
plt.tight_layout()
plt.show()
