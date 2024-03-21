# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:21:06 2024

@author: Antoine
"""

import os
import numpy as np

from util.util import timing, format_number
from scripts.problem import Problem

class Problem12(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'threshold' not in kwargs.keys():
            raise ValueError("threshold not specified")
        
        self.answer, self.time_taken = self.resolution(threshold = kwargs['threshold'])
        
        self.detailed_answer = f"The first triangle number to have over {format_number(kwargs['threshold'])} divisors is {format_number(self.answer)}"
            
    
    def compterDiviseurs(self, n):
        produit = 1 
        for facteur in self.facteursPremiers(n).values():
            produit = produit*(facteur+1)
        return produit

    def facteursPremiers(self, n):
        L={}
        m=n
        while m!=1 or m!=m:
            for i in range(2,m+1):
                if m%i==0:
                    try:
                        L.update({i  : L.get(i)+1})
                    except:
                        L[i] = 1
                    m=m//i
                    break
        return L
    
    @timing
    def resolution(self, threshold):
        i=1
        s=1
        n=0
        while (n < threshold):
            n = self.compterDiviseurs(s)
            if n >= threshold:
                return s
            i+=1
            s+=i


if __name__ == '__main__':
    problem = Problem12(threshold = 500)
    problem.print_problem()