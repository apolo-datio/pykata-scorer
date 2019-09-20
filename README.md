# Measuring your code

The following document will show how your code can be measured in order to determiner what is good, what isn't and how it can be improved.

## Measuring Execution time with `timeit`

_timeit_ module allows measuring the time consumed for executing small pieces of code, either through its CLI interface or programatically through its timer objects.

```bash
python -m timeit -s "from timeit_test import test_main" "test_main()"
```

```python
import timeit
time_results = timeit.timeit(test_main)
```

It allows defining several parameters like:

 * The number of executions to perform
 * A previous setup before performing the execution

## Static code metrics using Radon

_radon_ package provides the implementation of four static code metrics aimed at analuysing your code:

 * Cyclomatic complexity
 * RAW code metrics
 * Halstead metrics
 * Maintainability index: This is a combination of the previously listed metrics.

As with timeit, radon can be used programatically or throug its 


```bash
python -m radon cc -s -a paths radon_test.py
```

```bash
python -m radon mi -s paths radon_test.py
```


##Basic Instructions

###Step 1

In folder "participants" leave the corresponding .py files.

###Step 2

In folder kata_tests change the assert list and "def".

###Step 3

In rank.py leave def and kata_test = get_kata_test("kataX") to which it corresponds.
Run rank.py

