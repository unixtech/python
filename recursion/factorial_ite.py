

def factorial_iterative_while(N):
    result = 1
    while N >= 1:
        result *= N
        N -=1 
    print(result)
    return result


def factorial_iterative_while(N: int) -> dict:
    result_dict = {}
    result = 1
    while N >= 1:
        result *= N
        N -= 1
        result_dict[N] = result
    print(result_dict.items())
    return result_dict


# assert factorial_iterative_while(10) == 3628800
# assert factorial_iterative_while(4) == 24


'''
Full support to the cause of the rest of the world there can be worked up our own way. 
You do understand the question, Your fucking game for good amount of time. 

'''
def factorial(n):
    if n <= 1:
        return 1
    else:
        # Recursive case
        return n * factorial( n - 1 )


print(factorial(4))
print(factorial(100))
