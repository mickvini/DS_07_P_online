class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(" ".join(self.letters))

    def letters_num(self):
        # Буквы в алфавите это пара верхнего и нижнего регистра выводить просто len, неправильно
        return len(set(letter.lower() for letter in self.letters))


def main():
    alphabet = Alphabet("Ok", ('o', 'k', 'O', 'K'))

    # Выводим буквы алфавита
    alphabet.print()

    # Получаем количество букв в алфавите
    print((alphabet.letters_num()))


# Без данного условия в EngAlphabet на вывод бы сперва выводился main() из Alphabet
# Решается или импортирование части модуля скажем только класса Alpahbet или таким условием
# Вместе с тем, можем в EngAlphabet вызвать Alphabet.main(), если импортируем весь модуль
# По факту такой подход позволяет использовать два модуля как отдельные программы

if __name__ == "__main__":
    main()
