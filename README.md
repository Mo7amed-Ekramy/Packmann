# 🟡 Pac-Man AI Pathfinding Project

This project implements classical AI search algorithms to navigate a Pac-Man agent through a 2D grid environment. The goal is to find the optimal path from the starting position to the food while avoiding walls and ghost boundaries.

## 🚀 Features

* Grid-based environment representation
* Pathfinding using:

  * Breadth-First Search (BFS)
  * Depth-First Search (DFS)
  * Dijkstra’s Algorithm
* Obstacle handling (walls and ghosts)
* Path reconstruction using parent tracking
* Visualization of the solution using Matplotlib

## 🧠 Problem Description

The environment is modeled as a 2D grid where:

* `P` = Pac-Man (start position)
* `F` = Food (goal)
* `0` = Free cell
* `1` = Wall (blocked)
* `G` = Ghost (danger zone)

The agent can move in four directions:

* Up, Down, Left, Right

## 🎯 Objective

Find a valid (and optimal) path from `P` to `F` while avoiding invalid cells.

## ⚙️ Algorithms Used

### 🔹 Breadth-First Search (BFS)

* Guarantees the shortest path in terms of steps
* Explores nodes level by level

### 🔹 Depth-First Search (DFS)

* Explores deeply before backtracking
* Does not guarantee optimality

### 🔹 Dijkstra’s Algorithm

* Finds the shortest path based on cost
* Useful for weighted environments

## 📊 Visualization

The final path is visualized using Matplotlib, showing:

* Start and goal positions
* Obstacles and ghost zones
* The computed path

## 🧪 Example Output

* Path from start to goal
* Number of steps taken
* Visual grid representation

## 📌 Future Improvements

* Interactive GUI (Tkinter or Pygame)
* Animated pathfinding
* Dynamic obstacles
* Heuristic-based search (A*)

## 🛠️ Technologies Used

* Python
* Matplotlib
* Basic Data Structures (Queue, Set, Dictionary)

## 👨‍💻 Author

Mohamed Ekramy
Mahmoud Sayed
Mohamed ElMotaz
