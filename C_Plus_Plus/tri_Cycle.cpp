#include <iostream>
// #include <string.h>
// #include <stdio.h>

class Tricycle
{
public:
	int getSpeed();
	void setSpeed(int speed);
	void pedal();
	void brake();
private:
	int speed;
};

// get speed from user
int Tricycle::getSpeed()
{
	return speed;
}

//set trike`s speed
void Tricycle::setSpeed(int newSpeed)
{
	if (newSpeed >= 0)
	{
		speed = newSpeed;
	}
}

//pedal the trike

void Tricycle::pedal()
{
	setSpeed(speed + 1);
	std::cout << "\nPedaling; tricyle speed " << speed << " mph\n";
}

//apply the brake
void Tricycle::brake()
{
	setSpeed(speed - 1);
	std::cout << "\nBraking; tricycle speed " << speed << " mph\n";
}

//create a trike and ride it
int main()
{
	Tricycle wichita;
	wichita.setSpeed(0);
	wichita.pedal();
	wichita.pedal();
	wichita.pedal();
	wichita.pedal();
	wichita.brake();
	wichita.brake();
	wichita.brake();
	wichita.brake();
	wichita.brake();
	return 0;
}