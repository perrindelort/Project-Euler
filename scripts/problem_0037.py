# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:59:30 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from util.funct import isprime
from scripts.problem import Problem

class Problem37(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        
        self.answer, self.time_taken = self.solve()
        
        self.detailed_answer = f"The sum of the only 11 primes that are both truncatable from left to right and right to left are {format_number(self.answer)}"
      
    
    
    @timing
    def solve(self, **kwargs):
        truncatable_primes_list = [] 
        integer = 21
        while len(truncatable_primes_list) < 11:
            if isprime(integer):
                integer_string = str(integer)
                for i in range(1, len(integer_string)):
                    if (not isprime(int(integer_string[i:]))) or (not isprime(int(integer_string[:-i]))): 
                        break
                else: 
                    truncatable_primes_list.append(integer)
            integer += 2
        print(truncatable_primes_list)
        return sum(truncatable_primes_list)


if __name__ == '__main__':
    problem = Problem37()
    problem.print_problem()