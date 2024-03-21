# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:13:59 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class Problem17(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'arg' not in kwargs.keys():
            raise ValueError("arg not specified")
        
        self.answer, self.time_taken = self.resolution(arg = kwargs['arg'])
        
        self.detailed_answer = f"Problem not yet implemented !"
            
    
    @timing
    def resolution(self, **kwargs):
        return None, None


if __name__ == '__main__':
    problem = Problem17(arg = None)
    problem.print_problem()