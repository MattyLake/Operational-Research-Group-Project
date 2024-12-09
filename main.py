import numpy as np
from simplex import revisedSimplexMethod
from bfs import convertToCanonicalForm, renderLPP

# ------------------------- Enter LPP Below Line --------------------------------

nature = 1                                             # CW Example // Solution should be 200
c = nature * np.array([7, 0, 11, -10, -1, 26])
A = np.array([[1, -1, 1, 0, 1, 1], [0, 1, -1, 1, 0, 3], [1, 1, -3, 1, 1, 0], [1, 1, 0, 0, 0, 1]])
b = np.array([76, 18, 12, 50])
signs = np.array([0, -1, -1, 1])  # 1 is >= , -1 is <= , 0 is =

# ------------------------- Enter LPP Above Line --------------------------------

tolerance = 1e-7
cCopy = c*nature
feasible=True

cNew, ANew, bNew, signsNew, basicIndices, artificialIndices, validInput = convertToCanonicalForm(c, A, b, signs)

if validInput:
    renderLPP(nature, cCopy, A, b, signs)
    print("\n\nConverting to Canonical Form..... \n\n")
    renderLPP(1, cNew, ANew, bNew, signsNew)

    ans = revisedSimplexMethod(cNew, ANew, bNew, basicIndices)
    if ans['status'] == "Unbounded solution":
        print("Unbounded solution")
    else:
        if len(artificialIndices)>0:
            for i in range(0,len(artificialIndices)):
                if ans['x'][artificialIndices[i]]!=0 : #Feasibility check ( Artificial variables should =0 in equation)
                    feasible=False
                    print("\n\n-------------------------------------------------\n")
                    print("Solution is Infeasible.")
                    print("\n-------------------------------------------------")
        if feasible==True:
            errorCheck = round(ans['optimal_value'])
            if abs(abs(errorCheck) - abs(ans['optimal_value']))<tolerance:
                ans['optimal_value'] = errorCheck
            else:
                ans['optimal_value'] = round(ans['optimal_value'],5)
            print("\n\n-------------------------------------------------\n")
            print("Optimal Value: ", nature * ans['optimal_value'])
            print("Optimal Solution: ", ans['x'])
            print("Status: ", ans['status'])
            print("\n-------------------------------------------------")
