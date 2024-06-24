import re
import string
from collections import Counter
from Levenshtein import distance
import nltk
nltk.download('punkt')

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
    sentence_endings = re.compile(
        r'(?<!\w\.\w\.)(?<![A-Z][a-z]\.)(?<!\.\.\.)(?<!\d\.\d)(?<=[.?!])(?=\s+[A-Z])'
    )
    sentences = sentence_endings.split(text)
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


# Функция получения уникальных слов с nltk
def get_unique_words_nltk(text):
    words = nltk.word_tokenize(text.lower())
    unique_words = set(words)
    return unique_words


# Функция подсчета предложений и их длины с nltk
def get_sentences_info_nltk(text):
    sentences = nltk.sent_tokenize(text)
    number_of_sentences = len(sentences)
    total_length_of_sentences = sum(len(nltk.word_tokenize(sentence)) for sentence in sentences)
    return number_of_sentences, total_length_of_sentences


# Функция подсчета частоты слов с nltk
def get_word_frequency_nltk(text):
    words = nltk.word_tokenize(text.lower())
    word_frequency = Counter(words)
    return word_frequency


def main():
    # Загрузка текста
    text = read_file('text.txt')

    if text:
        # Подсчет уникальных слов
        unique_words = get_unique_words(text)
        unique_words_nltk = get_unique_words_nltk(text)
        print(f"Количество уникальных слов: {len(unique_words)}")
        print(f"Количество уникальных слов (nltk): {len(unique_words_nltk)}")
        print(f"Различие между get_unique_words и get_unique_words_nltk {unique_words_nltk-unique_words}")

        # Подсчет гласных и согласных
        vowels, consonants = count_vowels_and_consonants(text)
        print(f"Гласные: {vowels}")
        print(f"Согласные: {consonants}")

        # Подсчет количества и длины предложений
        number_of_sentences, total_length_of_sentences = get_sentences_info(text)
        number_of_sentences_nltk, total_length_of_sentences_nltk = get_sentences_info_nltk(text)
        print(f"Количество предложений: {number_of_sentences}")
        print(f"Количество предложений (nltk): {number_of_sentences_nltk}")
        print(f"Общая длина предложений: {total_length_of_sentences}")
        print(f"Общая длина предложений (nltk): {total_length_of_sentences_nltk} - Тут 431 это знаки пунктуации")
        # Тут 431 это знаки пунктуации

        # Подсчет частоты слов с учетом схожести
        word_frequency_with_similarity = get_word_frequency_with_similarity(text)
        print("Частота слов с учетом схожести:")
        for word, count in word_frequency_with_similarity.most_common():
            print(f"{word}: {count}")

        # Подсчет частоты слов с nltk
        word_frequency_nltk = get_word_frequency_nltk(text)
        print("Частота слов (nltk):")
        for word, count in word_frequency_nltk.most_common():
            print(f"{word}: {count}")

        # Получение 10 самых часто встречающихся слов
        top_10_words = get_top_10_words(word_frequency_with_similarity)
        top_10_words_nltk = get_top_10_words(word_frequency_nltk)
        print("10 самых часто встречающихся слов:")
        for word, count in top_10_words:
            print(f"{word}: {count}")
        print("10 самых часто встречающихся слов (nltk):")
        for word, count in top_10_words_nltk:
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()
