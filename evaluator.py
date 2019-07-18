import inspect
import timeit
from radon.complexity import cc_visit
from radon.metrics import mi_visit


def evaluate_code(kata_test, kata_implementation, kata_path):
    """
    Evaluate the code resulting from executing the kata_implementation stared at the given path
    :param kata_test: the test to pass
    :param kata_implementation: the kata implementation
    :param kata_path: the kata script
    """
    time_consumption = timeit.timeit(lambda: kata_test(kata_implementation), number=10000)
    with open(kata_path, "r") as kata_file:
        kata_code = kata_file.read()
    mantainability_index = mi_visit(kata_code, False)
    cyclomatic_complexity = cc_visit(kata_code)[0].complexity
    return {"time": time_consumption, "mi": mantainability_index, "cc": cyclomatic_complexity}