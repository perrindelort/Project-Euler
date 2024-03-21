# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:01:54 2024

@author: Antoine
"""
import runpy
import warnings

from util.arg_parser import ProjectEulerArgumentParser

if __name__ == "__main__":
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    
    parser = ProjectEulerArgumentParser()
    args = parser.parse_args()

    # Get the module name from the command line argument
    problem_number_str = str(args.problem_number).zfill(4)
    script_name = f"scripts.problem_{problem_number_str}"

    # Get the module object using __import__
    script = __import__(script_name)

    # Run the __main__ function of the module using runpy
    runpy.run_module(script_name, run_name="__main__", alter_sys=True)