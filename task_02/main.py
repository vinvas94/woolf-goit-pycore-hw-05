import re
from typing import Callable


def generator_numbers(text: str):
    pattern=r"\b\d+(?:\.\d+)?\b"
    matches=  re.findall(pattern,text)
    if not matches:
        raise ValueError('Not found any numbers in the text.')
    for match in matches: 
        yield float(match)


def sum_profit(text: str, func: Callable):
    try:
        return sum(func(text))
    except ValueError as e:
        print(f"Error:{e}")
        return 0



# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
text = "Загальний дохід працівника складається з декількох частин: як основний дохід, доповнений додатковими надходженнями  доларів."


total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")



