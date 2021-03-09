import collections
import re
from typing import List

paragraph: str = "Bob hit a ball, the hit BALL flew far after it was hit."
ban_list: List[str] = ["hit"]


def most_common_word(s: str, banned: List[str]) -> str:
    # 리스트 컴프리헨션 학습
    str_list = [word for word in re.sub(r'[^\w]', ' ', s).lower().split()
                if word not in banned]
    count_dict = collections.Counter(str_list)
    return count_dict.most_common(1)[0][0]


print(most_common_word(paragraph, ban_list))
