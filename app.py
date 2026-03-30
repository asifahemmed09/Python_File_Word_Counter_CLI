import string


def count_words(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        data_without_symbols = data.translate(str.maketrans('', '', string.punctuation))
        new_data = [word for word in data_without_symbols.split() if word.isalpha()]
        word_count = len(new_data)
    return word_count

file_name = input("Enter the file name you want to read and count the words: ")

word_count = count_words(file_name)
print(f"The number of words in the file is: {word_count}")