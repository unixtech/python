from collections import OrderedDict


def ordereddict_examples():
    ordered_dict = OrderedDict()
    ordered_dict['red'] = 4
    ordered_dict['blue'] = 9
    ordered_dict['green'] = 1
    print(ordered_dict)
    ordered_dict['yellow'] = 11
    print(ordered_dict)
    del ordered_dict['red']
    print(ordered_dict)
    ordered_dict['red'] = 5
    print(ordered_dict)
    ordered_dict.move_to_end('blue')
    print(ordered_dict)
    ordered_dict.move_to_end('red', last=False)


if __name__ == '__main__':
    ordereddict_examples()

