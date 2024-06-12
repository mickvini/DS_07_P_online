#pragma once
#include <vector>
#include <functional>
#include <iostream>


using MenuFunction = std::function<void(std::string& text)>;

bool showMenu(const std::vector<std::pair<std::string, MenuFunction>>& options, std::string& text);

// Вообще эти методы это просто мое баловство с менюшкой
// Стандартная менюшка это swith case, где мы вызываем нужные нам методы
// по крайней мере так я делал два года назад
// И они сразу выводят на консоль результаты, думаю это неправильно
// Метод должен вернуть результат который мы можем обрабатывать
// Так что сделаю 'обертки' для этих методов которые выводят на консоль резултаты

void firstOption(const std::string& text);
void secondOption(const std::string& text);
void thirdOption(const std::string& text);
void fourOption(const std::string& text);