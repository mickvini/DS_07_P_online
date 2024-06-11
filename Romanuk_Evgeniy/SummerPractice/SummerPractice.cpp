#include "Menu.h"
#include "Functions.h"

//На текущий момент вообще вспоминаю плюсы, так как не программировал на них в течении ~двух лет
//Вполне возможно, что я тут всё переделаю несколько раз

//.gitignore сгенерил через https://www.toptal.com/developers/gitignore

//TODO: Загрузить файл длиной не менее 2000 символов.
//TODO: Составить программу, которая считает число уникальных слов в тексте(без критерия схожести).
//TODO: Составить программу, которая считает число гласных и согласных букв.
//TODO: Составить программу, которая считает число предложений, их длину и число(количество) раз использования каждого слова в тексте
//TODO: (с критерием схожести, критерий схожести слов выбрать самостоятельно, например, spacy(en_core_web_sm) или расстояние Левенштейна).
//TODO: Вывести 10 наиболее часто встречаемых слов.



int main()
{

    std::string text = readFile("text.txt");

    std::vector<std::pair<std::string, MenuFunction>> menuOptions = {
        {"Get unique words", getUniqueWords},  
        {"Count Vowels and Consonants", countVowelsAndConsonants}
    };

    if (showMenu(menuOptions, text))
        return 0;
    else return 1;

}
