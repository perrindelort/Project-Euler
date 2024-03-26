# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:46:15 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

def new_triangle(triangle):
    new_triangle = triangle
    new_line = []
    last_line = new_triangle.pop()
    before_last_line = new_triangle.pop()
    try:
        last_line = last_line.split()
    except:
        pass
    try:
        before_last_line = before_last_line.split()
    except:
        pass
    for i in range(len(before_last_line)):
        l = []
        l.append(int(last_line[i]))
        l.append(int(last_line[i+1]))
        new_line.append(max(l)+int(before_last_line[i]))
    new_triangle.append(new_line)
    return new_triangle    

class Problem67(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        
        self.answer, self.time_taken = self.solve()
        
        self.detailed_answer = f"The maximum total from top to bottom of the given triangle is {format_number(self.answer)}"
            
                
    
    @timing
    def solve(self, **kwargs):
        lines = self.load_data_from_txt(split = False)
        lines_string = lines.strip().split('\n')
        triangle = []
        for line in lines_string:
            new_line_split = line.split(' ')
            new_line = [int(number) if number[0] != '0' else int(number[1]) for number in new_line_split]
            triangle.append(new_line)
        n_triangle = new_triangle(triangle)
        while len(n_triangle)!=1:
            n_triangle = new_triangle(n_triangle)
        return n_triangle[0][0]


if __name__ == '__main__':
    problem = Problem67()
    problem.print_problem()