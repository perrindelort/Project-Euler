import re

from abc import ABC, abstractmethod
from typing import Optional, Any

from util.statements import get_statement
from util.titles import get_title
from util.util import (
    format_statement_answer,
    load_data_from_txt,
    timing,
)
from util.const import ANSWERS


class Problem(ABC):
    problem_number: int
    title: str
    statement: str
    time_taken: int
    answer: str
    detailed_answer: str

    def __init__(self):
        match = re.search(r"(?P<problem_number>(\d+)$)", self.__class__.__name__)
        if match:
            self.problem_number = int(match.group("problem_number"))
        else:
            raise Exception("No problem number was found")
        self.title = get_title(self.problem_number)
        self.statement = get_statement(self.problem_number)

        self.true_answer = ANSWERS[self.problem_number]

    @timing
    @abstractmethod
    def solve(self, **kwargs) -> Any:
        raise NotImplementedError

    def assert_answer(self) -> None:
        return str(self.answer) == str(self.true_answer)

    def load_data_from_txt(
        self,
        split: Optional[bool] = True,
        sep: Optional[str] = ",",
        use_numpy: Optional[bool] = False,
    ) -> None:
        return load_data_from_txt(
            problem_number=self.problem_number,
            split=split,
            sep=sep,
            use_numpy=use_numpy,
        )

    def print_problem(self) -> None:
        format_statement_answer(
            problem_number=self.problem_number,
            title=self.title,
            statement=self.statement,
            time_taken=self.time_taken,
            short_answer=self.answer,
            detailed_answer=self.detailed_answer,
            correct_answer=self.assert_answer(),
        )
