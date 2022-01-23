import pandas as pd
import random
import json



# while(True):
    # K = K+1
    # if (N == 1):
        # break
    # elif (N % 2 == 0):
        # N = N/2
    # else:
        # N = 3*N + 1


# print(f"K is {K} for {x}")

x = random.randint(1, 100)
N = int(x)
print(N)


def col_con(NUM: int) -> int:
    K = 0
    while(True):
        K = K + 1
        if (NUM == 1):
            break
        elif (NUM % 2 == 0):
            NUM = N/2
        else:
            NUM = 3*N + 1

    C = dict(K, NUM)
    with open('sample.json', 'w') as outfile:
        json.dump(C, outfile)
    # pd.to_json(C)
    return C


if __name__ == '__main__':
    col_con(N)
