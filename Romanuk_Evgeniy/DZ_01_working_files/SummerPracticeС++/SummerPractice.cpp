#include "Menu.h"
#include "IOFile.h"
//На текущий момент вообще вспоминаю плюсы, так как не программировал на них в течении ~двух лет
//Вполне возможно, что я тут всё переделаю несколько раз

//.gitignore сгенерил через https://www.toptal.com/developers/gitignore

//TODO: 1. Загрузить файл длиной не менее 2000 символов.
//TODO: 2. Составить программу, которая считает число уникальных слов в тексте(без критерия схожести).
//TODO: 3. Составить программу, которая считает число гласных и согласных букв.
//TODO: 4. Составить программу, которая считает число предложений, их длину и число(количество) раз использования каждого слова в тексте
//TODO: (с критерием схожести, критерий схожести слов выбрать самостоятельно, например, spacy(en_core_web_sm) или расстояние Левенштейна).
//TODO: 5. Вывести 10 наиболее часто встречаемых слов.



int main()
{

    std::string text = readFileReturnString("text.txt");

    std::vector<std::pair<std::string, MenuFunction>> menuOptions = {
        {"Get unique words", firstOption},
        {"Count Vowels and Consonants", secondOption},
        {"Get the number and total length of sentences, the frequency of each word in the text with a similarity criterion", thirdOption},        
        {"Get ten most frequently encountered words", fourOption}
    };

    if (showMenu(menuOptions, text))
        return 0;
    else return 1;
}


