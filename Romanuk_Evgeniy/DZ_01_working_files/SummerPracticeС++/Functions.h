#pragma once
#include <set>
#include <string>
#include <tuple>
#include <vector>
#include <map>


std::set<std::string> getUniqueWords(const std::string& text);
std::tuple<int, int> countVowelsAndConsonants(const std::string& text);
std::tuple<int, int> getCountAndLenghtOfSentences(const std::string& text);
std::map<std::string, int> getNumberOfUsesOfEachWordWithSimilliarCriterion(const std::string& text);
std::vector<std::pair<std::string, int>> getTenMostFrequentlyEncounteredWords(const std::string& text);