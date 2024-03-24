# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 23:59:59 2024

@author: Antoine
"""

from bs4 import BeautifulSoup
import re
import PIL.Image
from pylatexenc.latex2text import LatexNodes2Text

REPLACEMENTS = {'</p>' : '\n',
                '$' : '',
                '\dots' : '...',
                r'\cdots' : '...',
                '\\times' : '×',
                '\,' : ' ',
                '&amp;\colon' : ':',
                r'\begin{align}' : '',
                r'\end{align}' : '',
                '\mathbf' : '',
                r'\\' : '',
                r'\to' : '→',
                r'\ne' : '≠',
                r'\lt' : '<',
                '&=' : '=',
                '<br>' : '\n',
                r'\le' : '≤',
                'amp;' : '',
                '=' : ' = ',
                }

LATEX_REPLACEMENT = {r'\lt' : '<',
                     r'\le' : '≤',
                     r'\ne' : '≠'}

REGEX_LATEX = {r"\\dfrac\s*(\w+)\s*(\w+)" : r"\1/\2",
               r"\\dfrac\s*(\w)\s*(\w)" :  r"\1/\2",
               r"\\dfrac\s*(\d)\s*(\d)" :  r"\1/\2"}

REGEX_SUB = {r'<span class="tooltiptext">.*?</span></strong>' : '',
             r'\{(\d+)\}': r'\1'}

        
# =============================================================================
# def html_to_string(html_code):
#     for old, new in REPLACEMENTS.items():
#         html_code = html_code.replace(old, new)
#     for pattern, replacement in REGEX_SUB.items():
#         html_code = re.sub(pattern, replacement, html_code, flags=re.DOTALL)
#     soup = BeautifulSoup(html_code, 'html.parser')
#     return soup.get_text()
# =============================================================================


# =============================================================================
# def html_to_string(html_code, problem_number):
#     soup = BeautifulSoup(html_code, 'html.parser')
#         
#     # Find the <img> tag
#     img_tag = soup.find('img')
# 
#     if img_tag:
#         img_src = img_tag['src']
#         
#         problem_number_str = str(problem_number).zfill(4)
#         ascii_img = png_to_ascii(f"././data/images/problem_{problem_number_str}.png")
# 
#         img_tag.replace_with(ascii_img)
# 
#     txt = soup.get_text() 
# 
#     # Remove HTML tags and perform other replacements as needed
#     for old, new in REPLACEMENTS.items():
#         txt = txt.replace(old, new)
#         
#     for pattern, replacement in REGEX_SUB.items():
#         txt = re.sub(pattern, replacement, txt, flags=re.DOTALL)
# 
#     return txt
# =============================================================================

def html_to_string(html_code, problem_number):
    for old, new in LATEX_REPLACEMENT.items():
        html_code = html_code.replace(old, new)
        
    for pattern, replacement in REGEX_LATEX.items():
        html_code = re.sub(pattern, replacement, html_code)
        
    html_code = LatexNodes2Text().latex_to_text(html_code)
    soup = BeautifulSoup(html_code, 'html.parser')

    img_tag = soup.find('img')
    
    if img_tag:
        img_src = img_tag['src']
            
        problem_number_str = str(problem_number).zfill(4)
        ascii_img = png_to_ascii(f"././data/images/problem_{problem_number_str}.png")
    
        img_tag.replace_with(ascii_img)
    
    txt = soup.get_text() 
    # Remove HTML tags and perform other replacements as needed
    for old, new in REPLACEMENTS.items():
        txt = txt.replace(old, new)
           
    for pattern, replacement in REGEX_SUB.items():
        txt = re.sub(pattern, replacement, txt, flags=re.DOTALL)
    return txt

def png_to_ascii(image_path, new_width = 90):
     
    try:
      img = PIL.Image.open(image_path)
    except:
      raise ValueError(f"Unable to find image located at {image_path}");
     
    width, height = img.size
    aspect_ratio = height/width
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
     
    img = img.convert('L')
     
    chars = ["@", " ", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
     
    pixels = img.getdata()
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    return ascii_image

def get_statement(problem_number):
    problem_number_str = str(problem_number).zfill(4)
    filename = f"././data/html_statements/problem_{problem_number_str}.txt"

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        
    return html_to_string(content,problem_number)