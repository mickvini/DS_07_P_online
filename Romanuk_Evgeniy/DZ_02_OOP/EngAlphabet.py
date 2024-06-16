import string
import Alphabet


class EngAlphabet(Alphabet.Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('en_EN', list(string.ascii_letters))

    def is_en_letter(self, letter):
        return letter in self.letters

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque in orci nec orci molestie maximus."


def main():
    eng_alphabet = EngAlphabet()

    # Выводим буквы алфавита
    eng_alphabet.print()

    # Получаем количество букв в алфавите
    print(eng_alphabet.letters_num())

    # Проверяем, является ли символ 'F' английской буквой
    print(eng_alphabet.is_en_letter('F'))

    # Проверяем, является ли символ 'Щ' английской буквой
    print(eng_alphabet.is_en_letter('Щ'))

    # Пример текста на английском языке
    print(EngAlphabet.example())


if __name__ == "__main__":
    main()
