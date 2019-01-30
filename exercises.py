from itertools import groupby


def filter_odd_ocurrences(array):
    counts = [(i, len(list(c))) for i, c in groupby(sorted(array))]
    return [element for element, count in counts if count % 2 != 0]


def hyerarchy_from_markup(array):
    class Heading:
        def __init__(self, str):
            [level, title] = str.split(' ')
            self.level = level[1:]
            self.title = title

        def __repr__(self):
            return self.__str__()

        def __str__(self):
            return "{} - {}".format(self.level, self.title)

    def get_children(parent_level, children_str):
        pass

    root = Heading(array[0])
    tree = {root: get_children(root.level, array[1:])}
    return tree


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
    # expected_tree = {
    #     'Root': [
    #         {'Child': [
    #             {'Sub Child': []}
    #         ]},
    #         {'Sibling': [
    #             {'Sub Child Sibling': []}
    #         ]},
    #     ]
    # }

    from pprint import pprint as pp
    pp(hyerarchy_from_markup(markup))

    count = 1
    for i in range(1, 1800):
        if (
            i % 2 == 0 and
            i % 4 == 0 and
            i % 6 == 0 and
            i % 8 == 0 and
            i % 10 == 0 and
            i % 12 == 0
        ):
            count += 1
    print("Total together: {}".format(count))
