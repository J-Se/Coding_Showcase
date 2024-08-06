#ifndef GAME_H
#define GAME_H
#include "scoreCard.h"
#include <map>
class Game {
    public:
        void Start();
    private:
        const int ROUND_COUNT = 13;
        const map<int, ScoreCard::ScoreType> SCORE_TYPE_INDICES { // this is here to avoid repeating code elsewhere
            {1, ScoreCard::ScoreType::aces},
            {2, ScoreCard::ScoreType::twos},
            {3, ScoreCard::ScoreType::threes},
            {4, ScoreCard::ScoreType::fours},
            {5, ScoreCard::ScoreType::fives},
            {6, ScoreCard::ScoreType::sixes},
            {7, ScoreCard::ScoreType::threeOfAKind},
            {8, ScoreCard::ScoreType::fourOfAKind},
            {9, ScoreCard::ScoreType::fullHouse},
            {10, ScoreCard::ScoreType::smallStraight},
            {11, ScoreCard::ScoreType::largeStraight},
            {12, ScoreCard::ScoreType::yahtzee},
            {13, ScoreCard::ScoreType::chance}
        };
};
#endif