import string


alphabeth = list(string.ascii_lowercase)
vowels = list('aeiou')
forbidden_combinations = ['ab', 'cd', 'pq', 'xy']


def is_nice_string(teststring):
    # Remobe all the \n and white spaces
    teststring = teststring.rstrip()
    len_teststring = len(teststring)

    has_three_vowels = False
    has_repeated_letter = False

    num_vowels = 0
    for pos, letter in enumerate(teststring, start=1):
        # first criteria:
        if not has_three_vowels:
            if letter in vowels:
                num_vowels += 1
            if num_vowels >= 3:
                has_three_vowels = True
        if not (pos >= len_teststring):
            # second criteria:
            if not has_repeated_letter:
                if alphabeth.index(letter) == alphabeth.index(teststring[pos]):
                    has_repeated_letter = True
            # third criteria:
            combination = letter + teststring[pos]
            if combination in forbidden_combinations:
                return False
    return has_three_vowels and has_repeated_letter

with open('data.txt', 'r') as f:
    nice_strings = 0
    content = f.readlines()
    for line in content:
        if is_nice_string(line):
            nice_strings += 1
    print nice_strings
