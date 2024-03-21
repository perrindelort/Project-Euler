# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 02:14:03 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class Problem5(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_limit' not in kwargs.keys():
            raise ValueError("upper_limit not specified")
        
        self.answer, self.time_taken = self.solve(upper_limit = kwargs['upper_limit'])

        
        self.detailed_answer = f"The smallest positive integer that is evenly divisible with no remainder by all the numbers from 1 to {format_number(kwargs['upper_limit'])} is {format_number(self.answer)}"
            
    
    def facteursPremiers(self,n):
        L=[]
        m=n
        while m!=1 or m!=m:
            for i in range(2,m+1):
                if m%i==0:
                    L.append(i)
                    m=m//i
                    break
        return L
    
    @timing
    def solve(self, upper_limit):
        L=[2]
        for i in range(3,upper_limit+1):
            L2 = self.facteursPremiers(i)
            for facteur in L2:
                if facteur in L:
                    if L2.count(facteur) > L.count(facteur):
                        while L2.count(facteur) != L.count(facteur):
                            L.append(facteur)
                else:
                    L.append(facteur)
        p = 1
        for facteur in L:
            p=p*facteur
        return p


if __name__ == '__main__':
    problem = Problem5(upper_limit = 20)
    problem.print_problem()