from collections import Counter


def counter_examples():
    repeated_letters = 'abdegadlbdaalg'
    cn = Counter(repeated_letters)
    print("Counter Ob:", cn)
    elem = cn.elements()
    print("Counter Object:", list(elem))
    com_2 = cn.most_common(2)
    print("2 Most Common:", com_2)
    sub_map = dict(a=2, d=2, e=1)
    cn.subtract(sub_map)
    print("After_Substraction ", cn)
    com_2 = cn.most_common(2)
    print("2 Most Common:", com_2)



if __name__ == '__main__':
    counter_examples()
