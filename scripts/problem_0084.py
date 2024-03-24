# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:26:34 2024

@author: Antoine
"""

import os
import queue
import random

from util.util import timing, format_number
from scripts.problem import Problem

def generate_community_chest():
    community_chest = queue.Queue()
    cards = ['GO','JAIL','None','None','None','None','None','None','None','None','None','None','None','None','None','None']
    random.shuffle(cards)
    for card in cards:
        community_chest.put(card)
    return community_chest

def use_community_chest(card,position):
    if card == 'None':
        return position
    elif card == 'GO':
        return 0
    elif card == 'JAIL':
        return 10

def generate_chances():
    chances = queue.Queue()
    cards = ['GO','JAIL','C1','E3','H2','R1','nextR','nextR','nextU','back3S','None','None','None','None','None','None']
    random.shuffle(cards)
    for card in cards:
        chances.put(card)
    return chances

def use_chances(card,position):
    if card == 'None':
        return position
    elif card == 'GO':
        return 0
    elif card == 'JAIL':
        return 10
    elif card == 'C1':
        return 11
    elif card == 'E3':
        return 24
    elif card == 'H2':
        return 39
    elif card == 'R1':
        return 5
    elif card == 'nextR':
        return next_r(position)
    elif card == 'nextU':
        return next_u(position)
    elif card == 'back3S':
        return (position-3)%40
        
            
def next_r(position):
    if position >= 35 or (0 <= position < 5):
        return 5
    elif 5 <= position < 15 :
        return 15
    elif 15 <= position < 25:
        return 25
    else:
        return 35

def next_u(position):
    if position >= 28 or (0 <= position < 12):
        return 12
    else: 
        return 28
    
class Problem84(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
            
        if 'upper_bound_a' not in kwargs.keys():
            raise ValueError("upper_bound_a not specified")
        
        if 'upper_bound_b' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'],
                                                  upper_bound_a = kwargs['upper_bound_a'],
                                                  upper_bound_b = kwargs['upper_bound_b'])
        
        if kwargs['upper_bound_a'] == kwargs['upper_bound_b']:
            self.detailed_answer = f"By using 2 {format_number(kwargs['upper_bound_a'])}-sided dice the 3 most popular squares are {' '.join([key for key in self.answer[1].keys()])} with corresponding probabilities {' '.join([str(val) for val in self.answer[1].values()])} thus forming the 6-digit modal string {self.answer[0]}"
        else:
            self.detailed_answer = f"By using 1 {format_number(kwargs['upper_bound_a'])}-sided die and 1 {format_number(kwargs['upper_bound_b'])}-sided die the 3 most popular squares are {' '.join([key for key in self.answer[1].keys()])} with corresponding probabilities {' '.join([str(val) for val in self.answer[1].values()])} thus forming the 6-digit modal string {self.answer[0]}"
        
        # We returned 4 values for the detailed_answer
        self.answer = self.answer[0]
    
    @timing
    def solve(self, upper_bound, upper_bound_a, upper_bound_b):
        chances = generate_chances()
        community_chest = generate_community_chest()
        CC = [2,17,33]
        CH = [7,22,36]
        board = {'GO' : 0, 'A1' : 1, 'CC' : 2, 'A2' : 3,'T1' : 4,'R1' : 5,'B1' : 6, 'CH1' : 7, 'B2' : 8, 'B3': 9, 'JAIL': 10,
                 'C1': 11, 'U1' : 12, 'C2' : 13, 'C3' : 14, 'R2' : 15, 'D1' : 16, 'CC2' : 17, 'D2' : 18, 'D3' : 19, 'FP' :20,
                 'E1' : 21, 'CH2' : 22, 'E2' : 23, 'E3' : 24, 'R3' : 25, 'F1' : 26, 'F2' : 27, 'U2': 28, 'F3' : 29, 'G2J' : 30,
                 'G1' : 31, 'G2' : 32, 'CC3' : 33, 'G3' : 34, 'R4' : 35, 'CH3' : 36, 'H1' : 37, 'T2' : 38, 'H2' : 39}
        doubles = 0
        position = 0
        occurences = [0]*40
        for iteration in range(upper_bound):
            d1 = random.randint(1,upper_bound_a)
            d2 = random.randint(1,upper_bound_b)
            if d1 == d2:
                doubles += 1
            else: 
                doubles = 0
            if doubles == 3:
                position = 10
            else:
                position = (position + d1 + d2) % 40
                if position in CC:
                    card = community_chest.get()
                    community_chest.put(card)
                    position = use_community_chest(card,position)            
                elif position in CH:
                    card = chances.get()
                    chances.put(card)
                    position = use_chances(card,position)
                elif position == 30:
                    position = 10
            occurences[position] += 1
            
                    
            
        tot = sum(occurences)
        string = ""
        max_values = []
        details = {}
        inv_board = {v: k for k, v in board.items()}

        for _ in range(3):
            max_value = max(occurences)
            max_index = occurences.index(max_value)
            string += str(max_index).zfill(2)
            max_values.append(max_value)
            occurences[max_index] = 0  
            details[inv_board[max_index]] = max_value  / tot        
        
        return string, details



if __name__ == '__main__':
    problem = Problem84(upper_bound = 1_000_000,
                        upper_bound_a = 4,
                        upper_bound_b = 4)
    problem.print_problem()