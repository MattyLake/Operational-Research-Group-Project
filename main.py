import numpy as np
from simplex import revised_simplex
from bfs import convertToCanonicalForm, renderLLP

# ------------------------- Enter LLP Below Line --------------------------------

nature = 1                                             # CW Example // Solution should be 200
c = nature * np.array([7, 0, 11, -10, -1, 26])
A = np.array([[1, -1, 1, 0, 1, 1], [0, 1, -1, 1, 0, 3], [1, 1, -3, 1, 1, 0], [1, 1, 0, 0, 0, 1]])
b = np.array([76, 18, 12, 50])
signs = np.array([0, -1, -1, 1])  # 1 is >= , -1 is <= , 0 is =

# ------------------------- Enter LLP Above Line --------------------------------


cNew, ANew, bNew, basicIndices, artificialIndices = convertToCanonicalForm(c, A, b, signs)
print("c: ", cNew)
print("A:\n ", ANew)
print("b: ", bNew)
print("Basic: ", basicIndices)
print("Artificial: ", artificialIndices)

# TODO: decide how we're going to use renderLLP
# TODO: Round floating point numbers to decimal places

ans = revised_simplex(cNew, ANew, bNew, basicIndices)

if ans['status'] == "Unbounded solution":
    print("Unbounded solution")
else:
    print("Optimal Value: ", nature*ans['optimal_value'])
    print("Optimal Solution: ", ans['x'])
    print("Status: ", ans['status'])


