from typing import List


def find_capital_indexes(text: str) -> List:
    return [i for i, v in enumerate(text) if v.isupper()]
