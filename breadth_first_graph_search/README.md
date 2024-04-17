# Breadth-First Search Implementation

This is a program to find the shortest path between two nodes in a graph. It also includes a program for generating graphs. To generate a graph, run the following commands.

```
g++ genGraphs.cpp -o gg
./gg [number of nodes] [number of edges] [output file name]
```

Now, to perform breadth-first search, run these commands.

```
g++ pathFinder.cpp -o pf
./pf [graph file name] [start node index] [destination code index]
```

Alternatively, you can choose to not include the start and destination index. In this case, the program will generate 25 random start and destination nodes and find the paths between them.