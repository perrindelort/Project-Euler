# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:36:19 2024

@author: Antoine
"""

import os
from collections import Counter
from util.util import timing, format_number
from scripts.problem import Problem
    
def attribute_value(symbol:str) -> int:
    if symbol == "A":
        return 14
    elif symbol == "K":
        return 13
    elif symbol == "Q":
        return 12
    elif symbol == "J":
        return 11
    elif symbol == "T":
        return 10
    else:
        return int(symbol)

def evaluate_hand(player_hand: list[str]) -> int:
    symbols = [attribute_value(card[0]) for card in player_hand]
    symbols.sort(reverse = True)
    colors = [card[1] for card in player_hand]
    
    symbols = Counter(symbols)
    symbols_count = sorted(symbols.values())
    symbols_count.sort(reverse = True)
    sorted_keys = sorted(symbols, key=symbols.get, reverse = True)
    
    
    # Where color matters
    # Straight Flush
    # Flush
    if len(set(colors)) == 1:
        for idx in range(len(sorted_keys) - 1):
            if idx == 0 and sorted_keys[idx] == 14:
                if sorted_keys[idx + 1] == 13 or sorted_keys[idx + 1] == 5:
                    continue # Straight with an Ace
            if sorted_keys[idx] == sorted_keys[idx + 1] + 1:
                continue # Straight
            
            # Flush
            else:
                return 5*10**11 + symbols[0]*10**8 
            
        # Straight Flush
        return 8*10**11 + symbols[0]*10**8 
    
    # Where color doesn't matter
    # Four of a kind
    # Full house
    # Straight
    # Three of a kind
    # Two pairs
    # One pair
    # High card
    else:
        
        # Four of a kind
        if symbols_count[0] == 4:
            score = 7*10**11
            for idx,key in enumerate(sorted_keys):
                score += key*10**(8-2*idx)
            return  score
        
        # Full house
        # Three of a kind
        elif symbols_count[0] == 3:
            
            # Full House
            if symbols_count[1] == 2:
                score = 6*10**11
                for idx,key in enumerate(sorted_keys):
                    score += key*10**(8-2*idx)
                return score
            
            # Three of a kind
            else:
                score = 3*10**11
                for idx,key in enumerate(sorted_keys):
                    score += key*10**(8-2*idx)
                return score
            
        # Two pairs
        # One pair
        elif symbols_count[0] == 2:
            
            # Two pairs
            if symbols_count[1] == 2:
                score = 2*10**11
                for idx,key in enumerate(sorted_keys):
                    score += key*10**(8-2*idx)
                return score
            
            # One pair
            else:
                score = 10**11
                for idx1,key in enumerate(sorted_keys):
                    score += key*10**(8-2*idx1)
                return score
            
        else:
            for idx in range(len(sorted_keys) - 1):
                if idx == 0 and sorted_keys[idx] == 14:
                    if sorted_keys[idx + 1] == 13 or sorted_keys[idx + 1] == 5:
                        continue # Straight with an Ace
                elif sorted_keys[idx] == sorted_keys[idx + 1] + 1:
                    continue # Straight
                
                # High card
                else:
                    score = 0
                    for idx,key in enumerate(sorted_keys):
                        score += key*10**(8-2*idx)
                    return score
                
            # Straight
            score = 4*10**11
            for idx,key in enumerate(sorted_keys):
                score += key*10**(8-2*idx)
            return score

class Problem54(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        self.answer, self.time_taken = self.solve()
        
        self.detailed_answer = f"In the thousand hands of poker contained in the given file, Players 1 has won {format_number(self.answer)} of them\nHe might need some training :-)"
            
    
    @timing
    def solve(self, **kwargs):
        lines = self.load_data_from_txt(sep = '\n')
        player1_wins = 0
        for line in lines:
            cards = line.split(' ')
            player_1_hand= cards[0:5]
            player_2_hand = cards[5:]
            #print(line)
            #print(player_1_hand)
            #print(player_2_hand)
            if evaluate_hand(player_1_hand) > evaluate_hand(player_2_hand):
                player1_wins += 1
        return player1_wins
            


if __name__ == '__main__':
    problem = Problem54()
    problem.print_problem()