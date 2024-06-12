#include "Functions.h"
#include <sstream>
#include <algorithm>

std::set<std::string> getUniqueWords(const std::string& text)
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
	//std::cout << uniqueWords.size() << std::endl;															// по таску нужно считать число уникальных слов


	return uniqueWords;																						// UPD теперь юзаю
}

std::tuple<int, int> countVowelsAndConsonants(const std::string& text) {															// Считает число гласных и согласных, но только латинского алфавита
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
	//std::cout << vowels << std::endl << consonants << std::endl;
	return std::make_tuple(vowels, consonants);																						// UPD: Теперь возвращаю

}

//https://ru.wikibooks.org/wiki/%D0%A0%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8_%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D0%BE%D0%B2/%D0%A0%D0%B0%D1%81%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D0%B5_%D0%9B%D0%B5%D0%B2%D0%B5%D0%BD%D1%88%D1%82%D0%B5%D0%B9%D0%BD%D0%B0
template<typename T>
typename T::size_type levenshteinDistance(const T& source,	const T& target) {
	if (source.size() > target.size()) {
		return levenshteinDistance(target, source);
	}

	using TSizeType = typename T::size_type;
	const TSizeType min_size = source.size(), max_size = target.size();
	std::vector<TSizeType> lev_dist(min_size + 1);

	for (TSizeType i = 0; i <= min_size; ++i) {
		lev_dist[i] = i;
	}

	for (TSizeType j = 1; j <= max_size; ++j) {
		TSizeType previous_diagonal = lev_dist[0], previous_diagonal_save;
		++lev_dist[0];

		for (TSizeType i = 1; i <= min_size; ++i) {
			previous_diagonal_save = lev_dist[i];
			if (source[i - 1] == target[j - 1]) {
				lev_dist[i] = previous_diagonal;
			}
			else {
				lev_dist[i] = std::min(std::min(lev_dist[i - 1], lev_dist[i]), previous_diagonal) + 1;
			}
			previous_diagonal = previous_diagonal_save;
		}
	}

	return lev_dist[min_size];
}
// Функция для определения, являются ли два слова схожими, расстояние по умолчанию 2
bool areWordsSimilar(const std::string& word1, const std::string& word2, int threshold = 2)
{
	return levenshteinDistance(word1, word2) <= threshold;
}
// Количество предложении в тексте, длину предложений(всех)
std::tuple<int, int> getCountAndLenghtOfSentences(const std::string& text)
{
	std::vector<std::string> sentences;
	std::istringstream sentenceStream(text);
	std::string sentence;
	while (std::getline(sentenceStream, sentence, '.')) {
		if (!sentence.empty()) {
			sentences.push_back(sentence);
		}
	}
	int totalWordCount = 0;
	for (const auto& s : sentences) {
		std::istringstream wordStream(s);
		std::string word;

		while (wordStream >> word) {
			++totalWordCount;
		}
	}
	return std::make_tuple(sentences.size(), totalWordCount);
}

std::map<std::string, int> getNumberOfUsesOfEachWordWithSimilliarCriterion(const std::string& text)
{
	std::map<std::string, int> wordFrequency;
	std::istringstream wordStream(text);
	std::string word;
	std::set<std::string> processedWords;

	while (wordStream >> word) {
		word.erase(std::remove_if(word.begin(), word.end(), [](char c) { return ispunct(c); }), word.end());
		for (auto& c : word) c = tolower(c);

		bool foundSimilar = false;
		for (const auto& processedWord : processedWords) {
			if (areWordsSimilar(word, processedWord)) {
				wordFrequency[processedWord]++;
				foundSimilar = true;
				break;
			}
		}

		if (!foundSimilar) {
			wordFrequency[word]++;
			processedWords.insert(word);
		}
	}
	
	return wordFrequency;
}

std::vector<std::pair<std::string, int>> getTenMostFrequentlyEncounteredWords(const std::string& text)
{
	auto wordFrequency = getNumberOfUsesOfEachWordWithSimilliarCriterion(text);

	std::vector<std::pair<std::string, int>> wordFrequencyVec(wordFrequency.begin(), wordFrequency.end());

	std::sort(wordFrequencyVec.begin(), wordFrequencyVec.end(), [](const auto& a, const auto& b) {
		return b.second < a.second;
		});

	if (wordFrequencyVec.size() > 10) {
		wordFrequencyVec.resize(10);
	}

	return wordFrequencyVec;
}