import shlex

import functools
 
def bfajardo_digital_root(n):
    if len(str(n)) == 1:
        return n
    else:
        partial_sum = functools.reduce(lambda x,y: str(int(x)+int(y)), str(n))
        return digital_root(int(partial_sum))


def digital_root(n):
    nList = [int(i) for i in list(str(n))]
    import functools
    import operator
    foldl = lambda func, acc, xs: functools.reduce(func, xs, acc)
    aux = 0
    while len(nList) > 1: 
        aux = foldl(operator.add, 0, nList)
        nList = [int(i) for i in list(str(aux))]
    return aux



def test_main():
    assert digital_root(493193) == 2
    assert digital_root(9) == 9
    assert digital_root(132189) == 6
    assert digital_root(942) == 6

if __name__ == "__main__":
    # Execute from the command line as follows:
    # python -m timeit -s "from timeit_test import test_main" "test_main"
    import timeit
    timeit_res = timeit.timeit(test_main)
    print(timeit_res)
