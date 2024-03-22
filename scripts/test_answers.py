# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 18:31:31 2024

@author: Antoine
"""

import unittest
import importlib
from termcolor import colored

from util.const import ANSWERS, KWARGS

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

def test_all(n_dashes = 50):
    print('-' * n_dashes + " TESTING " + '-' * n_dashes)
    for problem_number in ANSWERS.keys():
        
        problem_number_str = str(problem_number).zfill(4)
        module_name = f"scripts.problem_{problem_number_str}"
        
        # script = __import__(script_name)
        module = importlib.import_module(module_name)

        class_name = f"Problem{problem_number}"
        problem_class = getattr(module, class_name)

        problem_instance = problem_class(**KWARGS[problem_number])
        answer = problem_instance.answer
        
        if str(answer) == str(ANSWERS[problem_number]):
            print(colored(f"Problem {problem_number_str} : Passed",'green'))
        else:
            print(colored(f"Problem {problem_number_str} : Failed",'red'))
            
    print('-' * (2*n_dashes + 9))

if __name__ == '__main__':
    TestProblems()
