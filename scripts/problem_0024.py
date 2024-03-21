# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 23:36:23 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from util.funct import factorial
from scripts.problem import Problem

class Problem24(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'target' not in kwargs.keys():
            raise ValueError("target not specified")
        if 'string' not in kwargs.keys():
            raise ValueError("string not specified")
        
        self.answer, self.time_taken = self.solve(string = kwargs['string'], 
                                                  target = kwargs['target'])
        
        self.detailed_answer = f"The {format_number(kwargs['target'])}th permutation of the string {kwargs['string']} is {self.answer}"
    
    def permutation_position(self,number,string):
        n = len(string)
        if(n>0):
            return number//factorial(n-1)
        else:
            return number        
    
    @timing
    def solve(self, string, target):
        string_copy = "".join([s for s in string])
        n = len(string_copy)
        L = [0]*n
        for i in range(n-1):
            L[i] = int(string_copy[self.permutation_position(target - 1,string_copy)])
            f = max(len(string_copy)-1,0)
            target = target % factorial(f)
            string_copy = string_copy.replace(str(L[i]),'')
        L[n-1] = int(string_copy[0])
        string_copy = "".join([s for s in string])
        solution =""
        for idx in L:
            solution += string_copy[idx]
        return solution


if __name__ == '__main__':
    problem = Problem24(string = "0123456789",
                        target = 1_000_000)
    problem.print_problem()