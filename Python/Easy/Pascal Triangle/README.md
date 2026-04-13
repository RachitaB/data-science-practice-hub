# 🐍 Pascal's Triangle

## 📌 Problem Statement
Given an integer **numRows**, return the **first numRows rows** of **Pascal's Triangle**.

In Pascal's Triangle:

- The first and last element of each row is always **1**
- Every other element is the **sum of the two numbers directly above it**

---

## 📝 Pascal's Triangle Pattern

```python
        [1]
      [1, 1]
    [1, 2, 1]
  [1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

---

## 🧾 Example 1

### Input
```python
numRows = 1
```

### Output
```python
[[1]]
```

---

## 🧾 Example 2

### Input
```python
numRows = 4
```

### Output
```python
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
```

---

## 💡 Explanation
Each row is built using the previous row:

- Row 1 → `[1]`
- Row 2 → `[1, 1]`
- Row 3 → `[1, 2, 1]` → because **1+1 = 2**
- Row 4 → `[1, 3, 3, 1]` → because:
  - **1+2 = 3**
  - **2+1 = 3**

---

## 🧠 Approach
- Start with the first row: **[1]**
- For every new row:
  - Begin and end with **1**
  - Fill middle values using previous row:
  
> **new_row[i] = prev_row[i-1] + prev_row[i]**

- Repeat until **numRows** are generated

---

## 🚀 Python Solution

```python
def generate_pascal(numRows):
    triangle = []

    for i in range(numRows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
```

---

## 🔍 Complexity Analysis

| Metric | Value |
|--------|------|
| Time Complexity | O(n²) |
| Space Complexity | O(n²) |

---

## 🚀 Key Concepts
- Nested Loops  
- Dynamic Array Construction  
- Mathematical Patterns  
- Simulation Problems  

---
