#include "IOFile.h"


std::string readFileReturnString(const std::string& filename) {
	std::ifstream file(filename);
	if (!file) {
		throw std::runtime_error("Could not open the file!");
	}
	std::stringstream buffer;
	buffer << file.rdbuf();
	return buffer.str();
}