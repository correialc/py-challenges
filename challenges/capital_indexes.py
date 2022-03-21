def find_capital_indexes(one_string):
    return [idx for idx, value in enumerate(one_string) if value.isupper()]