# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:11:32 2024

@author: Antoine
"""

import os
from primePy import primes

from util.util import timing, format_number
from scripts.problem import Problem

def verify_compatibility(compatibility,prime1,prime2):
    if prime1 != prime2:
        if prime1 in compatibility[prime2]:
            return True
    return False


class Problem60(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        self.answer, self.time_taken = self.solve()
        
        self.detailed_answer = f"The set of five primes for which any two primes concatenate to produce another prime is {self.answer[1]} and their sums is {format_number(self.answer[0])}"
         
        # We returned 2 values for the detailed answer
        self.answer = self.answer[0]
    
    @timing
    def solve(self, **kwargs):
        # Ugly solution
        primes_list = primes.upto(10_000)
        primes_list_string = [str(prime) for prime in primes_list]
        compatibility = {}
        for prime in primes_list_string:
            compatibility[prime] = []
        for prime1 in primes_list_string:
            for prime2 in primes_list_string:
                if prime1 != prime2:
                    if primes.check(int(prime1+prime2)) and primes.check(int(prime2+prime1)):
                        compatibility[prime1].append(prime2)
                        compatibility[prime2].append(prime1)
        candidates = []
        for key in compatibility.keys():
            for prime2 in compatibility[key]:
                for prime3 in compatibility[key]:
                    if verify_compatibility(compatibility,prime2,prime3):
                        for prime4 in compatibility[key]:
                            if verify_compatibility(compatibility,prime4,prime3) and verify_compatibility(compatibility,prime4,prime2):
                                for prime5 in compatibility[key]:
                                        if verify_compatibility(compatibility,prime5,prime4) and verify_compatibility(compatibility,prime5,prime3) and verify_compatibility(compatibility,prime5,prime2):
                                            candidates.append([int(key),int(prime2),int(prime3),int(prime4),int(prime5)])
        
        candidates.sort(key = lambda s:sum(s))
        return sum(candidates[0]), candidates[0]


if __name__ == '__main__':
    problem = Problem60()
    problem.print_problem()