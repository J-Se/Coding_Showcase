#ifndef SCORE_CARD_H
#define SCORE_CARD_H
#include <map>
#include <string>
using namespace std;

class ScoreCard {
	public:
		enum ScoreType {
			aces,
			twos,
			threes,
			fours,
			fives,
			sixes,
			threeOfAKind,
			fourOfAKind,
			fullHouse,
			smallStraight,
			largeStraight,
			yahtzee,
			chance
		};
		const map<ScoreType, string> scoreNames {
			{ScoreType::aces, "Aces"},
			{ScoreType::twos, "Twos"},
			{ScoreType::threes, "Threes"},
			{ScoreType::fours, "Fours"},
			{ScoreType::fives, "Fives"},
			{ScoreType::sixes, "Sixes"},
			{ScoreType::threeOfAKind, "Three of a kind"},
			{ScoreType::fourOfAKind, "Four of a kind"},
			{ScoreType::fullHouse, "Full house"},
			{ScoreType::smallStraight, "Small straight"},
			{ScoreType::largeStraight, "Large straight"},
			{ScoreType::yahtzee, "Yahtzee"},
			{ScoreType::chance, "Chance"}
		};
		int GetScore(ScoreType type);
		void PrintScores();
		void SetScore(ScoreType type, int dice[]);
		ScoreCard();
	private:
		map<ScoreType, int> currScoreValues;
		void CountRolls(int dice[], int arrayToChange[]);
};
#endif