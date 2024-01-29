import random


def convert_library_to_list(library):
    word_list = open(library).read().split()

    return word_list


def replace_words(original_sentence, word_list):
    original_sentence = original_sentence.split()
    new_sentence = []

    for word in original_sentence:
        # reject special characters/numbers
        if word.isalpha():
            new_word = find_matching_word(word, word_list)
            new_sentence.append(new_word)
        else:
            new_sentence.append(word)

    modified_sentence = " ".join(new_sentence)

    return modified_sentence


def find_matching_word(original_word, word_list):
    # filter based on criteria
    # same first letter + length
    matching_words = [
        new_word
        for new_word in word_list
        if new_word[0] == original_word[0] and len(new_word) == len(original_word)
    ]

    if matching_words:
        # generate unique output
        matching_word = random.choice(matching_words)
    else:
        # return original if no match
        matching_word = original_word

    return matching_word