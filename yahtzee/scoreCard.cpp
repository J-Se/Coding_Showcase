#include "scoreCard.h"
#include <iostream>

ScoreCard::ScoreCard() {
	for (const auto& pair : scoreNames) { // convenient to iterate over this
		currScoreValues[pair.first] = -1;
	}
}

int ScoreCard::GetScore(ScoreCard::ScoreType type) {
	return ScoreCard::currScoreValues[type];
}

void ScoreCard::PrintScores() {
	int currIndex = 1;
	int totalScore = 0;

	for (const auto& pair : scoreNames) { // iterates over all key-value pairs in scoreNames
		cout << currIndex << ". ";
		cout << pair.second << ": [";
		if (currScoreValues[pair.first] < 0) {
			cout << " ";
		}
		else {
			cout << currScoreValues[pair.first];
			totalScore += currScoreValues[pair.first];
		}
		cout << "]" << endl;
		currIndex++;
	}

	cout << endl << "Total score: " << totalScore << endl << endl;
}

void ScoreCard::SetScore(ScoreType type, int dice[]) {
	int scoreAmount = 0;
	int amounts[6];
	bool conditionsMet; // used for most of the lower section scores

	switch (type) {
		case aces:
			for (int i = 0; i < 5; i++) {
				if (dice[i] == 1) {
					scoreAmount += 1;
				}
			}
			break;

		case twos:
			for (int i = 0; i < 5; i++) {
				if (dice[i] == 2) {
					scoreAmount += 2;
				}
			}
			break;

		case threes:
			for (int i = 0; i < 5; i++) {
				if (dice[i] == 3) {
					scoreAmount += 3;
				}
			}
			break;

		case fours:
			for (int i = 0; i < 5; i++) {
				if (dice[i] == 4) {
					scoreAmount += 4;
				}
			}
			break;

		case fives:
			for (int i = 0; i < 5; i++) {
				if (dice[i] == 5) {
					scoreAmount += 5;
				}
			}
			break;

		case sixes:
			for (int i = 0; i < 5; i++) {
				if (dice[i] == 6) {
					scoreAmount += 6;
				}
			}
			break;

		case threeOfAKind:
			conditionsMet = false;

			CountRolls(dice, amounts);

			for (int i = 0; i < 6; i++) {
				if (amounts[i] >= 3) {
					conditionsMet = true;
					break;
				}
			}

			if (conditionsMet) {
				for (int i = 0; i < 5; i++) {
					scoreAmount += dice[i];
				}
			}

			break;

		case fourOfAKind:
			conditionsMet = false;

			CountRolls(dice, amounts);

			for (int i = 0; i < 6; i++) {
				if (amounts[i] >= 4) {
					conditionsMet = true;
					break;
				}
			}

			if (conditionsMet) {
				for (int i = 0; i < 5; i++) {
					scoreAmount += dice[i];
				}
			}

			break;

		case fullHouse:
			conditionsMet = true; // this calculation is easier if we disprove a full house, rather than proving it

			CountRolls(dice, amounts);

			for (int i = 0; i < 6; i++) {
				if (amounts[i] != 0 && amounts[i] != 2 && amounts[i] != 3) {
					conditionsMet = false;
				}
			}

			if (conditionsMet) {
				scoreAmount = 25;
			}

			break;

		case smallStraight:
			conditionsMet = true;

			CountRolls(dice, amounts);

			if (amounts[2] == 0 || amounts[3] == 0) { // if they didn't roll both 3 and 4
				conditionsMet = false;
			} else if ((amounts[0] == 0 || amounts[1] == 0) && (amounts[1] == 0 || amounts[4] == 0) && (amounts[4] == 0 || amounts[5] == 0)) { // if they didn't roll (1 and 2), (2 and 5), or (5 and 6)
				conditionsMet = false;
			}

			if (conditionsMet) {
				scoreAmount = 30;
			}
			
			break;

		case largeStraight:
			conditionsMet = true;

			CountRolls(dice, amounts);

			if (amounts[1] == 0 || amounts[2] == 0 || amounts[3] == 0 || amounts[4] == 0) { // if they didn't roll a 2, 3, 4, AND 5
				conditionsMet = false;
			}
			else if (amounts[0] == 0 && amounts[5] == 0) { // if they didn't roll a 1 OR 6
				conditionsMet = false;
			}

			if (conditionsMet) {
				scoreAmount = 40;
			}

			break;

		case yahtzee:
			conditionsMet = true;

			CountRolls(dice, amounts);

			for (int i = 0; i < 6; i++) {
				if (amounts[i] != 0 && amounts[i] != 5) {
					conditionsMet = false;
				}
			}

			if (conditionsMet) {
				if (currScoreValues[yahtzee] > 0) { // if a yahtzee has already been scored, the rest of the yahtzees are 100 points
					scoreAmount = currScoreValues[yahtzee] + 100;
				}
				else {
					scoreAmount = 50;
				}
			} else {
				if (currScoreValues[yahtzee] < 0) {
					scoreAmount = 0;
				} else {
					scoreAmount = currScoreValues[yahtzee];
				}
			}
			break;

		case chance:
			for (int i = 0; i < 5; i++) {
				scoreAmount += dice[i];
			}
			break;
		}

	currScoreValues[type] = scoreAmount;
}

// converts the dice array into a different format which shows the number of recurrences of each die type
// e.g. [2, 3, 6, 4, 3] returns [0, 1, 2, 1, 0, 1] because there are zero 1's, one 2, two 3's, one 4, zero 5's and one 6
void ScoreCard::CountRolls(int dice[], int arrayToChange[]) {
	int returnArray[6] = { 0, 0, 0, 0, 0, 0 };
	for (int i = 0; i < 5; i++) {
		returnArray[dice[i] - 1] = returnArray[dice[i] - 1] + 1;
	}
	for (int i = 0; i < 6; i++) {
		arrayToChange[i] = returnArray[i];
	}
}