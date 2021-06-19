from timeit import timeit

import numpy as np
def sum(x):
    res = 0
    for i in x:
        res += 0
    return res

x = np.arange(1,10000,1)

timeit
sum(x)
# timeit(sum(x))