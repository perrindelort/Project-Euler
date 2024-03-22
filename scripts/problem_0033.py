# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:26:51 2024

@author: Antoine
"""

import os
import numpy as np
from fractions import Fraction

from util.util import timing, format_number
from scripts.problem import Problem

class Problem33(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        
        self.answer, self.time_taken = self.solve()
        
        self.detailed_answer = f"The value of the denominator of the product of the four mentionned fractions given in its lowest common terms is {format_number(self.answer)}"
            
    
    @timing
    def solve(self, **kwargs):
        numerator_list = []
        denominator_list = []
        for denominator in range(10,100):
            for numerator in range(10,denominator):
                if (numerator%10==0 and denominator%10==0):
                    continue
                numerator_string = str(numerator)
                denominator_string = str(denominator)
                for digit1 in range(len(numerator_string)):
                    for digit2 in range(len(denominator_string)):
                        if numerator_string[digit1] == denominator_string[digit2]:
                            if len(numerator_string) == 1 and len(denominator_string) == 1 :
                                pass
                            new_numerator = int(numerator_string[digit1-1])
                            new_denominator = int(denominator_string[digit2-1])
                            if new_denominator !=0:
                                value = new_numerator/new_denominator
                                if  value < 1: 
                                    if value == numerator/denominator:
                                        numerator_list.append(numerator)
                                        denominator_list.append(denominator)
        final_numerator = np.prod(numerator_list)
        final_denominator = np.prod(denominator_list)
        return Fraction(final_numerator,final_denominator).denominator


if __name__ == '__main__':
    problem = Problem33()
    problem.print_problem()