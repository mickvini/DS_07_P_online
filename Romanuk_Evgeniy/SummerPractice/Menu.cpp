#include "Menu.h"


bool showMenu(const std::vector<std::pair<std::string, MenuFunction>>& options, std::string& text)
{
    int choice = 0;
    do {
        system("cls");
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