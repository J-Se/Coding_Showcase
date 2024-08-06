#ifndef DICE_H
#define DICE_H
class Dice {
    private:
        int dice[5];
    public:
        int* GetDice();
        void RollDice(bool shouldRoll[]);
        void PrintDice();
        Dice();
};
#endif
