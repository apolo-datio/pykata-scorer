import shlex

import functools
 

def digital_root(n):
    return n if n <= 9 else digital_root(sum([int(x) for x in str(n)]))

def test_main():
    assert digital_root(493193) == 2
    assert digital_root(9) == 9
    assert digital_root(132189) == 6
    assert digital_root(942) == 6

if __name__ == "__main__":
    # Execute from the command line as follows:
    # $ python -m radon cc -s -a paths radon_test.py
    # $ python -m radon mi -s paths radon_test.py
    test_main()
