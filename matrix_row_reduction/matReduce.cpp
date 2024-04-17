// Matrix row reduction, might add more features if they seem useful
#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
using namespace std;

void PrintMat(vector<vector<double>> mat, int precision) {
    cout << fixed << right << setprecision(precision);
    for (vector<double> row : mat) {
        for (double num : row) {
            if (abs(num) <= 0.0001) { // purely aesthetic
                num = abs(num);
            }
            cout << setw(precision + 4) << num << " ";
        }
        cout << endl;
    }
    cout << endl;
}

vector<double> MultiplyRow(vector<double> row, double factor) {
    vector<double> returnRow = row;
    for (int i = 0; i < row.size(); i++) {
        returnRow.at(i) *= factor;
    }
    return returnRow;
}

vector<double> DivideRow(vector<double> row, double divisor) {
    vector<double> returnRow = row;
    for (int i = 0; i < row.size(); i++) {
        returnRow.at(i) /= divisor;
    }
    return returnRow;
}

void AddRows(vector<double>& row1, const vector<double>& row2) { // row1 += row2
    for (int i = 0; i < row1.size(); i++) {
        row1.at(i) += row2.at(i);
    }
}

void SwapRows(vector<vector<double>>& mat, int rowNum1, int rowNum2) {
    vector<double> tempRow = mat.at(rowNum1);
    mat.at(rowNum1) = mat.at(rowNum2);
    mat.at(rowNum2) = tempRow;
}

void MatReduce(vector<vector<double>>& mat) {
    int r = 0; // current row
    int c = 0; // current column
    int numRows = mat.size(); // not really necessary, but used for readability
    int numCols = mat.at(0).size();
    while (r < numRows && c < numCols) {
        if (abs(mat.at(r).at(c)) <= 0.0001) {
            bool pivotFound = false;
            for (int i = r + 1; i < numRows; i++) { // look for a row to swap with
                if (mat.at(i).at(c) != 0) {
                    SwapRows(mat, r, i);
                    pivotFound = true;
                    break;
                }
            }
            if (!pivotFound) { // no pivot can be found for this variable, increment column but not row (so the program doesn't run out of rows and end early)
                c++;
                continue;
            }
        }

        mat.at(r) = DivideRow(mat.at(r), mat.at(r).at(c)); // convert the pivot into a one
        for (int i = 0; i < numRows; i++) { // convert all numbers directly above and below the pivot into zeroes
            if (i != r) {
                AddRows(mat.at(i), MultiplyRow(mat.at(r), -1 * mat.at(i).at(c)));
            }
        }
        r++; // pivot was found for this row and column, so increment both
        c++;
    }
}

int main() {
    int numRows, numCols, precision;
    vector<vector<double>> mat;

    cout << "Enter number of rows: ";
    cin >> numRows;
    cout << "Enter number of columns: ";
    cin >> numCols;
    cout << "Enter numbers to populate the matrix (left to right, top to bottom):" << endl;
    for (int i = 0; i < numRows * numCols; i++) {
        int tempInt;
        cin >> tempInt;
        if (i % numCols == 0) {
            mat.push_back(vector<double>());
        }
        mat.at(i / numCols).push_back(tempInt);
    }

    cout << "Enter number of digits after decimal point: ";
    cin >> precision;
    cout << endl;

    PrintMat(mat, precision);
    MatReduce(mat);
    PrintMat(mat, precision);
}