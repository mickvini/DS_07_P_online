#include "Menu.h"
#include "Functions.h"

bool showMenu(const std::vector<std::pair<std::string, MenuFunction>>& options, std::string& text)
{
    int choice = 0;
    do {
        system("cls"); // Тут моментик в том, что system чисто под винду
        std::cout << "Menu:\n";
        for (size_t i = 0; i < options.size(); ++i) {
            std::cout << (i + 1) << ". " << options[i].first << "\n";
        }
        std::cout << "0. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        if (choice > 0 && choice <= options.size()) {
            options[choice - 1].second(text);
        }
        else if (choice != 0) {
            std::cout << "Invalid choice, please try again." << std::endl;            
        }
        system("pause");
    } while (choice != 0);

    std::cout << "Exiting menu." << std::endl;
	return true;
}

void firstOption(const std::string& text)
{
    std::cout << "Count of UniqueWords: " << getUniqueWords(text).size() << std::endl;
}

void secondOption(const std::string& text)
{
    auto [vowels, consonants] = countVowelsAndConsonants(text);
    std::cout << "Vowels: " << vowels << "\nConsonants: " << consonants << std::endl;
}
// 4 задачу из TODO следует разбить на две подзадачи, считаем количество предложениё и длину это первая задача
// количество использования каждого слова в тексте с критерием схожести это два от этого и работаем
void thirdOption(const std::string& text)
{    
    auto [countOfSentences, totalLenghtOfSentences] = getCountAndLenghtOfSentences(text);
    std::cout << "Count of sentences: " << countOfSentences << "\nTotal lenght of sentences: " << totalLenghtOfSentences << std::endl;

    for (const auto& pair : getNumberOfUsesOfEachWordWithSimilliarCriterion(text)) {
        std::cout << pair.first << ": " << pair.second << " times\n";
    }

}
void fourOption(const std::string& text)
{
    auto topWords = getTenMostFrequentlyEncounteredWords(text);
    std::cout << "Top 10 most frequent words:\n";
    for (const auto& pair : topWords) {
        std::cout << pair.first << ": " << pair.second << " times\n";
    }
}
