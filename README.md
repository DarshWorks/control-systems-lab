# Control Systems Lab 🚀

## 📌 Overview

This project is a simulation-based **control systems lab** demonstrating the behavior of:

* Proportional (P) controller
* Proportional–Integral (PI) controller
* Proportional–Integral–Derivative (PID) controller

The system models a **1D position control problem**, where an object must reach a target position.

---

## 🎯 Objective

To compare how different controllers affect:

* Overshoot
* Steady-state error
* Settling time
* Stability

---

## ⚙️ Controllers Implemented

### 🔹 P Controller

* Output depends only on current error
* Simple but causes oscillations

---

### 🔹 PI Controller

* Eliminates steady-state error
* Can increase overshoot

---

### 🔹 PID Controller

* Combines all three terms
* Provides fast, stable, and accurate response

---

## 📊 Key Concepts Explained

### 🔴 Overshoot

When the system exceeds the target value before settling.

👉 Caused by:

* high proportional gain
* system momentum

---

### 🎯 Steady-State Error

The difference between the final value and the setpoint.

👉 P controller → may have error
👉 PI/PID → eliminate this

---

### ⏱️ Settling Time

Time taken for the system to stabilize near the setpoint.

👉 Good systems:

* settle quickly
* don’t oscillate

---

## 📈 Results

The comparison shows:

* P → oscillatory and inaccurate
* PI → eliminates steady-state error but may overshoot
* PID → best overall performance

---

## ▶️ How to Run

```bash
pip install numpy matplotlib
python main.py
```

Output:

```
output.png
```

---

## 📷 Output

![Control Comparison](output.png)

---

## 🔧 Adjustable Parameters

You can modify:

```python
Kp = 0.8
Ki = 0.2
Kd = 0.5
```

👉 Try different values to observe behavior changes.

---

## 🚀 Future Improvements

* Interactive tuning sliders
* Realistic motor model
* Disturbance & noise simulation
* Hardware implementation

---

## 👨‍💻 Author

Built as a learning project in **control systems, robotics, and simulation**.
