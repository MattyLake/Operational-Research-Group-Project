import numpy as np
from scipy.optimize import linprog

c =-np.array([1, 4, 7,5])

#define Aup,bup with constraints containing <= and Aeq,beq with constraints containing =
Aup=None
bup=None
Aeq = np.array([[2, 1, 2, 4], [3, -1, -2, 6]])
beq = np.array([10, 5])


res=linprog(c,Aup,bup,Aeq,beq)
print(res.fun)
