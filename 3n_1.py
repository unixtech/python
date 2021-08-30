# from pandas import pd
import random

x = random.randint(1, 200000)
N = int(x)
print(N)
K = 0


while(True):
    K = K+1
    if (N == 1):
        break
    elif (N % 2 == 0):
        N = N/2
    else:
        N = 3*N + 1


print(f"K is {K} for {x}")
# This is added to own1 branch so we can checkout random changes
