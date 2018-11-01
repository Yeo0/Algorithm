#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 23:57:23 2018

@author: yeoyoung
"""

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            print("set(visited)=,",set(visited))
            stack += graph[n] - set(visited)
            print("stack=",stack)
            print("visited=",visited)
    return visited

dfs(graph,'A')

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
            print("queue=",queue)
            print("visited=",visited)
    return visited

bfs(graph,'A')
