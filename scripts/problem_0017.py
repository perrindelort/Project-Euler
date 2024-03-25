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
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"To write the numbers 1 to {format_number(kwargs['upper_bound'])} you need {format_number(self.answer)} letters !"
            
    
    @timing
    def solve(self, upper_bound):
        count = 0
        units  = {0 : 0,
                 1 : 3, # 'one'
                 2 : 3, # 'two'
                 3 : 5, # 'three'
                 4 : 4, # 'four'
                 5 : 4, # 'five'
                 6 : 3, # 'six'
                 7 : 5, # 'seven'
                 8 : 5, # 'eight'
                 9 : 4, # 'nine'
                 10 : 3, # 'ten'
                 11 : 6, # 'eleven'
                 12 : 6, # 'twelve'
                 13 : 8, # 'thirteen'
                 14 : 8, # 'fourteen'
                 15 : 7, # 'fifteen'
                 16 : 7, # 'sixteen'
                 17 : 9, # 'seventeen'
                 18 : 8, # 'eighteen'
                 19 : 8, # 'nineteen'
                 }
        tens = {0 : 0,
                1 : 3, # 'ten'
                2 : 6, # 'twenty'
                3 : 6, # 'thirty'
                4 : 5, # 'fourty'
                5 : 5, # 'fifty'
                6 : 5, # 'sixty'
                7 : 7, # 'seventy'
                8 : 6, # 'eighty'
                9 : 6 # 'ninety'
                }
        
        def count_letter(integer):
            
            number_of_letters = 0
            u = integer % 10
            t = ((integer//10) % 10) 
            h = (integer//100) % 10
            
            if t <= 1:
                # Adding units
                number_of_letters += units[u+t*10]
            else:
                # Adding tens
                number_of_letters += tens[t]
                number_of_letters += units[u]
                
                
            # Adding hundreds
            if h != 0:
                number_of_letters += units[h] + 7 # hundred
            
            if h != 0 and (t != 0 or u != 0):
                number_of_letters += 3 # and 
                
            return number_of_letters
        
        for integer in range(1, upper_bound):
            count += count_letter(integer)
        
        # Adding 'one thousand'
        count += 11 
        return count


if __name__ == '__main__':
    problem = Problem17(upper_bound = 1_000)
    problem.print_problem()