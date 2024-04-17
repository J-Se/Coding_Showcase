#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <chrono>
using namespace std;

vector<int> dynamicChange(int n, int k, vector<int> d);

const int INF = 1000000; // this should work for the scale of numbers we are using

enum Arrows {
    up,
    left
};

int main(int argc, char** argv) {
    int n, k;
    vector<int> d;
    vector<int> coinsUsed;

    if (argc < 4) {
        cout << "Error: incorrect number of arguments" << endl;
        return 1;
    }

    for (int i = 1; i < argc; i++) {
        for (int j = 0; j < strlen(argv[i]); j++) {
            if (!isdigit(argv[i][j])) {
                cout << "Error: all arguments must be positive integers" << endl;
                return 1;
            }
        }
    }

    n = stoi(argv[1]);
    k = stoi(argv[2]);

    if (k != (argc - 3)) {
        cout << "Error: incorrect number of denominations" << endl;
        return 1;
    }

    for (int i = 3; i < argc; i++) {
        d.push_back(stoi(argv[i]));
    }
    
    chrono::steady_clock::time_point start = chrono::steady_clock::now();
    coinsUsed = dynamicChange(n, k, d);
    chrono::steady_clock::time_point end = chrono::steady_clock::now();

    cout << "coins used: ";
    for (int coin : coinsUsed) {
        cout << coin << " ";
    }
    cout << endl;
    cout << chrono::duration_cast<chrono::microseconds>(end - start).count() << " microseconds elapsed" << endl;
}

vector<int> dynamicChange(int n, int k, vector<int> d) {
    vector<vector<int>> c(n + 1, vector<int>(k + 1)); // int c[n + 1][k + 1];
    vector<vector<Arrows>> a(n + 1, vector<Arrows>(k + 1)); // Arrows a[n + 1][k + 1];
    vector<int> outputs;
    int currN, currK;

    for (currN = 1; currN <= n; currN++) { // when n > 0 and k == 0, there is no possible solution
        c.at(currN).at(0) = INF;
    }

    for (currK = 0; currK <= k; currK++) { // when n == 0, we need zero coins
        c.at(0).at(currK) = 0;
    }

    for (currN = 1; currN <= n; currN++) {
        for (currK = 1; currK <= k; currK++) {
            int doNotUseCoin = c.at(currN).at(currK - 1); // how many coins we will use if we don't use the current coin
            if (currN < d.at(currK - 1)) {
                c.at(currN).at(currK) = doNotUseCoin;
                a.at(currN).at(currK) = Arrows::left;
            } else {
                int doUseCoin = 1 + c.at(currN - d.at(currK - 1)).at(currK); // how many coins we will use if we do use the current coin
                if (doUseCoin <= doNotUseCoin) {
                    c.at(currN).at(currK) = doUseCoin;
                    a.at(currN).at(currK) = Arrows::up;
                } else {
                    c.at(currN).at(currK) = doNotUseCoin;
                    a.at(currN).at(currK) = Arrows::left;
                }
            }
        }
    }

    currN = n;
    currK = k;
    
    while (currN > 0 && currK > 0) {
        if (a.at(currN).at(currK) == Arrows::up) {
            outputs.push_back(d.at(currK - 1));
            currN -= d.at(currK - 1);
        } else {
            currK--;
        }
    }

    return outputs;
}