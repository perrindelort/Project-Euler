# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 23:59:59 2024

@author: Antoine
"""

from bs4 import BeautifulSoup
import re

REPLACEMENTS = {'</p>' : '\n',
                '$' : '',
                '\dots' : '...',
                '\\times' : '×',
                '\,' : ' '
                }

REGEX_SUB = {r'<span class="tooltiptext">.*?</span></strong>' : ''}

        
def html_to_string(html_code):
    for old, new in REPLACEMENTS.items():
        html_code = html_code.replace(old, new)
    for pattern, replacement in REGEX_SUB.items():
        html_code = re.sub(pattern, replacement, html_code, flags=re.DOTALL)
    soup = BeautifulSoup(html_code, 'html.parser')
    return soup.get_text()


def get_statement(problem_number):
    filename = f"././data/html_statements/problem_{problem_number}.txt"

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        
    return html_to_string(content)