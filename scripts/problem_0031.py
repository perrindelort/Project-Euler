# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 02:12:15 2024

@author: Antoine
"""

import os
from util.util import timing, format_number
from scripts.problem import Problem

class Problem31(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'target' not in kwargs.keys():
            raise ValueError("target not specified")
            
        if 'coins' not in kwargs.keys():
            raise ValueError("coins not specified")
        
        self.answer, self.time_taken = self.solve(coins = kwargs['coins'], 
                                                  target = kwargs['target'])
        
        self.detailed_answer = f"There are {format_number(self.answer)} ways to make {format_number(kwargs['target'])}p using {'p, '.join([str(coin) for coin in kwargs['coins'][:-1]])}p and {str(kwargs['coins'][-1])}p"
            
    
    @timing
    def solve(self, coins, target):
        number_of_ways = [0] * (target+1)
        # Initialization
        number_of_ways[0] = 1
        # Then number_of_ways[1] : how to do 1p with all the coins
        # number_of_ways[2] : how to do 2p with all the coins...
        for coin in coins:
            for way in range(coin, target + 1):
                number_of_ways[way] += number_of_ways[way - coin]
        return number_of_ways[200]
            
if __name__ == '__main__':
    problem = Problem31(coins = [1,2,5,10,20,50,100,200], 
                        target = 200)
    problem.print_problem()