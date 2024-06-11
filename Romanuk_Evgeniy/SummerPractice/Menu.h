#pragma once
#include <vector>
#include <functional>
#include <string>
#include <iostream>


using MenuFunction = std::function<void(std::string& text)>;

bool showMenu(const std::vector<std::pair<std::string, MenuFunction>>& options, std::string& text);
