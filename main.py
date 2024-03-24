# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:01:54 2024

@author: Antoine
"""
import runpy
import warnings

from util.arg_parser import ProjectEulerArgumentParser
from util.color_checker import display_colors

if __name__ == "__main__":
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    
    parser = ProjectEulerArgumentParser()
    args = parser.parse_args()
    print(args)

    if args.test_all == True:
        from scripts.test_answers import test_all
        test_all()
        
    if args.color_checker:
        display_colors(args.color_checker)
        
    else:
        problem_number_str = str(args.problem_number).zfill(4)
        script_name = f"scripts.problem_{problem_number_str}"
    
        script = __import__(script_name)
    
        runpy.run_module(script_name, run_name="__main__", alter_sys=True)