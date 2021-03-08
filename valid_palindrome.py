from typing import List

string: str = input()
str_list: List[str] = []


def is_palindrome(s: str) -> bool:
    for char in s:
        if char.isalnum():
            str_list.append(char.lower())
    if str_list == str_list[::-1]:
        return True
    return False


if not is_palindrome(string):
    print('False')
else:
    print('True')
