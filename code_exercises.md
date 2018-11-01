# Code Exercises

## FizzBuzz

n % 3 == 0 -> Fizz
n % 5 == 0 -> Buzz
n % 3 == 0 and n % 5 == 0 -> FizzBuzz

```python
print(" ".join(["Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i) for i in range(1,100)]))
```

## Odd Occurrences

```python
from itertools import groupby


def filter_odd_ocurrences(array):
    counts = [(i, len(list(c))) for i, c in groupby(sorted(array))]
    return [element for element, count in counts if count % 2 != 0]


if __name__ == '__main__':
    letters = ['a', 'b', 'c', 'a']
    filtered_letters = filter_odd_ocurrences(letters)
    assert filtered_letters == ['b', 'c']
```

## Create Tree based on Hierarchy markup