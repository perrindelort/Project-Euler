from util.util import timing, format_number
from scripts.abstract_problem import Problem


class Problem19(Problem):
    def __init__(self, **kwargs):
        super().__init__()

        if "final_year" not in kwargs.keys():
            raise ValueError("final_year not specified")

        self.answer, self.time_taken = self.solve(final_year=kwargs["final_year"])

        self.detailed_answer = f"The number of sundays that fell on the first of the month during the 20th century is {format_number(self.answer)}"

    # TODO : move function to utils
    def number_of_first_sundays(self, first_day, year):
        compte = 0
        if first_day % 7 == 0:
            compte += 1
        for i in range(1, 12):
            elapsed_days = 0
            if i == 2:
                elapsed_days += 28 + year % 400

            # 30 days monts
            elif i in [4, 6, 9, 11]:
                elapsed_days += 30
            else:
                elapsed_days += 31
            if (elapsed_days + first_day) % 7 == 0:
                compte += 1
        return compte

    def hom_many_days(self, year):
        days = 30 * 4 + 7 * 31 + 28
        if self.is_leap_year(year):
            days += 1
        return days

    def is_leap_year(self, year):
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            if year % 4 == 0:
                return True
            return False

    @timing
    def solve(self, final_year: int) -> int:
        year = 1900
        first_day = 1
        count = 0
        while year != final_year + 1:
            count += self.number_of_first_sundays(first_day, year)
            first_day = (first_day + self.hom_many_days(year)) % 7
            year += 1
        return count


if __name__ == "__main__":
    problem = Problem19(final_year=2_000)
    problem.print_problem()
