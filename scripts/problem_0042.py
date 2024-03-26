# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:27:39 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class Problem42(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        self.answer, self.time_taken = self.solve()
        
        self.detailed_answer = f"There are {format_number(self.answer)} triangle words in the given text file"
            
    
    @timing
    def solve(self, **kwargs):
        lines = self.load_data_from_txt()
        score_lines = []
        for line in lines:
            score = 0
            for letter in line:
                if letter != '"':
                    score += ord(letter)%64
            score_lines.append(score)
        score_lines.sort()
        triangle_numbers = [1]
        supremum = score_lines[-1]
        while triangle_numbers[-1] < supremum :
            triangle_numbers.append(triangle_numbers[-1]+len(triangle_numbers)+1)
        count_triangle_numbers = 0
        for score in score_lines:
            if score in triangle_numbers:
                count_triangle_numbers += 1
        return count_triangle_numbers


if __name__ == '__main__':
    problem = Problem42()
    problem.print_problem()