# 🚚 Vehicle Routing Problem (VRP) - Optimization with Pyomo and CBC

## 📍 About the Project

This repository contains a mathematical optimization model for solving the **Vehicle Routing Problem (VRP)** using **Pyomo** in Python and the **CBC Solver**.

The objective is to minimize the total distance traveled by a vehicle that starts and ends at a depot while visiting all customers exactly once. Additionally, a **Miller-Tucker-Zemlin (MTZ)** formulation is implemented to eliminate subtours.

---

## 🎯 Problem Overview

- **Type:** Single Vehicle Routing Problem (VRP)
- **Objective:** Minimize total travel distance
- **Constraints:**
  - Each customer is visited exactly once
  - The vehicle starts and ends at the depot
  - No subtours (via MTZ constraints)

This type of problem is fundamental in **logistics**, **supply chain management**, and **transportation planning**, making it highly relevant for real-world decision-making environments like those handled by **Kpler**.

---

## 🗃️ Project Structure

```
vrp-pyomo/
├── data/
│   └── customers.csv          # Coordinates for depot and customers
├── results/
│   └── solution.txt           # Model output (optimized route)
├── model.py               # Main Pyomo optimization model
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## 📌 Dataset Example (`data/customers.csv`)

The dataset contains XY coordinates for the depot and each customer:

```
x,y
0,0
2,3
5,2
6,6
8,3
3,7
```

- **Node 0:** Depot  
- **Nodes 1-5:** Customers

---

## ⚙️ How to Run the Model

### 1. Install Python Dependencies:

```bash
pip install -r requirements.txt
```

---

### 2. Install CBC Solver:

- **Windows:**  
Download from [CoinOR CBC Releases](https://github.com/coin-or/Cbc/releases), extract, and add the binary folder to your system PATH.

- **Linux (Debian/Ubuntu):**
```bash
sudo apt install coinor-cbc
```

- **MacOS (Homebrew):**
```bash
brew install cbc
```

> ✅ Alternatively, if you have **Gurobi**, you can modify the solver in the script to use it.

---

### 3. Run the Optimization:

```bash
python vrp_model.py
```

The solution will be saved in:

```
results/solution.txt
```

Example Output:

```
0 -> 1
1 -> 2
2 -> 4
4 -> 3
3 -> 5
5 -> 0
```

---

## 🛑 Subtour Elimination - MTZ Formulation

To prevent subtours, the model uses the **MTZ (Miller-Tucker-Zemlin) constraints**, introducing ordering variables (`u[i]`) for each customer:

```
u[i] - u[j] + n * x[i, j] <= n - 1   ∀ i ≠ j, i,j ∈ Customers
```

This ensures a single connected tour visiting all nodes.

---

## 📈 Optional Visualization (Customer Locations):

You can visualize customer positions using `matplotlib`:

```python
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data/customers.csv')
plt.scatter(data['x'], data['y'], color='blue')
plt.scatter(data.iloc[0]['x'], data.iloc[0]['y'], color='red', label='Depot')
plt.title('Customer Locations')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
```

---

## 💡 Possible Future Extensions

- Multiple Vehicles (Multi-VRP)
- Vehicle capacity constraints (CVRP)
- Time windows for delivery (VRPTW)
- Dynamic data loading
- Interactive visualization with NetworkX or Plotly

---

## 👤 About Me

**Cristian Fortuna**  
Researcher passionate about **mathematical modeling**, **optimization algorithms**, and **decision support systems**.

[My LinkedIn Profile](https://www.linkedin.com/in/cristianfortunareis/)

---

## 📬 Contact

Feel free to reach out if you want to discuss optimization, logistics problems, or mathematical modeling!
