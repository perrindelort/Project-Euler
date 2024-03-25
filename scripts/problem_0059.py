# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:58:00 2024

@author: Antoine
"""

import os
from collections import Counter

from util.util import timing, format_number, load_data_from_txt
from scripts.problem import Problem

def is_english(ascii1,ascii2):
    val = ascii1 ^ ascii2
    if 32 <= val <= 93:
        return True
    elif 97 <= val <= 122:
        return True
    else:
        return False
    
def xor_decrypt(crypted_string,key):
    string = ""
    ord_key = [ord(letter) for letter in key]
    for index,crypted_letter in enumerate(crypted_string):
        key_index = index%3
        string += chr(crypted_letter ^ ord_key[key_index])
    return string

def decrypt(ciphertext, key):
	return [(c ^ key[i % len(key)]) for (i, c) in enumerate(ciphertext)]

class Problem59(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        
        self.answer, self.time_taken = self.solve()
        
        self.detailed_answer = f"The sum of the ASCII values in the given text is {format_number(self.answer[0])}\nThe decryption key was {self.answer[1]}\nThe orignal text was : {self.answer[2]}"
          
        # We returned 3 values for the detailed_answer
        self.answer = self.answer[0]
    
    @timing
    def solve(self, **kwargs):
        lines = load_data_from_txt(self.problem_number,split = False)
        lines_string = lines.strip().split(',')
        cipher = [int(letter_string) for letter_string in lines_string]
            
        alphabet = "abcdefghijklmnopqrstuvwxyz"


        lines_0 = cipher[0::3]
        lines_1 = cipher[1::3]
        lines_2 = cipher[2::3]

        lines = [lines_0,lines_1,lines_2]

        
        key = ""
        for line in lines:
            for letter in alphabet:
                ascii_letter = ord(letter)
                is_cipher = True
                for crypted_letter in line:
                    if not is_english(crypted_letter,ascii_letter):
                        is_cipher = False
                        break
                if is_cipher:
                    key += letter
        
        decrypted_string = xor_decrypt(cipher,key)
        
        sum_ascii = sum([ord(letter) for letter in decrypted_string])
        return sum_ascii, key, decrypted_string

if __name__ == '__main__':
    problem = Problem59()
    problem.print_problem()