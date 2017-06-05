#include <iostream>

int main()
{
	int grade;
	std::cout << "Enter your grade (1 - 100): ";
	std::cin >> grade;

	if (grade >= 70)
	{	
		if (grade >=90)
		{
			std::cout << "\nYou got A, Great Job!\n";
			return 0;
		}
	    if (grade >=80)
		{
			std::cout << "\nYou got B, Good Job!\n";
			return 0;
		}
		std::cout << "\nYou got C, Fine work!\n";
	}
    else 
    {
    	std::cout << "\nYou got F, Sign Up Again!\n";
    }

	return 0;
}