# 🐍 Weakest Strong Link in a Matrix

## 📌 Problem Statement
You are given a matrix **strength** where:

- `strength[i][j]` represents the strength of the chain-link at position **(i, j)**
- All numbers in the matrix are **unique**

A **Weakest Strong Link** is defined as a value that is:

1. The **smallest value in its row**
2. The **largest value in its column**

Return the Weakest Strong Link if it exists; otherwise return **-1**.

> It is guaranteed that if one exists, there will be exactly **one**.

---

## 📝 Example 1

### Input

```python
strength = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
