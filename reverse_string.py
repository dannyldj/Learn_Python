from typing import List

str_list: List[str] = ['h', 'e', 'l', 'l', 'o']


def reverse_string(s: List[str]) -> None:
    s.reverse()


reverse_string(str_list)
print(str_list)
