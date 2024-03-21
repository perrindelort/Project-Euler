# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:29:41 2024

@author: Antoine
"""

from util.statements import get_statement
from util.titles import get_title
from util.util import get_problem_number_from_filename, format_statement_answer, timing

class Problem():
    def __init__(self, path):
        self.problem_number = get_problem_number_from_filename(path)
        self.title = get_title(self.problem_number)
        self.statement = get_statement(self.problem_number)
        
        
       
    @timing    
    def resolution(self, **kwargs):
        pass
    
    def print_problem(self):
        format_statement_answer(problem_number = self.problem_number,
                                title = self.title,
                                statement = self.statement,
                                time_taken = self.time_taken,
                                short_answer = self.answer,
                                detailed_answer = self.detailed_answer)