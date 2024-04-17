#include <fstream>
#include <vector>
#include <iostream>
#include <sstream>
#include <queue>
#include <climits>
#include <random>
#include <ctime>
#include <chrono>
using namespace std;

enum Color {
    white,
    gray,
    black
};

struct Node {
    int id;
    Color color;
    int distance;
    int parentID;
    vector<int> adjList;
};

vector<int> splitBySpaces(string str);
void BFS(vector<Node>& graph, int sourceID);
string GetPath(vector<Node>& graph, int sourceID, int destID);

const int INF = INT_MAX;

int main(int argc, char** argv) {
    ifstream fileInput;
    vector<Node> graph;
    string line;
    vector<int> tempVect;
    int pos, sourceID, destID;
    int currIndex = 0;
    vector<string> outputs = vector<string>();
    bool customPath = argc == 4; // whether or not we are searching for a specific path

    if (argc != 2 && argc != 4) {
        cout << "Error: incorrect number of arguments" << endl;
        return 1;
    }

    fileInput.open(argv[1]);
    if (!fileInput.is_open()) {
        cout << "Error: could not open input file" << endl;
        return 1;
    }

    if (customPath) {
        try {
            sourceID = stoi(argv[2]);
            destID = stoi(argv[3]);
        } catch (exception e) {
            cout << "Error: source and destination must be integers" << endl;
            return 1;
        }
    }

    while (getline(fileInput, line)) {
        Node myNode;
        myNode.id = currIndex;
        pos = line.find(':');
        line = line.substr(pos + 2);
        tempVect = splitBySpaces(line);
        myNode.adjList = tempVect;
        graph.push_back(myNode);
        currIndex++;
    }

    if (customPath && (sourceID < 0 || destID > graph.size() - 1)) {
        cout << "Error: invalid source and/or destination ID" << endl;
        return 1;
    }

    srand(time(0));

    chrono::high_resolution_clock::time_point start = chrono::high_resolution_clock::now();
    if (customPath) {
        BFS(graph, sourceID);
        outputs.push_back(GetPath(graph, sourceID, destID));
    } else {
        for (int i = 0; i < 25; i++) { // pick two random nodes, then find the shortest path between them
            sourceID = rand() % graph.size();
            do {
                destID = rand() % graph.size();
            } while (destID == sourceID);
            BFS(graph, sourceID);
            outputs.push_back(GetPath(graph, sourceID, destID));
        }
    }
    chrono::high_resolution_clock::time_point end = chrono::high_resolution_clock::now();

    for (string path : outputs) {
        cout << path << endl;
    }
    
    if (customPath) {
        cout << "Computation time: " << (chrono::duration_cast<chrono::microseconds>(end - start).count()) << " microseconds" << endl;
    } else {
        cout << "Average computation time: " << (chrono::duration_cast<chrono::microseconds>(end - start).count() / 25) << " microseconds" << endl;
    }
}

string GetPath(vector<Node>& graph, int sourceID, int destID) {
    string outputStr;
    Node* destNode = &graph.at(destID);
    if (sourceID == destID) {
        outputStr = to_string(sourceID) + " ";
        return outputStr;
    }
    if (destNode->parentID < 0) {
        outputStr = "No path exists from " + to_string(sourceID) + " to " + to_string(destID);
        return outputStr;
    }
    if (destNode->distance > 0) {
        outputStr = GetPath(graph, sourceID, destNode->parentID);
        outputStr += to_string(destNode->id) + " ";
        return outputStr;
    }
}

void BFS(vector<Node>& graph, int sourceID) {
    queue<int> nodeQueue = queue<int>();

    for (int i = 0; i < graph.size(); i++) {
        graph.at(i).color = Color::white;
        graph.at(i).distance = INF;
        graph.at(i).parentID = -1;
    }
    
    graph.at(sourceID).color = Color::gray;
    graph.at(sourceID).distance = 0;
    graph.at(sourceID).parentID = -1;

    nodeQueue.push(sourceID);

    while (!nodeQueue.empty()) {
        int currNodeID = nodeQueue.front();
        nodeQueue.pop();
        for (int currChildNodeID : graph.at(currNodeID).adjList) {
            if (graph.at(currChildNodeID).color == Color::white) {
                graph.at(currChildNodeID).color = Color::gray;
                graph.at(currChildNodeID).distance = graph.at(currNodeID).distance + 1;
                graph.at(currChildNodeID).parentID = graph.at(currNodeID).id;
                nodeQueue.push(currChildNodeID);
            }
        }
        graph.at(currNodeID).color = Color::black;
    }
}

vector<int> splitBySpaces(string str) {
    vector<int> returnVect = vector<int>();
    string tempStr = "";
    for (char c : str) {
        if (c != ' ') {
            tempStr += c;
        } else if (tempStr.size() > 0) {
            returnVect.push_back(stoi(tempStr));
            tempStr = "";
        }
    }
    return returnVect;
}