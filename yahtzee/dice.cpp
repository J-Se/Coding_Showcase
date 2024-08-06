#include "dice.h"
#include <iostream>
#include <ctime>
using namespace std;

Dice::Dice() {
    srand(time(0));
    bool temp[5] = {true, true, true, true, true};
    RollDice(temp); // roll each die
}

int* Dice::GetDice() {
    return dice;
}

void Dice::RollDice(bool shouldRoll[]) { // shouldRoll describes which dice to reroll (true means the corresponding die gets rolled)
    for (int i = 0; i < 5; i++) {
        if (shouldRoll[i]) {
            dice[i] = rand() % 6 + 1;
        }
    }
}

void Dice::PrintDice() {
    cout << "Your dice: " << endl;
    for (int die : dice) {
        cout << die << " ";
    }
    cout << endl;
}