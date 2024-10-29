# Graph-Based Arrow Maze Traversal
## Project Overview
This project is a Python solution for traversing an arrow-based maze. The goal is to navigate from the starting cell at the top left of the grid to the bullseye located in the bottom right corner, following specific movement rules based on the colors and directions of arrows. The program finds a valid path and outputs the series of moves required to reach the bullseye.

## Problem Description
The maze consists of cells with arrows, either red (R) or blue (B), each pointing in a specific direction:
** Directions ** : North (N), East (E), South (S), West (W), Northeast (NE), Southeast (SE), Southwest (SW), or Northwest (NW).
** Movement rules ** : Starting from the top left corner, the program alternates between red and blue arrows, following each arrow's direction until it reaches the bullseye at the bottom right corner.

## Solution Details
The algorithm uses a depth-first search (DFS) approach with backtracking:
- Visited List (vstd): Keeps track of already visited cells to prevent infinite loops.
- Path List (path): Records the current path and its directions.
- Direction Dictionary (dir): Maps each direction to corresponding coordinate changes.
- Output Path: When the bullseye is reached, the program formats the path and writes it to an output file.
## Files
- Project2.py: Main script that contains the find_path function and initiates the program.
  
## Input and Output

### Input Format
The program takes an input file structured as follows:
The first line contains two integers representing the maze's row (r) and column (c) dimensions.
Subsequent lines contain cells representing the color (R or B) and the direction of the arrow.
Example Input File (input.txt):
3 3
R E B N R S
B SE R W O
R SW B NW B

### Output Format
The output file will contain a single line detailing the moves to reach the bullseye. Each move is represented by a number (step count) and a direction (e.g., 3E 2SW).

Example Output File (output.txt):
3E 2SW 1SE

input.txt: The input file with the maze details.
output.txt: The output file where the program writes the path.

## Code Explanation

### Key Functions
- find_path: Recursively finds a path from the starting cell to the bullseye, adhering to the color and direction constraints.
- output_path: Formats and writes the final path to the output file once the bullseye is reached.
  
### Program Flow
The program reads the input maze and initializes the maze dimensions.
The find_path function is called with the starting position (0,0) and follows arrows according to color and direction, recursively navigating until it reaches the bullseye.
If a path is found, it writes the formatted path to output.txt.
