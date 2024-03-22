# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:19:22 2024

@author: Antoine
"""

import os
from itertools import permutations

from util.util import timing, format_number
from util.funct import isprime
from scripts.problem import Problem

class Problem41(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        
        self.answer, self.time_taken = self.solve()
        
        self.detailed_answer = f"The largest n-digits pandigital prime that exists is {format_number(self.answer)}"
            
    
    @timing
    def solve(self, **kwargs):
        """
        Else n(n+1)/2 can be divided by 3 for n = 8 and n = 9
        so 1234567 < integer < 7654312
        """
        supremum_string = "7654321"
        permutation_list = list(permutations(supremum_string))
        for index in range(len(permutation_list)):
            integer = int(''.join(permutation_list[index]))
            if isprime(integer):
                return integer


if __name__ == '__main__':
    problem = Problem41()
    problem.print_problem()