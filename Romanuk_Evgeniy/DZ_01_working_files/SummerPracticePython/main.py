import re
import string
from collections import Counter
from Levenshtein import distance


# Функция чтения файла
def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        return text
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return ""


# Функция получения уникальных слов
def get_unique_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = set(words)
    return unique_words


# Функция подсчета гласных и согласных
def count_vowels_and_consonants(text):
    vowels = 0
    consonants = 0
    for char in text.lower():
        if char in string.ascii_letters:                     
            if char in 'aeiouy':
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants


# Функция подсчета предложений и их длины
def get_sentences_info(text):
    sentences = re.split(r'[.!?]', text)    
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    number_of_sentences = len(sentences)
    total_length_of_sentences = sum(len(re.findall(r'\b\w+\b', sentence)) for sentence in sentences)
    return number_of_sentences, total_length_of_sentences


# Функция проверки схожести слов (по расстоянию Левенштейна)
def are_words_similar(word1, word2, threshold=2):
    return distance(word1, word2) <= threshold


# Функция подсчета частоты слов с учетом схожести
def get_word_frequency_with_similarity(text, threshold=2):
    word_frequency = Counter()
    processed_words = set()
    for word in re.findall(r'\b\w+\b', text.lower()):
        word = word.strip()
        found_similar = False
        for processed_word in processed_words:
            if are_words_similar(word, processed_word, threshold):
                word_frequency[processed_word] += 1
                found_similar = True
                break
        if not found_similar:
            word_frequency[word] += 1
            processed_words.add(word)
    return word_frequency


# Функция получения 10 самых часто встречающихся слов
def get_top_10_words(word_frequency):
    top_10_words = word_frequency.most_common(10)
    return top_10_words


# Функция основного кода
def main():
    # Загрузка текста
    text = read_file('text.txt')

    if text:
        # Подсчет уникальных слов
        unique_words = get_unique_words(text)
        print(f"Количество уникальных слов: {len(unique_words)}")

        # Подсчет гласных и согласных
        vowels, consonants = count_vowels_and_consonants(text)
        print(f"Гласные: {vowels}")
        print(f"Согласные: {consonants}")

        # Подсчет количества и длины предложений
        number_of_sentences, total_length_of_sentences = get_sentences_info(text)
        print(f"Количество предложений: {number_of_sentences}")
        print(f"Общая длина предложений: {total_length_of_sentences}")

        # Подсчет частоты слов с учетом схожести
        word_frequency_with_similarity = get_word_frequency_with_similarity(text)
        print("Частота слов с учетом схожести:")
        for word, count in word_frequency_with_similarity.most_common():
            print(f"{word}: {count}")

        # Получение 10 самых часто встречающихся слов
        top_10_words = get_top_10_words(word_frequency_with_similarity)
        print("10 самых часто встречающихся слов:")
        for word, count in top_10_words:
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()
