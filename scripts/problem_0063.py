# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:15:49 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class Problem63(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        
        self.answer, self.time_taken = self.solve()
        
        self.detailed_answer = f"There are {format_number(self.answer[0])} n-digit positive integers that exist which are also an nth power \nThe complete list being {self.answer[1]}"
        
        # We returned two values for the detailed_answer
        self.answer = self.answer[0]
    
    @timing
    def solve(self, **kwargs):
        count = 0
        numbers = []
        for integer in range(1,10):
            # Kind of bruteforcing or I don't remember how I ended-up with this bound honestly
            for power in range(50):
                number_string = str(integer**power)
                if len(number_string) == power:
                    count += 1
                    numbers.append(int(number_string))
        numbers = sorted(numbers)
        return count, numbers


if __name__ == '__main__':
    problem = Problem63()
    problem.print_problem()