#include <iostream>

int add(int x, int y)
{ 
    std::cout << "Running Calculator ...\n";
    return (x+y) ;
}

int main()
{
	/* code */
    std::cout << "What is 3 +5?\n";
	std::cout << "The sum is " << add(3, 5) << "\n";
	return 0;
}