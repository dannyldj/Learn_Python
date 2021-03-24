import collections
from typing import List

str_list: List[str] = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(s: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in s:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()


print(group_anagrams(str_list))
