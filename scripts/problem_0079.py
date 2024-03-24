# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:45:52 2024

@author: Antoine
"""

import os
import numpy as np 

from util.util import timing, format_number
from util.funct import load_data_from_txt
from scripts.problem import Problem

def get_max(liste):
    max_value = max(liste)
    max_indices = [index for index, value in enumerate(liste) if value == max_value]
    return max_value, max_indices


class Problem79(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        
        self.answer, self.time_taken = self.solve()
        
        self.detailed_answer = f"The shortest possible secret passcode of unknown length is {format_number(self.answer)}"
            
    
    @timing
    def solve(self, **kwargs):
        lines = load_data_from_txt(self.problem_number, split = False)
        lines_string = lines.strip().split('\n')
        order = np.zeros((10,10))
        for answer in lines_string:
            digit1 = int(answer[0])
            digit2 = int(answer[1])
            digit3 = int(answer[2])
            order[digit1][digit2] = 1
            order[digit1][digit3] = 1
            order[digit2][digit3] = 1 
        password = ""
        for integer in range(10):
            for col in range(10):
                if sum(order[col]) != 0:
                    if np.count_nonzero(order[col]) == 10-integer:
                        password += str(col)
        present = [False]*10
        for i in range(10):
            i_str = str(i)
            for answer in lines_string:
                for digit in answer:
                    if i_str == digit:
                        present[i] = True
        for index in range(10):
            if present[index]:
                if str(index) not in password:
                    password += str(index)
        return int(password)


if __name__ == '__main__':
    problem = Problem79()
    problem.print_problem()