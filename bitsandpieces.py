def generate_word_list():
    valid_words = []
    with open('possible_words.txt', 'r', encoding=str) as file_n:
        for line in file_n:
            valid_words.append(line)
    return valid_words


all_black_letters = []
all_yellow_letters = []

repeating_letters = []
non_repeating_letters = []


def black_letter_filter(black_letters, valid_words):
    all_black_letters.append(black_letters)
    for letter in black_letters:
        if letter in all_yellow_letters:
            non_repeating_letters.append(letter)
        valid_words = list(filter(lambda word: letter not in word, valid_words))
    return valid_words


def yellow_letter_filter(yellow_letters, valid_words):
    # Yellow letters will be a tuple, (letter: str, position: List[int])
    # In the case of yellow letters, it can't be in any of the positions in the
    # list
    for letter, position in yellow_letters:
        if letter in all_yellow_letters:
            all_yellow_letters.append(letter)
            repeating_letters.append(letter)
        else:
            all_yellow_letters.append(letter)
        valid_words = list(filter(lambda word: letter in word, valid_words))
        valid_words = list(filter(lambda word: word[position] != letter,
                                  valid_words))
    return valid_words


def _repetition_checker(to_check):
    # to_check is a list of form ['letter', "word],
    # check if the letter is repeated in the word
    letter = to_check[0]
    word = to_check[1]
    return word.count(letter) > 1


def _non_repetition_checker(to_check):
    # to_check is a list of form ['letter', "word],
    # check if the letter is NOT repeated in the word
    letter = to_check[0]
    word = to_check[1]
    return word.count(letter) > 1


def repeating_or_non_repeating_letter_filter(valid_words):
    if repeating_letters:
        for letter in repeating_letters:
            valid_words = list(filter(_repetition_checker,
                                      [letter, valid_words]))
    if non_repeating_letters:
        for letter in non_repeating_letters:
            valid_words = list(filter(_non_repetition_checker,
                                      [letter, valid_words]))


def green_letter_filter(green_letters, valid_words):
    # Green letters will be a tuple, (letter: str, position: int)
    for letter, position in green_letters:
        valid_words = list(filter(lambda word: word[position] == letter,
                                  valid_words))
    return valid_words


def run_it_through_with_repeat():
    starting_words = generate_word_list()
    after_bl1 = black_letter_filter(['i', 't'], starting_words)
    after_yl1 = yellow_letter_filter([('r', 1), ('a', 2), ('e', 4)], after_bl1)
    print(len(after_yl1))
    print(after_yl1)

    after_bl2 = black_letter_filter(['b'], after_yl1)
    after_yl2 = yellow_letter_filter([('a', 0), ('m', 1), ('r', 4)], after_bl2)
    after_gl2 = green_letter_filter([('e', 3)], after_yl2)
    print(len(after_gl2))
    print(after_gl2)
    after_bl3 = black_letter_filter(['h'], after_gl2)
    after_yl3 = yellow_letter_filter([('m', 4), ('r', 2)], after_bl3)
    after_gl3 = green_letter_filter([('a', 1), ('e', 3)], after_yl3)
    print(len(after_gl3))
    print(after_gl3)

    #
    # after_bl2 = black_letter_filter(['b', 'r', 'y'], after_yl1)
    # print("afterBL2")
    # print(len(after_bl2))
    # after_yl2 = yellow_letter_filter([('r', 2), ('e', 1)], after_bl2)
    # print("afterYL2")
    # print(len(after_yl2))


run_it_through_with_repeat()

# How to know when we have a repeating letter:
# 2 yellows in the same word
#
