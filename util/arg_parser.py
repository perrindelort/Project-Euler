# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:19:22 2024

@author: Antoine
"""

import argparse

class ProjectEulerArgumentParser(argparse.ArgumentParser):
    def __init__(self,description = "coucou!"):
        super().__init__(description = description)
        self.add_argument("-n","--problem_number",type=int, 
                          dest = "problem_number",
                          default = "1",
                          help="Which Project Euler problem would you like to run?")

class Problem3ArgumentParser(ProjectEulerArgumentParser):
    def __init__(self):
        super().__init__(description="Argument Parser of the 3rd problem from Project Euler https://projecteuler.net/")
        self.add_argument("-f","--number_to_factor",type=int, 
                          dest = "number_to_factor",
                          default = 600851475143,
                          help="Input the number you wish to know the biggest prime factor")

class Problem8ArgumentParser(ProjectEulerArgumentParser):
    def __init__(self):
        super().__init__(description="Argument Parser of the 8th problem from Project Euler https://projecteuler.net/")
        self.add_argument("-s","--large_number_string",type=str, 
                          dest = "large_number_string",
                          default = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450",
                          help="Input the number in string format from which you'd like to have the n-th adjacents")
        
        self.add_argument("-d","--number_of_adjacents_digits",type=int, 
                          dest = "number_of_adjacents_digits",
                          default = 13,
                          help="Input the number of adjacents digits to have the biggest product")