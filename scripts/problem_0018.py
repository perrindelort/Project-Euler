# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:19:44 2024

@author: Antoine
"""

import os

from util.util import timing, format_number
from scripts.problem import Problem

class Problem18(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'triangle_string' not in kwargs.keys():
            raise ValueError("triangle_string not specified")
        
        self.answer, self.time_taken = self.resolution(triangle_string = kwargs['triangle_string'])
        
        self.detailed_answer = f"The maximum total from top to bottom of the given triangle is {format_number(self.answer)}"
            
    def new_triangle(self,triangle):
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
        # print("nouveau triangle est de taille : ",len(nouveau_triangle))
        # for ligne in nouveau_triangle:
            # print(ligne)
        return new_triangle    
                
    
    @timing
    def resolution(self, triangle_string):
        new_triangle = self.new_triangle(triangle_string)
        while len(new_triangle)!=1:
            new_triangle = self.new_triangle(new_triangle)
        return new_triangle[0][0]


if __name__ == '__main__':
    problem = Problem18(triangle_string = """75
                                             95 64
                                             17 47 82
                                             18 35 87 10
                                             20 04 82 47 65
                                             19 01 23 75 03 34
                                             88 02 77 73 07 63 67
                                             99 65 04 28 06 16 70 92
                                             41 41 26 56 83 40 80 70 33
                                             41 48 72 33 47 32 37 16 94 29
                                             53 71 44 65 25 43 91 52 97 51 14
                                             70 11 33 28 77 73 17 78 39 68 17 57
                                             91 71 52 38 17 14 91 43 58 50 27 29 48
                                             63 66 04 68 89 53 67 30 73 16 69 87 40 31
                                             04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split("\n"))
    problem.print_problem()