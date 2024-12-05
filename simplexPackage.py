import numpy as np
from scipy.optimize import linprog

c =-np.array([7, 6, 0, 0])

#define Aup,bup with constraints containing <= and Aeq,beq with constraints containing =
Aup=None
bup=None
Aeq = np.array([[2, 4, 1, 0], [3, 2, 0, 1]])
beq = np.array([16, 12])


res=linprog(c,Aup,bup,Aeq,beq)
print(-res.fun)
