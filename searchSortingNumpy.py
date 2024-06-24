import numpy as np
arr = np.array([1,2,3,9,5,9,7,8,9])
## find indices where 9 is present
find = np.where(arr == 9)
print(find)

## find even number indices
even = np.where(arr % 2 == 0)
print(even)

## sorting ascending order
print(np.sort(arr))

## sorting descending  order
arrTwo = ['banana', 'apple', 'cherry', 'peach', 'watermelon']
print(np.sort(arrTwo)[::-1])