# Vehicle Routing Problem (VRP) - Pyomo Implementation

## Overview
This project implements a basic Vehicle Routing Problem (VRP) using Pyomo and CBC solver.
The goal is to minimize total travel distance for a single vehicle visiting multiple customers.

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Ensure CBC solver is installed (or modify the code to use Gurobi if available).

3. Run the model:

```bash
python model.py
```

The solution will be saved at `results/solution.txt`.

## Dataset
See `data/customers.csv` for example customer coordinates.
