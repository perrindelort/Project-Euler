# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:19:42 2024

@author: Antoine
"""

import os
from heapy import pqueue
import numpy as np

from util.util import timing, format_number
from scripts.problem import Problem

class Node():
    def __init__(self,x,y,number,distance_from_initial_node = float('inf')):
        self.x = x
        self.y = y
        self.distance_from_initial_node = distance_from_initial_node
        self.number = number
        
    def set_distance(self,distance):
        self.distance_from_initial_node = distance
        
    def __lt__(self,o):
        return self.distance_from_initial_node < o.distance_from_initial_node
    
    def __hash__(self):
        return self.number
    
    def __eq__(self,o):
        if isinstance(o,self.__class__):
            return self.number == o.number
        else:
            return False
    
    def __ne__(self,o):
        return not self.__eq__(o)

def dijkstra(graph,initial_node, infinity_value):
    
    # Initialization
    distances = {}
    distances[initial_node] = 0
    
    predecessors = {}
    
    vertex_queue = pqueue()
        
    for vertex in graph.keys():
        if vertex != initial_node:
            distances[vertex] = infinity_value
            vertex.set_distance(infinity_value)
            predecessors[vertex] = None
        
        vertex_queue.push((vertex, distances[vertex]))   
        
    while vertex_queue:
        u,d = vertex_queue.pop()
        distances[u] = d
        for v in graph[u]:
            alt = distances[u] + graph[u][v]
            if alt < distances[v]:
                distances[v] = alt
                v.set_distance(alt)
                predecessors[v] = u
                vertex_queue[v] = alt
    
    return distances,predecessors

class Problem83(Problem):
    def __init__(self, path = os.path.realpath(__file__), **kwargs):
        super().__init__(path)
        
        self.answer, self.time_taken = self.solve()
        
        self.detailed_answer = f"The minimal path sum from the top left to the bottom right by only moving up, down, left and right in the given matrix is {format_number(self.answer)}"
            
    
    @timing
    def solve(self, **kwargs):
        matrix = self.load_data_from_txt(use_numpy = True)
        x_max, y_max = np.shape(matrix)
        x_min, y_min = 0, 0
        infinity_value = np.max(matrix)*np.shape(matrix)[0]*np.shape(matrix)[1]
        
        nodes = []
        for x in range(x_max):
            nodes.append([])
            for y in range(y_max):
                nodes[x].append([])
                
        for x in range(x_max):
            for y in range(y_max):
                nodes[x][y] = Node(x=x,y=y,number = x_max*x+y)
        
        initial_nodes = [nodes[x][0] for x in range(x_max)]
        
        graph = {}
        for x in range(x_max):
            for y in range(y_max):
                node = nodes[x][y]
                graph[node] = {}
                if x == x_max-1 and y == y_max-1:
                    continue
                if x_min < x < x_max-1:
                    bottom_node = nodes[x+1][y]
                    top_node = nodes[x-1][y]
                    graph[node][bottom_node] = matrix[x+1][y]
                    graph[node][top_node] = matrix[x-1][y]
                elif x == x_min:
                    bottom_node = nodes[x+1][y]
                    graph[node][bottom_node] = matrix[x+1][y]
                elif x == x_max-1:
                    top_node = nodes[x-1][y]
                    graph[node][top_node] = matrix[x-1][y]
                if y_min < y < y_max-1:
                    right_node = nodes[x][y+1]
                    left_node = nodes[x][y-1]
                    graph[node][right_node] = matrix[x][y+1] 
                    graph[node][left_node] = matrix[x][y-1]
                elif y == y_min:
                    right_node = nodes[x][y+1]
                    graph[node][right_node] = matrix[x][y+1]
                elif y == y_max:
                    left_node = nodes[x][y-1]
                    graph[node][left_node] = matrix[x][y-1]

        end_node = nodes[x_max-1][y_max-1]
        initial_node = nodes[0][0]
        
        distances_dijkstra,predecessors = dijkstra(graph,initial_node,infinity_value)
        
        return int(distances_dijkstra[end_node] + matrix[0][0])


if __name__ == '__main__':
    problem = Problem83()
    problem.print_problem()