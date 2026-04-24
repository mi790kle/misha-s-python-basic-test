import math
def special_percentile(percent: int, numbers: list) -> float:
    index: int = (math.floor((percent/100) * len(numbers)))
    nums_sorted = sorted(numbers)
    return nums_sorted[index]


print(special_percentile(25, [40, 10, 30, 20]))
print(special_percentile(25, [50, 10, 40, 30, 20]))
print(special_percentile(50, [9, 1, 7, 3]))
