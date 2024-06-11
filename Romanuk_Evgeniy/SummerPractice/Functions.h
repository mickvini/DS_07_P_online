#pragma once
#include <iostream>
#include <set>
#include <sstream>
#include <ctime>
#include <fstream>

std::set<std::string> getUniqueWords(std::string& text);
void countVowelsAndConsonants(std::string& text);
std::string readFile(const std::string& filename);
