import numpy as np
from scipy.optimize import linprog

c = np.array([7, 0, 11, -10,-1,26])

#define Aup,bup with constraints containing <= and Aeq,beq with constraints containing =
Aup=np.array([[0,1,-1,1,0,3],[1,1,-3,1,1,0],[-1,-1,0,0,0,-1]])
bup= np.array([18,12,-50])
Aeq = np.array([[1, -1, 1, 0,1,1]])
beq = np.array([76])


res = linprog(c,Aup,bup,Aeq,beq)
print(res)
