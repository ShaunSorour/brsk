import helpers


# Swap out library here
library_file = "word-library.txt"
word_list = helpers.convert_library_to_list(library_file)
first_time = True 

while True:
    if first_time:
        print('Welcome to Scrabble Pro! \U0001F3B2 \n'
            '\nHow to: Type your sentence at the prompt, press Enter,'
            ' watch the magic unfold \n')
        first_time = False


    input_sentence = input("Enter a sentence ('Esc' to quit): ")

    if input_sentence.lower() == '\x1b':
        print("Exiting program. Happy Scrabbling!")
        break

    new_sentence = helpers.replace_words(input_sentence, word_list)
    print("\nUpdated sentence: " + new_sentence)