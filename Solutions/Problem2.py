import array
from operator import mul
from functools import reduce

arr = array.array('i', [1, 2, 3, 4, 5])
result = list()
prod = reduce(mul, arr.tolist(), 1)

for i in arr:
    result.append(round(prod / i))

print(result)