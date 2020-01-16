#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:59:18 2019

@author: marjan
Question: Given the adjacency matrix of an undirected graph with no loops or multiple edges,
find the size of the connected component of vertex 1 (0-based).
"""

def bfsComponentSize(matrix):
    """
    Pseudocode: 
    input: adjacency matrix (a list of lists) contains True and False determine edges between vertexes
    output: size of the connected component of vertex 1 (start node is vertex 1)
    data structure: matrix/ double dimension array
    algorithm: Breadth-first search (BFS)

    1. Go through the matrix to find all pair of vertexes with corresponding 1 or zero, make a list of tuples, e.g. [(0,1,1), ..]
    2. Apply BFS data structure as follow:
        a) Define the starting node as vertex 1
        b) Define queue, neighbours, and explored lists
        c) Check the starting node and add its neighbours to the queue
        d) Mark the starting node as explored
        e) Get the next first node from the queue (FIFO)
        f) Check if it is explored if not add its neighbours to the queue and mark it as explored
        g) Repeat e and f until the queue is empty
    ref:https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
    """
    
    matrix_tpls = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix_tpls.append((i, j, 1 if matrix[i][j] == True else 0))
            
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    start_vertex = 1
    queue = [start_vertex]
    # keep track of neighbours
    neighbours = []
    # keep looping until there are nodes still to be checked
    while queue: ## while queue is not empty, this loop will be run
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            for x in matrix_tpls:
                if (x[0] == node) and (x[2] == 1):
                    neighbours.append(x[1])
            # add neighbours of node to queue
            if neighbours:
                for neighbour in neighbours:
                    queue.append(neighbour)
              
        return len(explored)

            
matrix = [[False,True,False], [True,False,False], [False,False,False]]         
print(bfsComponentSize(matrix))