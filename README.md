# Theory of Languages and Automata - Practical Project

A comprehensive practical project exploring the theory of computation through implementation of Turing machines and cellular automata.

## Project Overview

This project is part of the Theory of Languages and Automata (TLA) course at Iran University of Science and Technology (IUST), taught by Dr. Reza Entezari-Maleki . The project was co-designed with Taha Biklariyan (https://github.com/Tahabik).

The project consists of two main parts that explore fundamental concepts in theoretical computer science:

1. **Part 1: Turing Machines** - Implementation of a complete Turing machine simulator with applications to mathematical computations.

2. **Part 2: Cellular Automata and Universal Computation** - Implementation of two famous cellular automata (Conway's Game of Life and Langton's Ant) and proof of Turing completeness through digital logic gates.

## Course Information

- **University**: Iran University of Science and Technology (IUST)
- **Course**: Theory of Languages and Automata (TLA4042)
- **Instructor**: Dr. Reza Entezari-Maleki
- **Semester**: 4042
- **Designers**: Milad Zarei Maleki, Taha Biklariyan


## Key Concepts

### Part 1: Turing Machines

A **Turing Machine** is a mathematical model of computation that represents the simplest form of a computer. Key components include:

- **Finite state machine**: A set of states determining machine behavior
- **Tape**: An infinite or semi-infinite memory where symbols are read and written
- **Head**: A pointer that reads/writes symbols on the tape
- **Transition rules**: Rules that determine state changes based on current state and symbol

In this part, we implemented:

- A complete Turing machine simulator with support for infinite bidirectional tape
- Mathematical computations: addition and multiplication using unary representation

### Part 2: Cellular Automata

**Cellular Automata** are discrete computational models consisting of a grid of cells, each with a finite set of states. The next state of each cell depends only on its current state and neighboring cells.

#### Conway's Game of Life

A two-dimensional cellular automaton with four simple rules:

1. **Underpopulation**: A live cell with fewer than 2 live neighbors dies
2. **Survival**: A live cell with 2 or 3 live neighbors survives
3. **Overpopulation**: A live cell with more than 3 live neighbors dies
4. **Reproduction**: A dead cell with exactly 3 live neighbors becomes alive

Despite simple rules, it exhibits remarkable emergent behavior including Turing completeness.

#### Langton's Ant

A simple two-dimensional computational model representing a 2D Turing machine with chaotic and fascinating emergent behavior. The ant operates on a grid following simple rules based on cell colors and produces complex patterns.

#### Turing Completeness

The project demonstrates that both cellular automata are Turing complete by constructing digital logic gates (AND, NOT) using gliders in Conway's Game of Life. This proves that any computable function can be implemented in these systems.


## Technical Stack

- **Language**: Python 3
- **Visualization**: Pygame (for graphical simulations)
- **Scientific Computing**: NumPy, SciPy (for optimized cellular automata computation)
- **File Formats**: RLE (Run Length Encoded) and Plaintext for Game of Life patterns
