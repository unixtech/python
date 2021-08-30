from collections import defaultdict


def defaultdict_examples():
    repeated_letters = 'abdegadlbdaalg'
    letter_cnt = defaultdict(int)
    for letter in repeated_letters: 
        letter_cnt[letter] += 1
    print("Letter Counts: ", letter_cnt)


if __name__ == '__main__':
    defaultdict_examples()

