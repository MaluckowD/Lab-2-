import re
def filter_sentences(input_string):
    #sentences = input_string.split(".")
    sentences = re.split('!?.',input_string)
    filtered_sentences = []

    for sentence in sentences:
        words_and_numbers = sentence.split()
        words = [word for word in words_and_numbers if not word.isdigit()]
        numbers = [word for word in words_and_numbers if word.isdigit()]

        if len(words) >= len(numbers):
            filtered_sentences.append(sentence)

    filtered_string = ".".join(filtered_sentences)
    return filtered_string

input_string = input("Введите строку:")
filtered_string = filter_sentences(input_string)
print(filtered_string)