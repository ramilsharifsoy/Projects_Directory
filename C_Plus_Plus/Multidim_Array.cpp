#include <iostream>
#include <string.h>

int main()
{
	int box[5][3] = {8, 6, 7, 5, 3, 0, 9, 2, 1, 7, 8, 9, 0, 5, 2};

	for (int i = 0; i < 5; i++)
	{
		for (int j=0; j < 3; j++)
		{
			std::cout << "box[" << i << "]";
			std::cout << "[" << j << "] = ";
			std::cout << box[i][j] << "\n";
		}
	}
	return 0;
}