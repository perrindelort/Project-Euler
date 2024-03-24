# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:23:40 2024

@author: Antoine
"""

import os
import numba as nb

from util.util import timing, format_number
from scripts.problem import Problem

@nb.njit('List(int64)(int64)')
def get_prime_divisors(n):
    divisors = []
    while n % 2 == 0:
        divisors.append(2)
        n //= 2
    while n % 3 == 0:
        divisors.append(3)
        n //= 3
    i = 5
    while i*i <= n:
        for k in (i, i+2):
            while n % k == 0:
                divisors.append(k)
                n //= k
        i += 6
    if n > 1:
        divisors.append(n)
    return divisors

@nb.njit('List(int64)(int64)')
def get_divisors(n):
    divisors = []
    if n == 1:
        divisors.append(1)
    elif n > 1:
        prime_factors = get_prime_divisors(n)
        divisors = [1]
        last_prime = 0
        factor = 0
        slice_len = 0
        # Find all the products that are divisors of n
        for prime in prime_factors:
            if last_prime != prime:
                slice_len = len(divisors)
                factor = prime
            else:
                factor *= prime
            for i in range(slice_len):
                divisors.append(divisors[i] * factor)
            last_prime = prime
        divisors.sort()
    divisors.remove(n)
    return divisors


def get_chain(integer,supremum):
    is_amicable = False
    new_member = integer
    amicable_chain = []
    while new_member < supremum and not is_amicable:
        new_member = sum(get_divisors(new_member))
        if new_member == integer:
            is_amicable = True
        elif new_member < integer :
            break
        elif new_member in amicable_chain:
            break
        else:
            amicable_chain.append(new_member)
    return is_amicable, amicable_chain

class Problem95(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        if 'upper_bound' not in kwargs.keys():
            raise ValueError("upper_bound not specified")
        
        self.answer, self.time_taken = self.solve(upper_bound = kwargs['upper_bound'])
        
        self.detailed_answer = f"The smallest member of the longest amicable chain with no element exceeding {format_number(kwargs['upper_bound'])} is {format_number(self.answer[0])}.\nThe longest chains is made of {format_number(len(self.answer[1]))} which are {' → '.join([str(number) for number in self.answer[1]])}"
        # We returned 2 values for the detailed_answer
        self.answer = self.answer[0]
    
    @timing
    def solve(self, upper_bound):
        max_chain = []
        amicable_numbers = set([])
        for current_number in range(220,upper_bound):
            if current_number not in amicable_numbers:
                is_amicable, amicable_chain = get_chain(current_number,upper_bound)
            if is_amicable:
                for amicable_number in amicable_chain:
                    amicable_numbers.add(amicable_number)
                if len(amicable_chain) > len(max_chain):
                    max_chain = amicable_chain
                    max_chain.append(current_number)
        return min(max_chain), max_chain


if __name__ == '__main__':
    problem = Problem95(upper_bound = 1_000_000)
    problem.print_problem()