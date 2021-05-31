import array
from operator import mul
from functools import reduce

# Using division
arr = array.array('i', [3, 2, 1])
result = list()
prod = reduce(mul, arr.tolist(), 1)

for i in arr:
    result.append(prod // i)

print(result)

# Another way without division
arr = array.array('i', [1, 2, 3, 4, 5])
x = list()
result = list()

for i in arr:
    x = arr.tolist()
    x.pop(arr.index(i))
    result.append(reduce(mul, x, 1))

print(result)