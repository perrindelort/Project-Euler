# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:03:27 2024

@author: Antoine
"""

import os
import math
import numpy as np

from util.util import timing, format_number
from scripts.problem import Problem

class Problem39(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'max_perimeter' not in kwargs.keys():
            raise ValueError("max_perimeter not specified")
        
        self.answer, self.time_taken = self.solve(max_perimeter = kwargs['max_perimeter'])
        
        self.detailed_answer = f"The number of solutions is maximized for p = {format_number(self.answer[0])} with {format_number(self.answer[1])} solutions"
            
        self.answer = self.answer[0]
        
    def generate_primitive_pythagorean_triples(self,max_perimeter):
        if max_perimeter >=12 :
            L = []
            for m in range(2,math.ceil(math.sqrt(1+max_perimeter*4)/2)):
                for n in range(1,m):
                    if math.gcd(n,m) == 1 and (n-m)%2 != 0:
                        a = m**2 - n**2
                        b = 2*m*n
                        c = m**2+n**2
                        L.append([a,b,c])
            pythagorean_triples = np.array(L)
            return pythagorean_triples
    
    @timing
    def solve(self, max_perimeter):
        pythagorean_triples_list = self.generate_primitive_pythagorean_triples(max_perimeter)
        L = [0]*((max_perimeter+1-12)//2+1)
        for perimeter in range(12,max_perimeter+1,2):
            for pythagorean_triple in pythagorean_triples_list:
                sum_pythagorean_triple = sum(pythagorean_triple)
                maxK = max_perimeter//sum_pythagorean_triple+1
                for k in range(1,maxK):
                    if sum_pythagorean_triple*k == perimeter :
                        L[(perimeter-12)//2] +=1
                        break
                    elif sum_pythagorean_triple*k >= perimeter:
                        break
        best_perimeter = 0
        most_triples = 0
        for i in range(len(L)):
            count_triples = L[i]
            if count_triples > most_triples:
                most_triples = count_triples
                best_perimeter = i*2+12
        return best_perimeter, most_triples


if __name__ == '__main__':
    problem = Problem39(max_perimeter = 1_000)
    problem.print_problem()