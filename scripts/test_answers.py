# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 18:31:31 2024

@author: Antoine
"""
import os
import unittest
import importlib
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

def test_all(threshold = SOLVE_DURATION_THRESHOLD, n_dashes=N_DASHES):

    failed = 0
    passed = 0
    slow = 0
    remaining = len(ANSWERS)
    elapsed_time = 0.0
    results = ""

    # Print the header line for the last print statement
    print(f" elapsed_time : 0 \t Passed : 0 \t Failed : 0 \t Remaining : {remaining}", end='')

    for problem_number, problem_answer in ANSWERS.items():

        problem_number_str = str(problem_number).zfill(4)
        module_name = f"scripts.problem_{problem_number_str}"

        module = importlib.import_module(module_name)

        class_name = f"Problem{problem_number}"
        problem_class = getattr(module, class_name)
        
        start_time = perf_counter_ns()
        problem_instance = problem_class(**KWARGS[problem_number])
        answer = problem_instance.answer
        end_time = perf_counter_ns()
        
        duration = (end_time-start_time)*10**-9
        elapsed_time += duration

        if str(answer) == str(problem_answer):
            passed += 1
            if duration < threshold:
                results += colored(f"Problem {problem_number_str} : Passed \n",'green')
            else:
                slow += 1
                results += colored(f"Problem {problem_number_str} : Passed {duration} s \n",'yellow')
        else:
            failed += 1
            results += colored(f"Problem {problem_number_str} : Failed \n",'red')

        remaining -= 1
        os.system('cls')
        print(results)
        print()  # Print an empty line
        print(f"\r elapsed_time : {elapsed_time} s \t Passed : {passed} \t Failed : {failed} \t Slow : {slow} \t Remaining : {remaining}", end='')

            

if __name__ == '__main__':
    TestProblems()
