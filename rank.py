from pathlib import Path
import importlib
import sys
from evaluator import evaluate_code

def get_kata_test(kata: str):
    """
    Get kata test
    """
    import kata_tests
    test_module = importlib.import_module("kata_tests.%s" % kata)
    return test_module.kata_test


def evaluate_candidates(kata_test):
    """
    Evaluate the candidates and return their evaluations
    """
    import os
    participants = Path("participants")
    for p_script in participants.glob("*.py"):
        print("TESTING %s" % p_script)
        modulename, extension = os.path.splitext(os.path.basename(str(p_script.absolute())))
        participant_module = importlib.import_module("participants.%s" % modulename)
        try:
            kata_test(participant_module.sum_dig_pow)
        except AssertionError as e:
            print("TEST FAILED! %s" % e)
        else:
            print(evaluate_code(kata_test, participant_module.sum_dig_pow, str(p_script.absolute())))


if __name__ == "__main__":
    kata_test = get_kata_test(sys.argv[1])
    results = evaluate_candidates(kata_test)
    print(results)