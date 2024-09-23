#Floor, Ceil and Rint

import numpy as np

def float_format():

    A=np.array(input().split(','),dtype=float)

    return np.ceil(A) , np.floor(A) , np.rint(A)


