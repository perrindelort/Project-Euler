# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:19:22 2024

@author: Antoine
"""

import argparse


class ProjectEulerArgumentParser(argparse.ArgumentParser):
    def __init__(
        self,
        description="Parse arguments to launch any Project's Euler solution from main",
    ):
        super().__init__(description=description)
        self.add_argument(
            "-n",
            "--problem_number",
            type=int,
            dest="problem_number",
            default="1",
            help="Which Project Euler problem would you like to run?",
        )

        self.add_argument(
            "-t",
            "--test_all",
            dest="test_all",
            action="store_true",
            help="Would you like to verify that all problems give the correct answer ?",
        )

        self.add_argument(
            "-c",
            "--color_checker",
            dest="color_checker",
            type=str,
            nargs="?",
            const="all",
            help="Check how the colors from the colored library render on the cmd",
        )
