#include "game.h"
#include "dice.cpp"
#include "scoreCard.cpp"
#include <iostream>
using namespace std;

bool isNum(string str) {
    for (char c : str) {
        if (!isdigit(c)) {
            return false;
        }
    }
    return true;
}

void Game::Start() {
    ScoreCard scoreCard = ScoreCard();
    Dice dice = Dice();
    bool ALL_TRUE[5] = { true, true, true, true, true }; // can't be a const because we need to send it as an argument
    bool diceToReroll[5];
    string tempStr;
    int index, score;
    ScoreCard::ScoreType currScoreType;

    for (int i = 0; i < Game::ROUND_COUNT; i++) {
        dice.RollDice(ALL_TRUE);
        dice.PrintDice();
        for (int j = 0; j < 2; j++) { // rerolling dice
            for (int k = 0; k < 5; k++) {
                while (true) {
                    cout << "Reroll die #" << (k + 1) << " (y/n)? ";
                    cin >> tempStr;
                    if (tempStr.length() != 1) {
                        cout << "Invalid input; try again." << endl;
                        continue;
                    }
                    else if (tempStr == "y" || tempStr == "Y") {
                        diceToReroll[k] = true;
                        break;
                    }
                    else if (tempStr == "n" || tempStr == "N") {
                        diceToReroll[k] = false;
                        break;
                    }
                    else {
                        cout << "Invalid input; try again." << endl;
                        continue;
                    }
                }
            }
            cout << endl;
            dice.RollDice(diceToReroll);
            dice.PrintDice();
        }

        cout << endl << "Your score card:" << endl;
        scoreCard.PrintScores();
        
        while (true) {
            cout << "Enter the index of the score you would like to apply (1 - 13): ";
            cin >> tempStr;
            if (!isNum(tempStr)) {
                cout << "Invalid input; try again." << endl;
                continue;
            }

            index = stoi(tempStr);
            if (index < 1 || index > 13) {
                cout << "Invalid input; try again." << endl;
                continue;
            }

            currScoreType = SCORE_TYPE_INDICES.at(index);
            if (scoreCard.GetScore(currScoreType) >= 0 && currScoreType != ScoreCard::ScoreType::yahtzee) { // the score has already been used and is not a yahtzee
                cout << "Score has already been used; try again." << endl;
                continue;
            }
            scoreCard.SetScore(currScoreType, dice.GetDice());
            cout << scoreCard.scoreNames.at(currScoreType) << " score set to " << scoreCard.GetScore(currScoreType) << "." << endl << endl;
            break;
        }
    }
    cout << endl << "Final score card:" << endl;
    scoreCard.PrintScores();
}