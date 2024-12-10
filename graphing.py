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


colours = ['black', 'g', 'b','r','c','m','y']
bArray=[] # Stores feasible values of b
solutionArray=[] # Stores solutions varying b

for j in range(0,len(b)):
    solutionArray=[] # Resets after each iteration
    bArray=[]
    b = np.array([76, 18, 12, 50])
    for i in range (1,200):
        feasible=True
        b = np.array([76, 18, 12, 50])
        b[j]=i # Varies b from 1 to 200 for each constraint

        # Converts LPP to canonical form and finds solution
        cNew, ANew, bNew,signsNew, basicIndicesNew, artificialIndices,validInput = convertToCanonicalForm(c, A, b, signs) #converts LPP to canonical form
        solution = revisedSimplexMethod(cNew, ANew, bNew, basicIndicesNew)

        # Checks if input is valid and ensures the solution found is feasible
        if validInput:
            if solution['status'] == "Unbounded solution":
                print("Unbounded solution")

            else:
                if len(artificialIndices) > 0:
                    for m in range(0, len(artificialIndices)):
                        if solution['x'][artificialIndices[m]] != 0:  # Feasibility check ( Artificial variabled should =0 in equation)
                            feasible = False

                # If found solution is feasible add it to solutionArray as well as the current b value
                if feasible == True:
                    bArray.append(i)
                    solutionArray.append(solution['optimal_value'])


    #Plots points of solutions for current constraint in scatter with the color depending on current constraint number
    plt.scatter(bArray, solutionArray, label='Constraint: '+str(j+1), s=2, marker='o',color=colours[j])



#Displays final graph with visible key
plt.xlabel('b Value')
plt.ylabel('Solution')
lgnd=plt.legend(fontsize=10,loc='upper left',fancybox=True,shadow=True,bbox_to_anchor=(1,0.5),)
for i in range(0,len(b)):
    lgnd.legend_handles[i]._sizes=[30]
plt.title("Solution varying b value in each constraint ")
plt.tight_layout()
plt.show()
