
import numpy as np

def float_format(n):

    A=np.array(n.split(','),dtype=float)

    return np.ceil(A) , np.floor(A) , np.rint(A)


