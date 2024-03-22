# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:31:48 2024

@author: Antoine
"""

import os
from itertools import permutations

from util.util import timing, format_number
from scripts.problem import Problem

class Problem43(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        
        self.answer, self.time_taken = self.solve()
        
        self.detailed_answer = f"The sum of all 0 to 9 pandigital numbers with this property is {format_number(self.answer)}"
            
    
    @timing
    def solve(self, **kwargs):
        pan_digital_string = "9876543210"
        permutation_list = list(permutations(pan_digital_string))
        sub_string_divisibility_list = []
        for index in range(len(permutation_list)):
            integer_string = ''.join(permutation_list[index])
            if (int(integer_string[3])%2 == 0):
                s = 0
                for i in range(2,5):
                    s += int(integer_string[i])
                if s%3 == 0:
                    if (integer_string[5]=="0" or integer_string[5]=="5"):
                        if int(integer_string[4:7])%7 == 0:
                            if int(integer_string[5:8])%11 == 0:
                                if int(integer_string[6:9])%13 == 0:
                                    if int(integer_string[7:10])%17 == 0:
                                        if integer_string[0] != "0":
                                            sub_string_divisibility_list.append(int(integer_string))
        return sum(sub_string_divisibility_list)


if __name__ == '__main__':
    problem = Problem43()
    problem.print_problem()