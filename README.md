# Linear-algebra-cheatsheet
# MatrixOps CheatSheet

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/numpy-1.24%2B-4D77CF.svg)](https://numpy.org/)

An interactive command-line cheat sheet for linear algebra fundamentals, implemented using NumPy and Matplotlib. This project is designed to reinforce the mathematical foundation of Machine Learning and demonstrate Python engineering skills.

## Features
- CLI-based interface with a clear menu for topic selection and plot generation
- Vectors & Matrices: addition, multiplication, transposition, norms
- Spectral Analysis: eigenvalues and eigenvectors with validation checks
- Visualization: automatic plot saving to the `assets/` directory
- Documentation: every function includes a docstring with formulas and explanations
- Clean Architecture: separation of logic, visualization, and interface

## Tech Stack
- Python 3.8+
- NumPy - vector and matrix computations
- Matplotlib - plot generation
- venv / pip - environment isolation

## Installation & Usage
bash
# 1. Clone the repository
git clone https://github.com/theaecktann/matrix-ops-cheatsheet.git
cd matrix-ops-cheatsheet

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS

# 3. Run the application
python main.py
