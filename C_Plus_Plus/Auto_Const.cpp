#include <iostream>

int main()
{
	auto strength = 80;
	auto accuracy = 45.5;
	auto dexterity = 24.0;

	const auto MAXIMUM = 50;

	auto attack = strength * (accuracy / MAXIMUM);
	auto damage = strength * (dexterity / MAXIMUM);

	std::cout << "Attack Raeting: " << attack << "\n";
	std::cout << "Damage Rating: " << damage << "\n"

	return 0;
}