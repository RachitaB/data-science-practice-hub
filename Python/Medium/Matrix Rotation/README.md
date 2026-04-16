# 🐍 Matrix Rotation Match Checker

## 📌 Problem Statement
Given two **n × n binary matrices** `mat` and `target`, determine whether it is possible to make **mat equal to target** by rotating `mat` in **90-degree increments**.

### Allowed Rotations
- **90° clockwise**
- **180°**
- **270°**
- **360° / No rotation**

Return:

- **True** → If `mat` can match `target` after some rotation  
- **False** → Otherwise  

---

## 🧾 Example 1

### Input
```python
mat = [
    [1,0,1],
    [0,0,1],
    [1,0,1]
]

target = [
    [1,0,1],
    [1,0,0],
    [1,0,1]
]
```

### Output
```python
True
```

### Explanation
By rotating **mat 180°**, it becomes equal to **target**.

---

## 🧾 Example 2

### Input
```python
mat = [
    [0,1],
    [1,0]
]

target = [
    [1,1],
    [0,0]
]
```

### Output
```python
False
```

### Explanation
No rotation of **mat** matches **target**.

---

## 🧠 Approach
- Rotate the matrix up to **4 times**
- After each rotation:
  - Compare rotated matrix with target  
- If any rotation matches, return **True**
- Otherwise, return **False**

---

## 🔍 Complexity Analysis

| Metric | Value |
|--------|------|
| Time Complexity | O(n²) |
| Space Complexity | O(n²) |

---

## 🚀 Key Concepts
- Matrix Rotation  
- Nested Lists  
- Simulation  
- Matrix Comparison  

---
