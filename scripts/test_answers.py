import os
import unittest
import importlib
import traceback

from termcolor import colored
from time import perf_counter_ns

from util.const import ANSWERS, KWARGS, N_DASHES, SOLVE_DURATION_THRESHOLD


class TestProblems(unittest.TestCase):
    def test_problems(self):
        for problem_number in ANSWERS.keys():

            problem_number_str = str(problem_number).zfill(4)
            module_name = f"problem_{problem_number_str}"
            module = importlib.import_module(module_name)

            class_name = f"Problem{problem_number}"
            problem_class = getattr(module, class_name)

            problem_instance = problem_class()
            answer = problem_instance.answer

            # Comparer l'attribut answer à la réponse connue
            self.assertEqual(answer, ANSWERS[problem_number])


def test_all(threshold=SOLVE_DURATION_THRESHOLD, n_dashes=N_DASHES):

    crashed = 0
    failed = 0
    passed = 0
    slow = 0
    remaining = len(ANSWERS.keys())
    elapsed_time = 0.0
    results = ""

    # Print the header line for the last print statement
    print(
        f" elapsed_time : 0 \t Passed : 0 \t Failed : 0 \t Remaining : {remaining}",
        end="",
    )

    for problem_number, problem_answer in ANSWERS.items():
        problem_number_str = str(problem_number).zfill(4)

        try:
            module_name = f"scripts.problem_{problem_number_str}"

            module = importlib.import_module(module_name)

            class_name = f"Problem{problem_number}"
            problem_class = getattr(module, class_name)

            start_time = perf_counter_ns()
            problem_instance = problem_class(**KWARGS[problem_number])
            end_time = perf_counter_ns()

            duration = (end_time - start_time) * 10**-9
            elapsed_time += duration

            if problem_instance.assert_answer():
                passed += 1
                if duration < threshold:
                    results += colored(
                        f"Problem {problem_number_str} : Passed \n", "green"
                    )
                else:
                    slow += 1
                    results += colored(
                        f"Problem {problem_number_str} : Passed {duration} s \n",
                        "yellow",
                    )
            else:
                failed += 1
                results += colored(f"Problem {problem_number_str} : Failed \n", "red")

        except Exception as e:
            crashed += 1
            tb_str = traceback.format_exc()  # Capture the traceback as a string
            results += colored(
                f"Problem {problem_number_str} : Crashed {type(e).__name__}\n{tb_str}\n",
                "blue",
            )
        remaining -= 1
        os.system("cls")
        print(results)
        print()  # Print an empty line
        print(
            f"\rTotal Time Taken : {elapsed_time:.4f} s \t Passed : {passed} \t Failed : {failed} \t Slow : {slow} \t Crashed : {crashed} \t Remaining : {remaining}",
            end="",
        )


if __name__ == "__main__":
    TestProblems()
