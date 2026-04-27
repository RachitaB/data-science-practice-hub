# 🐍 Spiral Order Traversal of Matrix

## 📌 Problem Statement
Given an **m × n matrix**, return all elements of the matrix in **spiral order**.

### 🌀 What is Spiral Order?
Traverse the matrix in this pattern:

1. Move **right** across the top row  
2. Move **down** the last column  
3. Move **left** across the bottom row  
4. Move **up** the first column  
5. Repeat the process **inward**

> Think of it like peeling layers of an onion 🧅

---

## 🧾 Example 1

### Input
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
## ✅ Output
```python
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 💡 Explanation
You traverse the matrix **layer by layer**:

- First outer layer  
- Then move inward  
- Continue until all elements are visited  

---

## 🧠 Approach
- Maintain **4 boundaries**:
  - `top`, `bottom`, `left`, `right`

- Traverse in 4 directions:
  - Left → Right  
  - Top → Bottom  
  - Right → Left  
  - Bottom → Top  

- After each traversal:
  - Shrink boundaries inward  

- Stop when all elements are collected  

---

## 🚀 Key Concepts
- Matrix Traversal  
- Boundary Control  
- Simulation  
- Directional Movement  
- Iterative Logic  

---
