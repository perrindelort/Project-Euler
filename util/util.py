import os
import re
import numpy as np
import functools
import textwrap

from typing import Callable, Optional, Union, Any, AnyStr, List
from numpy.typing import NDArray
from time import perf_counter_ns
from termcolor import colored


from util.const import N_DASHES


def load_data_from_txt(
    problem_number: int,
    split: Optional[bool] = True,
    sep: Optional[str] = ",",
    use_numpy: Optional[bool] = False,
) -> Union[str, NDArray, List[Union[str, NDArray]]]:
    # TODO : better type hints
    problem_number_str = str(problem_number).zfill(4)
    path = f"././data/data/problem_{problem_number_str}.txt"
    if use_numpy:
        return np.loadtxt(path, delimiter=sep)
    file = open(path, "r")
    if split:
        if sep == "\n":
            return file.read().split(sep=sep)[:-1]
        else:
            return file.read().split(sep=sep)
    else:
        return file.read()


def format_number(number: int) -> str:
    return format(number, ",")


def timing(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        beginning = perf_counter_ns()
        answer = func(*args, **kwargs)
        end = perf_counter_ns()
        return answer, (end - beginning) * (10**-9)

    return wrapper


def format_statement_answer(
    problem_number,
    title,
    statement,
    time_taken,
    short_answer,
    detailed_answer,
    correct_answer,
    n_dashes=N_DASHES,
) -> None:
    os.system("cls")

    max_len = 2 * n_dashes + 10 + problem_number // 10 + 1
    statement_indent = "Statement : "
    detailed_answer_indent = "Detailed answer : "
    first_sentence_statement = textwrap.fill(
        statement.split("\n")[0],
        width=max_len,
        initial_indent="",
        subsequent_indent=" " * len(statement_indent),
        break_long_words=False,
        replace_whitespace=False,
    )
    text_statement = (
        first_sentence_statement
        + "\n"
        + "\n".join(
            textwrap.fill(
                l,
                width=max_len,
                initial_indent=" " * len(statement_indent),
                subsequent_indent=" " * len(statement_indent),
                break_long_words=False,
                replace_whitespace=False,
            )
            for l in statement.split("\n")[1:]
        )
    )

    first_sentence_detailed_answer = textwrap.fill(
        detailed_answer.split("\n")[0],
        width=max_len,
        initial_indent="",
        subsequent_indent=" " * len(detailed_answer_indent),
        break_long_words=False,
        replace_whitespace=False,
    )
    text_detailed_answer = (
        first_sentence_detailed_answer
        + "\n"
        + "\n".join(
            textwrap.fill(
                l,
                width=max_len,
                initial_indent=" " * len(detailed_answer_indent),
                subsequent_indent=" " * len(detailed_answer_indent),
                break_long_words=False,
                replace_whitespace=False,
            )
            for l in detailed_answer.split("\n")[1:]
        )
    )

    print("-" * n_dashes + f" PROBLEM {problem_number} " + "-" * n_dashes + "\n")
    print(f"Title : {title} \n")
    print(f"Statement : {text_statement}")
    print(f"Time taken : {time_taken} seconds \n")
    print(f"Short Answer : {short_answer} \n")
    print(f"Detailed answer : {text_detailed_answer} \n")
    (
        print(f"Answer : {colored('Correct', 'green')} \n")
        if correct_answer == True
        else print(f"Answer : {colored('False', 'red')} \n")
    )
    print("-" * max_len)
