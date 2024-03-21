# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 00:07:48 2024

@author: Antoine
"""
import os
import re
from time import perf_counter_ns

import functools
import textwrap

def format_number(number):
    return format(number,',')

def timing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        beginning = perf_counter_ns()
        answer = func(*args, **kwargs)
        end = perf_counter_ns()
        return answer, (end - beginning)*(10**-9)
    return wrapper
    

def get_problem_number_from_filename(path):
    # Get filename
    file_name = os.path.basename(path)
        
    # Use of regexto extract problem number
    regex = r"_(\d+)\."
    # Rechercher le nombre dans le nom de fichier
    match = re.search(regex, file_name)
    return int(match.group(1))


def format_statement_answer(problem_number, title, statement, time_taken, short_answer, detailed_answer, n_dashes=50):
    os.system('cls')

    max_len = 2*n_dashes + 10 + problem_number//10 + 1
    statement_indent = 'Statement : '
    detailed_answer_indent = "Detailed answer : "
    first_sentence_statement = textwrap.fill(statement.split('\n')[0],
                                   width = max_len,
                                   initial_indent='',
                                   subsequent_indent=' '*len(statement_indent),
                                   break_long_words=False,
                                   replace_whitespace=False
                                   ) 
    text_statement = first_sentence_statement + "\n" + "\n".join(textwrap.fill(l,
                                   width = max_len,
                                   initial_indent=' '*len(statement_indent),
                                   subsequent_indent=' '*len(statement_indent),
                                   break_long_words=False,
                                   replace_whitespace=False
                                   ) for l in statement.split('\n')[1:]
                     )
    
    first_sentence_detailed_answer = textwrap.fill(detailed_answer.split('\n')[0],
                                   width = max_len,
                                   initial_indent='',
                                   subsequent_indent=' '*len(detailed_answer_indent),
                                   break_long_words=False,
                                   replace_whitespace=False
                                   ) 
    text_detailed_answer = first_sentence_detailed_answer + "\n" + "\n".join(textwrap.fill(l,
                                   width = max_len,
                                   initial_indent=' '*len(detailed_answer_indent),
                                   subsequent_indent=' '*len(detailed_answer_indent),
                                   break_long_words=False,
                                   replace_whitespace=False
                                   ) for l in detailed_answer.split('\n')[1:]
                     )
    
# =============================================================================
#     statement_wrapped = textwrap.fill(statement,
#                                       width=max_len,
#                                       initial_indent="Statement : ",
#                                       subsequent_indent=" " * 12,
#                                       break_long_words=False,
#                                       replace_whitespace=False)
#     
#     detailed_answer_wrapped = textwrap.fill(detailed_answer,
#                                             width=max_len, 
#                                             initial_indent="Detailed answer : ",
#                                             subsequent_indent=" " * 19,
#                                             break_long_words=False,
#                                             replace_whitespace=False)
# =============================================================================

    print("-" * n_dashes + f" PROBLEM {problem_number} " + "-" * n_dashes + "\n")
    print(f"Title : {title} \n")
    print(f"Statement : {text_statement}")
    print(f"Time taken : {time_taken} seconds \n")
    print(f"Short Answer : {short_answer} \n")
    print(f"Detailed answer : {text_detailed_answer} \n")
    print("-" * max_len)