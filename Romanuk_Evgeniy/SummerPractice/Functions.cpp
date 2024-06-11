#include "Functions.h"


std::set<std::string> getUniqueWords(std::string& text)
{
	std::set<std::string> uniqueWords;																		// Юзаем сет, потому что это удобно, во первых сам сортирует,
																											// во вторых при добавлении одинаковых значении хранит только один экземпляр
	std::istringstream iss(text);																			// istringstream позволяет обрабатывать строку как поток, в принципе можно
																											// было и просто разбить текст на слова получить массив строк и работать уже с ними
	std::string word;

	while (iss >> word) {
		// Удаляем пунктуацию и приводим к нижнему регистру
		word.erase(remove_if(word.begin(), word.end(), [](char c) { return ispunct(c); }), word.end());
		for (auto& c : word) c = tolower(c);
		uniqueWords.insert(word);
	}
	/*for (std::set<std::string>::iterator it = uniqueWords.begin(); it != uniqueWords.end(); ++it)
		std::cout << *it << std::endl;*/
	std::cout << uniqueWords.size() << std::endl;															// по таску нужно считать число уникальных слов


	return uniqueWords;																						// Вообще возвращаю, но нигде не юзаю
}

void countVowelsAndConsonants(std::string& text) {															// Считает число гласных и согласных, но только латинского алфавита
	int vowels = 0;
	int consonants = 0;
	for (char c : text) {
		if (isalpha(c)) {
			char lower_c = tolower(c);
			if (lower_c == 'a' || lower_c == 'e' || lower_c == 'i' || lower_c == 'o' || lower_c == 'u') {
				++vowels;
			}
			else {
				++consonants;
			}
		}
	}
	std::cout << vowels << std::endl << consonants << std::endl;
																											// А вот тут ничего не возвращаю
}

std::string readFile(const std::string& filename) {
	std::ifstream file(filename);
	std::stringstream buffer;
	buffer << file.rdbuf();
	return buffer.str();
}