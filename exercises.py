from itertools import groupby


def filter_odd_ocurrences(array):
    counts = [(i, len(list(c))) for i, c in groupby(sorted(array))]
    return [element for element, count in counts if count % 2 != 0]


def hyerarchy_from_markup(array):
    return None


if __name__ == '__main__':
    print("FizzBuzz:\n")
    print(" ".join(["Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i) for i in range(1, 100)]))

    print("Odd Ocurrences:\n")
    letters = ['a', 'b', 'c', 'a']
    filtered_letters = filter_odd_ocurrences(letters)
    assert filtered_letters == ['b', 'c']

    print("Hyerachy from Markup:\n")
    markup = [
        'H1 Root',
        'H2 Child',
        'H3 Sub Child',
        'H2 Sibling',
        'H3 Sub Child Sibling',
    ]
    expected_tree = {
        'Root': [
            {'Child': [
                {'Sub Child': []}
            ]},
            {'Sibling': [
                {'Sub Child Sibling': []}
            ]},
        ]
    }

    assert expected_tree == hyerarchy_from_markup(markup)
