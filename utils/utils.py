from typing import List, Dict


def score_ratio(data: Dict[str: List[int]]):
    """Fluency, Adequacy, Ranking
        점수를 100%로 나타낸다.
    :param data: {'judge': [xx, xx, xx, ...]}
    """
    num_data = len(list(data.values())[0])
    scores = list(range(num_data))
    result = {}
    for k, values in data.items():
        num = sum((s+1) * int(vv) / 100 
                  for (s, vv) in zip(scores, values)) / num_data
        result[k] = round(num, 3)
    return result