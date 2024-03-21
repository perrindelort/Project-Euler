# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:11:10 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class Problem16(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'power_of_2' not in kwargs.keys():
            raise ValueError("power_of_2 not specified")
        
        self.answer, self.time_taken = self.resolution(power_of_2 = kwargs['power_of_2'])
        
        self.detailed_answer = f"The sum of the digits of 2^{kwargs['power_of_2']} is {format_number(self.answer)}"
            
    
    @timing
    def resolution(self, power_of_2):
        nombre = 2**power_of_2
        string = str(nombre)
        somme=0
        for chiffre in string:
            somme+=int(chiffre)
        return somme


if __name__ == '__main__':
    problem = Problem16(power_of_2 = 1_000)
    problem.print_problem()