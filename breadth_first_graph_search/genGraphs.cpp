#include <string>
#include <vector>
#include <fstream>
#include <random>
#include <ctime>
using namespace std;

bool contains(vector<int> vect, int key);

int main(int argc, char** argv) {
    int numNodes, numEdges;
    ofstream output;

    if (argc != 4) {
        return 1;
    }

    try {
        numNodes = stoi(argv[1]);
        numEdges = stoi(argv[2]);
    } catch (int exceptionNum) {
        return 1;
    }

    output.open(argv[3]);

    vector<vector<int>> adjLists(numNodes);

    srand(time(0));

    for (int i = 0; i < numEdges; i++) {
        int myEdgeSource;
        do {
            myEdgeSource = rand() % numNodes;
        } while (adjLists.at(myEdgeSource).size() >= (numNodes - 1)); // making sure the node doesn't already have a full adjacency list

        int myEdgeDest;
        do {
            myEdgeDest = rand() % numNodes;
        } while (contains(adjLists.at(myEdgeSource), myEdgeDest) || myEdgeDest == myEdgeSource); // making sure the edge doesn't already exist, and doesn't go from the node to itself
        adjLists.at(myEdgeSource).push_back(myEdgeDest);
    }

    for (int i = 0; i < numNodes; i++) {
        output << i << ": ";
        for (int j = 0; j < adjLists.at(i).size(); j++) {
            output << adjLists.at(i).at(j) << " ";
        }
        output << endl;
    }
}

bool contains(vector<int> vect, int key) {
    for (int elem : vect) {
        if (elem == key) {
            return true;
        }
    }
    return false;
}