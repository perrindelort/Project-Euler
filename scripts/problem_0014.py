# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:03:46 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class Problem14(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.resolution(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"The starting number under {format_number(kwargs['upper_bound'])} producing the longest chain is {format_number(self.answer[0])} with a {format_number(self.answer[1])}-long chain"
        
        # Because we returned 2 arguments
        self.answer = self.answer[0]
    
    def collatz_sequence(self,n,length):
        if n==1:
            return length
        if n%2==0:
            return self.collatz_sequence(n//2,length+1)
        else:
            return self.collatz_sequence(3*n+1,length+1)

    
    @timing
    def resolution(self, upper_bound):
        max_length = 0
        start = 0
        for i in range (1,upper_bound + 1):
            length = self.collatz_sequence(i,1)
            if length > max_length:
                max_length = length
                start = i
        return (start,max_length)


if __name__ == '__main__':
    problem = Problem14(upper_bound = 1_000_000)
    problem.print_problem()