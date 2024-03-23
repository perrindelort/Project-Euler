# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 12:37:15 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

def is_solution(number):
    number_string = str(number)
    number_string6 = str(number*6)
    if len(number_string) != len(number_string6):
        return False
    else:
        set_number = set(number_string)
        multiplier = 2
        while multiplier < 7:
            if set_number != set(str(number*multiplier)):
                return False
            multiplier +=1
        return True


class Problem52(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        self.answer, self.time_taken = self.solve()
        
        self.detailed_answer = f"The smallest integer x satisfying the problem is {format_number(self.answer)} as " + " ".join([f"{idx}x = {format_number(idx * self.answer)}" for idx in range(2, 7)])
            
    
    @timing
    def solve(self, **kwargs):
        for number in range(1,100000000):
            if is_solution(number):
                return number


if __name__ == '__main__':
    problem = Problem52()
    problem.print_problem()