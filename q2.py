import math
def special_percentile(percent: int, numbers: list) -> float:
    index: int = (math.floor((percent/100) * len(numbers)))
    nums_sorted = sorted(numbers)
    return nums_sorted[index]


print(special_percentile(50, [5, 6, 8, 45, 4, 15, 7]))